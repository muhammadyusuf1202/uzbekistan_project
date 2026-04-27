"""
database.py — SQLite ma'lumotlar bazasi
"""

import sqlite3
import os
from datetime import date
from config import DB_NAME


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id      INTEGER PRIMARY KEY,
            username     TEXT,
            first_name   TEXT NOT NULL,
            last_name    TEXT,
            age          INTEGER,
            phone        TEXT,
            school_grade INTEGER,
            coins        INTEGER DEFAULT 0,
            registered_at TEXT DEFAULT (date('now')),
            is_active    INTEGER DEFAULT 1
        )
    """)

    # quiz_results: attempts sonini saqlaymiz (completed emas, count)
    c.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            place_id    TEXT NOT NULL,
            quiz_date   TEXT NOT NULL,
            attempt_num INTEGER DEFAULT 1,
            score       INTEGER DEFAULT 0,
            completed   INTEGER DEFAULT 0,
            coin_earned INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS daily_rewards (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            reward_date TEXT NOT NULL,
            coins_earned INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            UNIQUE (user_id, reward_date)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS shop_orders (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            item_id     TEXT NOT NULL,
            item_name   TEXT NOT NULL,
            cost_coins  INTEGER NOT NULL,
            ordered_at  TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS user_jokers (
            user_id     INTEGER NOT NULL,
            joker_type  TEXT NOT NULL,
            count       INTEGER DEFAULT 0,
            last_reset  TEXT DEFAULT (date('now')),
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            PRIMARY KEY (user_id, joker_type)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS learning_progress (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            place_id    TEXT NOT NULL,
            learned_at  TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            UNIQUE (user_id, place_id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL,
            plan_id    TEXT NOT NULL,
            started_at TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            coin_spent INTEGER NOT NULL,
            is_active  INTEGER DEFAULT 1,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Ma'lumotlar bazasi jadvallari yaratildi.")


# ===================== FOYDALANUVCHI =====================

def register_user(user_id, username, first_name, last_name, age, phone, school_grade):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO users
        (user_id, username, first_name, last_name, age, phone, school_grade, coins)
        VALUES (?, ?, ?, ?, ?, ?, ?,
            COALESCE((SELECT coins FROM users WHERE user_id = ?), 0))
    """, (user_id, username, first_name, last_name, age, phone, school_grade, user_id))
    conn.commit()
    conn.close()


def get_user(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user


def is_registered(user_id):
    return get_user(user_id) is not None


def get_user_coins(user_id):
    user = get_user(user_id)
    return user['coins'] if user else 0


def add_coins(user_id, amount):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET coins = coins + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()


def deduct_coins(user_id, amount):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT coins FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    if not row or row['coins'] < amount:
        conn.close()
        return False
    c.execute("UPDATE users SET coins = coins - ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()
    return True


# ===================== OBUNA =====================

def get_active_subscription(user_id):
    """Foydalanuvchining faol obunasini qaytaradi."""
    today = str(date.today())
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT * FROM subscriptions
        WHERE user_id = ? AND is_active = 1 AND expires_at >= ?
        ORDER BY expires_at DESC LIMIT 1
    """, (user_id, today))
    sub = c.fetchone()
    conn.close()
    return sub


def get_plan_limits(user_id):
    """
    Foydalanuvchi obuna rejasi limitlarini qaytaradi.
    Obuna yo'q bo'lsa — standart (joker=0, retry=1).
    """
    try:
        from shared_config import SUBSCRIPTION_PLANS
    except ImportError:
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from shared_config import SUBSCRIPTION_PLANS

    sub = get_active_subscription(user_id)
    if not sub:
        return {"joker_daily": 0, "quiz_retry": 1, "bonus_coin": 0, "plan_id": None}

    plan = SUBSCRIPTION_PLANS.get(sub["plan_id"], {})
    return {
        "joker_daily": plan.get("joker_daily", 0),
        "quiz_retry":  plan.get("quiz_retry",  1),
        "bonus_coin":  plan.get("bonus_coin",  0),
        "plan_id":     sub["plan_id"],
    }


# ===================== QUIZ =====================

def get_today_quiz_count(user_id, place_id):
    """Bugun bu joy uchun necha marta quiz ishlangan."""
    today = str(date.today())
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT COUNT(*) as cnt FROM quiz_results
        WHERE user_id = ? AND place_id = ? AND quiz_date = ? AND completed = 1
    """, (user_id, place_id, today))
    cnt = c.fetchone()['cnt']
    conn.close()
    return cnt


def get_today_quiz(user_id, place_id):
    """Orqaga mos kelish uchun — bugungi birinchi quiz."""
    today = str(date.today())
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT * FROM quiz_results
        WHERE user_id = ? AND place_id = ? AND quiz_date = ?
        ORDER BY attempt_num DESC LIMIT 1
    """, (user_id, place_id, today))
    result = c.fetchone()
    conn.close()
    return result


def can_retry_quiz(user_id, place_id):
    """
    Foydalanuvchi bu joyni qayta ishlay oladimi?
    Qaytadi: (True/False, necha marta ishlagani, limit)
    """
    limits = get_plan_limits(user_id)
    retry_limit = limits["quiz_retry"]  # -1 = cheksiz
    done_count  = get_today_quiz_count(user_id, place_id)

    if retry_limit == -1:
        return True, done_count, -1
    return done_count < retry_limit, done_count, retry_limit


def save_quiz_result(user_id, place_id, score, coin_earned):
    """Quiz natijasini yangi qator sifatida saqlaymiz (har urinish alohida)."""
    today = str(date.today())
    conn = get_connection()
    c = conn.cursor()
    # Bugungi urinish raqamini topamiz
    c.execute("""
        SELECT COALESCE(MAX(attempt_num), 0) + 1 as next_num
        FROM quiz_results
        WHERE user_id = ? AND place_id = ? AND quiz_date = ?
    """, (user_id, place_id, today))
    next_num = c.fetchone()['next_num']

    c.execute("""
        INSERT INTO quiz_results
        (user_id, place_id, quiz_date, attempt_num, score, completed, coin_earned)
        VALUES (?, ?, ?, ?, ?, 1, ?)
    """, (user_id, place_id, today, next_num, score, coin_earned))
    conn.commit()
    conn.close()

    if coin_earned > 0:
        add_coins(user_id, coin_earned)


def check_and_award_daily_coin(user_id):
    from places_data import PLACES
    today = str(date.today())
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM daily_rewards WHERE user_id = ? AND reward_date = ?",
              (user_id, today))
    if c.fetchone():
        conn.close()
        return False

    # Bugun 10/10 ball olgan joylar soni
    c.execute("""
        SELECT COUNT(DISTINCT place_id) as cnt FROM quiz_results
        WHERE user_id = ? AND quiz_date = ? AND score = 10
    """, (user_id, today))
    perfect_count = c.fetchone()['cnt']
    conn.close()

    if perfect_count >= len(PLACES):
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO daily_rewards (user_id, reward_date, coins_earned) VALUES (?,?,1000)",
                  (user_id, today))
        conn.commit()
        conn.close()
        add_coins(user_id, 1000)
        return True
    return False


def get_user_quiz_stats(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT
            COUNT(*) as total_quizzes,
            SUM(score) as total_score,
            SUM(coin_earned) as total_coins_from_quiz,
            COUNT(CASE WHEN score = 10 THEN 1 END) as perfect_scores
        FROM quiz_results WHERE user_id = ?
    """, (user_id,))
    stats = c.fetchone()
    conn.close()
    return stats


