"""
web/main.py — FastAPI web sayt
Render.com ga deploy qilish uchun mo'ljallangan.

Ishga tushirish:
  uvicorn web.main:app --reload
  yoki Render: uvicorn main:app --host 0.0.0.0 --port $PORT
"""

import sys, os, hashlib, hmac, sqlite3
from datetime import date, datetime, timedelta
from functools import wraps
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Request, Response, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from shared_config import (
    WEB_SECRET_KEY, BOT_TOKEN, BOT_USERNAME,
    SITE_URL, DB_NAME, SUBSCRIPTION_PLANS
)

# ===================== APP SETUP =====================

app = FastAPI(title="O'zbekiston Ta'lim")

# Session middleware (cookie-based)
app.add_middleware(SessionMiddleware, secret_key=WEB_SECRET_KEY,
                   max_age=60 * 60 * 24 * 30)  # 30 kun

# Static fayllar va templatelar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
templates.env.globals["BOT_USERNAME"] = BOT_USERNAME
templates.env.globals["SITE_URL"] = SITE_URL

# ===================== DATABASE =====================

def get_db_path():
    # Render.com da DB bot bilan bir joyda bo'lishi kerak
    # Loyiha ildizida axtaramiz
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root, DB_NAME)


def db_conn():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Sayt uchun qo'shimcha jadvallar."""
    conn = db_conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL,
            plan_id    TEXT NOT NULL,
            started_at TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            coin_spent INTEGER NOT NULL,
            is_active  INTEGER DEFAULT 1
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS coin_transfers (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id        INTEGER NOT NULL,
            amount         INTEGER NOT NULL,
            direction      TEXT NOT NULL,
            reason         TEXT,
            transferred_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()


@app.on_event("startup")
async def startup():
    init_db()


# ===================== HELPERS =====================

def get_session_user(request: Request) -> Optional[int]:
    return request.session.get("user_id")


def get_user_from_db(user_id: int):
    conn = db_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user


def get_active_sub(user_id: int):
    today = str(date.today())
    conn = db_conn()
    c = conn.cursor()
    c.execute("""
        SELECT * FROM subscriptions
        WHERE user_id=? AND is_active=1 AND expires_at>=?
        ORDER BY expires_at DESC LIMIT 1
    """, (user_id, today))
    sub = c.fetchone()
    conn.close()
    return sub


def verify_telegram_auth(data: dict) -> bool:
    """Telegram Login Widget ma'lumotlarini tekshirish."""
    check_hash = data.pop("hash", None)
    if not check_hash:
        return False
    data_str = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))
    secret   = hashlib.sha256(BOT_TOKEN.encode()).digest()
    calc     = hmac.new(secret, data_str.encode(), hashlib.sha256).hexdigest()
    # auth_date — 24 soatdan eski bo'lmasin
    if datetime.now().timestamp() - int(data.get("auth_date", 0)) > 86400:
        return False
    return hmac.compare_digest(calc, check_hash)


# ===================== SAHIFALAR =====================

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    if get_session_user(request):
        return RedirectResponse("/dashboard")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "plans": SUBSCRIPTION_PLANS,
    })


@app.get("/auth/telegram")
async def telegram_auth(request: Request):
    """Telegram Login Widget callback."""
    params = dict(request.query_params)
    user_id = int(params.get("id", 0))
    if not user_id:
        return RedirectResponse("/")

    # Production da tekshirishni yoqing:
    # data_copy = dict(params)
    # if not verify_telegram_auth(data_copy):
    #     raise HTTPException(403, "Auth xatosi")

    user = get_user_from_db(user_id)
    if not user:
        return templates.TemplateResponse("not_registered.html", {
            "request": request,
            "bot_username": BOT_USERNAME,
        })

    request.session["user_id"]    = user_id
    request.session["first_name"] = params.get("first_name", "")
    return RedirectResponse("/dashboard")


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    uid = get_session_user(request)
    if not uid:
        return RedirectResponse("/")

    user = get_user_from_db(uid)
    if not user:
        request.session.clear()
        return RedirectResponse("/")

    active_sub  = get_active_sub(uid)
    active_plan = SUBSCRIPTION_PLANS.get(active_sub["plan_id"]) if active_sub else None

    return templates.TemplateResponse("dashboard.html", {
        "request":     request,
        "user":        user,
        "active_sub":  active_sub,
        "active_plan": active_plan,
        "plans":       SUBSCRIPTION_PLANS,
    })


@app.get("/plans", response_class=HTMLResponse)
async def plans_page(request: Request):
    uid = get_session_user(request)
    if not uid:
        return RedirectResponse("/")

    user       = get_user_from_db(uid)
    active_sub = get_active_sub(uid)

    return templates.TemplateResponse("plans.html", {
        "request":    request,
        "user":       user,
        "active_sub": active_sub,
        "plans":      SUBSCRIPTION_PLANS,
    })


@app.post("/buy/{plan_id}")
async def buy_plan(plan_id: str, request: Request):
    uid = get_session_user(request)
    if not uid:
        return RedirectResponse("/", status_code=303)

    plan = SUBSCRIPTION_PLANS.get(plan_id)
    if not plan:
        return RedirectResponse("/plans?error=notfound", status_code=303)

    user = get_user_from_db(uid)
    cost = plan["narx_coin"]

    if user["coins"] < cost:
        return RedirectResponse(
            f"/plans?error=nocoin&need={cost}&have={user['coins']}",
            status_code=303
        )

    conn = db_conn()
    c = conn.cursor()

    # Oldingi obunani o'chirish
    c.execute("UPDATE subscriptions SET is_active=0 WHERE user_id=? AND is_active=1", (uid,))

    # Coinni ayirish
    c.execute("UPDATE users SET coins=coins-? WHERE user_id=?", (cost, uid))

    # Yangi obuna
    started = str(date.today())
    expires = str(date.today() + timedelta(days=plan["muddat_kun"]))
    c.execute("""
        INSERT INTO subscriptions (user_id, plan_id, started_at, expires_at, coin_spent)
        VALUES (?,?,?,?,?)
    """, (uid, plan_id, started, expires, cost))

    # Transfer tarixi
    c.execute("""
        INSERT INTO coin_transfers (user_id, amount, direction, reason)
        VALUES (?,?,'to_site',?)
    """, (uid, cost, f"{plan['nomi']} obuna sotib olindi"))

    conn.commit()
    conn.close()

    return RedirectResponse(f"/dashboard?success={plan_id}", status_code=303)


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/")


# ===================== API (Bot uchun) =====================

@app.get("/api/subscription/{user_id}")
async def api_subscription(user_id: int, request: Request):
    """Bot bu endpoint orqali obuna tekshiradi."""
    api_key = request.headers.get("X-API-Key", "")
    if api_key != BOT_TOKEN[:20]:
        raise HTTPException(401, "Unauthorized")

    sub = get_active_sub(user_id)
    if sub:
        plan = SUBSCRIPTION_PLANS.get(sub["plan_id"], {})
        return {
            "has_subscription": True,
            "plan_id":    sub["plan_id"],
            "plan_name":  plan.get("nomi", ""),
            "expires_at": sub["expires_at"],
            "emoji":      plan.get("emoji", ""),
            "joker_daily": plan.get("joker_daily", 0),
            "quiz_retry":  plan.get("quiz_retry", 1),
        }
    return {"has_subscription": False}