# ===================== JOKER =====================

def get_joker_count(user_id, joker_type):
    """Foydalanuvchida qancha joker bor (sotib olingan + kunlik bepul)."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT count FROM user_jokers WHERE user_id=? AND joker_type=?",
              (user_id, joker_type))
    row = c.fetchone()
    conn.close()
    return row['count'] if row else 0


def get_total_jokers_available(user_id, joker_type="fifty_fifty"):
    """
    Jami mavjud jokerlar = sotib olingan + obunadan kunlik bepul.
    Obuna bepul jokerlari har kuni yangilanadi.
    """
    limits = get_plan_limits(user_id)
    plan_daily = limits["joker_daily"]   # -1=cheksiz
    purchased  = get_joker_count(user_id, joker_type)

    if plan_daily == -1:
        return -1  # cheksiz

    # Kunlik bepul jokerlar (bugun necha marta ishlatildi?)
    today = str(date.today())
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT COALESCE(daily_used, 0) as used
        FROM user_jokers
        WHERE user_id=? AND joker_type=?
    """, (user_id, joker_type))
    row = c.fetchone()
    conn.close()

    daily_used = 0
    if row:
        # last_reset sana bilan tekshiramiz
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT last_reset FROM user_jokers WHERE user_id=? AND joker_type=?",
                  (user_id, joker_type))
        r = c.fetchone()
        conn.close()
        if r and r['last_reset'] == today:
            daily_used = 0  # today_used boshqa jadvalda saqlash kerak bo'ladi — quyida

    # Soddalashtirish: kunlik joker va sotib olingan joker yig'indisi
    return purchased + max(0, plan_daily)


def use_joker(user_id, joker_type):
    """
    Joker ishlatish:
    1. Avval sotib olingan jokerdan ayiradi
    2. Agar yo'q bo'lsa, kunlik bepul jokerdan foydalanadi
    Qaytadi: True yoki False
    """
    limits = get_plan_limits(user_id)
    plan_daily = limits["joker_daily"]

    # Cheksiz (Ultra Plus)
    if plan_daily == -1:
        return True

    purchased = get_joker_count(user_id, joker_type)
    if purchased > 0:
        # Sotib olingan jokerdan ayiramiz
        conn = get_connection()
        c = conn.cursor()
        c.execute("UPDATE user_jokers SET count = count - 1 WHERE user_id=? AND joker_type=?",
                  (user_id, joker_type))
        conn.commit()
        conn.close()
        return True

    if plan_daily > 0:
        # Kunlik bepul joker — daily_joker_usage jadvalidan tekshiramiz
        today = str(date.today())
        conn = get_connection()
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS daily_joker_usage (
                user_id    INTEGER NOT NULL,
                joker_type TEXT NOT NULL,
                used_date  TEXT NOT NULL,
                used_count INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, joker_type, used_date)
            )
        """)
        c.execute("""
            SELECT used_count FROM daily_joker_usage
            WHERE user_id=? AND joker_type=? AND used_date=?
        """, (user_id, joker_type, today))
        row = c.fetchone()
        used_today = row['used_count'] if row else 0

        if used_today < plan_daily:
            c.execute("""
                INSERT INTO daily_joker_usage (user_id, joker_type, used_date, used_count)
                VALUES (?, ?, ?, 1)
                ON CONFLICT(user_id, joker_type, used_date)
                DO UPDATE SET used_count = used_count + 1
            """, (user_id, joker_type, today))
            conn.commit()
            conn.close()
            return True
        conn.close()
        return False

    return False


def get_jokers_left_today(user_id, joker_type="fifty_fifty"):
    """Bugun necha ta joker qolgan (bepul + sotib olingan)."""
    limits = get_plan_limits(user_id)
    plan_daily = limits["joker_daily"]

    if plan_daily == -1:
        return -1  # cheksiz

    purchased = get_joker_count(user_id, joker_type)
    if purchased > 0:
        return purchased + max(0, plan_daily)

    today = str(date.today())
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute("""
            SELECT used_count FROM daily_joker_usage
            WHERE user_id=? AND joker_type=? AND used_date=?
        """, (user_id, joker_type, today))
        row = c.fetchone()
        used = row['used_count'] if row else 0
    except Exception:
        used = 0
    conn.close()

    remaining = plan_daily - used
    return max(0, remaining)


def buy_joker(user_id, joker_type, item_name, cost_coins):
    if not deduct_coins(user_id, cost_coins):
        return False
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO user_jokers (user_id, joker_type, count)
        VALUES (?, ?, 1)
        ON CONFLICT(user_id, joker_type) DO UPDATE SET count = count + 1
    """, (user_id, joker_type))
    c.execute("INSERT INTO shop_orders (user_id, item_id, item_name, cost_coins) VALUES (?,?,?,?)",
              (user_id, joker_type, item_name, cost_coins))
    conn.commit()
    conn.close()
    return True


# ===================== DO'KON =====================

def buy_item(user_id, item_id, item_name, cost_coins):
    if deduct_coins(user_id, cost_coins):
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO shop_orders (user_id, item_id, item_name, cost_coins) VALUES (?,?,?,?)",
                  (user_id, item_id, item_name, cost_coins))
        conn.commit()
        conn.close()
        return True
    return False


def get_user_purchases(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM shop_orders WHERE user_id = ? ORDER BY ordered_at DESC",
              (user_id,))
    purchases = c.fetchall()
    conn.close()
    return purchases


# ===================== O'RGANISH =====================

def mark_place_learned(user_id, place_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO learning_progress (user_id, place_id) VALUES (?,?)",
              (user_id, place_id))
    conn.commit()
    conn.close()


def get_learned_places(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT place_id FROM learning_progress WHERE user_id = ?", (user_id,))
    places = [row['place_id'] for row in c.fetchall()]
    conn.close()
    return places


# ===================== ADMIN =====================

def get_all_users():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT u.*,
               COUNT(DISTINCT qr.place_id) as quizzes_done,
               COALESCE(SUM(qr.score), 0) as total_score
        FROM users u
        LEFT JOIN quiz_results qr ON u.user_id = qr.user_id
        GROUP BY u.user_id
        ORDER BY u.coins DESC
    """)
    users = c.fetchall()
    conn.close()
    return users


def get_total_stats():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) as cnt FROM users"); total_users = c.fetchone()['cnt']
    c.execute("SELECT COUNT(*) as cnt FROM quiz_results WHERE completed=1"); total_quizzes = c.fetchone()['cnt']
    c.execute("SELECT SUM(coins) as total FROM users"); r = c.fetchone(); total_coins = r['total'] or 0
    c.execute("SELECT COUNT(*) as cnt FROM quiz_results WHERE quiz_date=date('now')"); today_quizzes = c.fetchone()['cnt']
    c.execute("SELECT COUNT(*) as cnt FROM users WHERE registered_at=date('now')"); today_new = c.fetchone()['cnt']
    conn.close()
    return {'total_users': total_users, 'total_quizzes': total_quizzes,
            'total_coins': total_coins, 'today_quizzes': today_quizzes, 'today_new_users': today_new}


def get_top_users(limit=10):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT first_name, last_name, school_grade, coins FROM users ORDER BY coins DESC LIMIT ?", (limit,))
    top = c.fetchall()
    conn.close()
    return top
