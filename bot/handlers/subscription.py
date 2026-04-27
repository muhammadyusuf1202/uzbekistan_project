"""
handlers/subscription.py — Botda foydalanuvchi obuna holatini ko'rish.
Obuna sotib olish esa sayt orqali amalga oshiriladi.
"""

import sqlite3
from datetime import date
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

try:
    from shared_config import SUBSCRIPTION_PLANS, SITE_URL, DB_NAME
except ImportError:
    # Agar shared_config topilmasa — bot/config.py dan olamiz
    from config import DB_NAME
    SITE_URL = "http://127.0.0.1:5000"
    SUBSCRIPTION_PLANS = {
        "pro":       {"nomi": "Pro",       "narx_coin": 1000,  "emoji": "💙"},
        "plus":      {"nomi": "Plus",      "narx_coin": 1500,  "emoji": "💜"},
        "ultra_plus":{"nomi": "Ultra Plus","narx_coin": 20000, "emoji": "👑"},
    }

router = Router()

# Obuna ranglari (Telegram HTML uchun)
PLAN_COLORS = {
    "pro":        ("💙", "#378ADD"),
    "plus":       ("💜", "#7F77DD"),
    "ultra_plus": ("👑", "#BA7517"),
}


def get_active_subscription(user_id: int):
    """Foydalanuvchining faol obunasini DB dan oladi."""
    db_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        DB_NAME
    )
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    today = str(date.today())
    cursor.execute("""
        SELECT * FROM subscriptions
        WHERE user_id = ? AND is_active = 1 AND expires_at >= ?
        ORDER BY expires_at DESC LIMIT 1
    """, (user_id, today))
    sub = cursor.fetchone()
    conn.close()
    return sub


def subscription_keyboard():
    """Obuna menyusi uchun tugmalar."""
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🌐 Saytda obuna olish",
        url=SITE_URL
    )
    builder.button(
        text="🔄 Obunani yangilash",
        callback_data="refresh_subscription"
    )
    builder.adjust(1)
    return builder.as_markup()


def plans_info_text(user_coins: int, active_sub=None) -> str:
    """Obuna rejalari haqida matn hosil qiladi."""
    lines = [
        "👑 <b>Obuna Rejalari</b>",
        "━━━━━━━━━━━━━━━",
        "",
    ]

    plans_display = [
        ("pro",       "💙", "Pro",       1_000,  ["Cheksiz quiz", "+50 bonus coin/kun", "Pro nishon"]),
        ("plus",      "💜", "Plus",      1_500,  ["Pro + yana ko'p", "+150 bonus coin/kun", "3 ta bepul joker/kun"]),
        ("ultra_plus","👑", "Ultra Plus",20_000, ["Hammasi cheksiz", "+500 bonus coin/kun", "Oltin nishon", "Admin bilan aloqa"]),
    ]

    for plan_id, emoji, nomi, narx, imtiyozlar in plans_display:
        is_active = active_sub and active_sub["plan_id"] == plan_id
        status = " ✅ <i>(Faol)</i>" if is_active else ""
        affordable = "✓" if user_coins >= narx else "✗"

        lines.append(f"{emoji} <b>{nomi}</b>{status}")
        lines.append(f"   💰 Narx: <b>{narx:,} 🪙</b>  {affordable}")
        for f in imtiyozlar:
            lines.append(f"   • {f}")
        lines.append("")

    lines.append(f"💰 Sizning coinlaringiz: <b>{user_coins:,} 🪙</b>")
    lines.append("")
    lines.append(f"🌐 Sotib olish uchun: <a href=\"{SITE_URL}\">{SITE_URL}</a>")

    return "\n".join(lines)


@router.message(F.text == "👑 Obuna")
async def cmd_subscription(message: Message):
    """Obuna menyusi."""
    from database import is_registered, get_user_coins
    if not is_registered(message.from_user.id):# type: ignore
        await message.answer("❌ Avval /start orqali ro'yxatdan o'ting!")
        return

    user_id = message.from_user.id# type: ignore
    user_coins = get_user_coins(user_id)
    active_sub = get_active_subscription(user_id)

    # Faol obuna ma'lumoti
    if active_sub:
        plan = SUBSCRIPTION_PLANS.get(active_sub["plan_id"], {})
        emoji = plan.get("emoji", "⭐")
        nomi  = plan.get("nomi", "Obuna")
        header = (
            f"{emoji} <b>Faol obunangiz: {nomi}</b>\n"
            f"📅 Muddat: <b>{active_sub['expires_at']}</b> gacha\n\n"
        )
    else:
        header = "ℹ️ <i>Faol obunangiz yo'q.</i>\n\n"

    text = header + plans_info_text(user_coins, active_sub)

    await message.answer(
        text,
        reply_markup=subscription_keyboard(),
        parse_mode="HTML",
        disable_web_page_preview=True
    )


@router.callback_query(F.data == "refresh_subscription")
async def refresh_subscription(callback: CallbackQuery):
    """Obuna holatini yangilash."""
    from database import get_user_coins
    user_id = callback.from_user.id
    user_coins = get_user_coins(user_id)
    active_sub = get_active_subscription(user_id)

    if active_sub:
        plan = SUBSCRIPTION_PLANS.get(active_sub["plan_id"], {})
        emoji = plan.get("emoji", "⭐")
        nomi  = plan.get("nomi", "Obuna")
        await callback.answer(
            f"✅ {emoji} {nomi} — {active_sub['expires_at']} gacha faol",
            show_alert=True
        )
    else:
        await callback.answer(
            "❌ Faol obuna topilmadi.\nSaytda sotib oling.",
            show_alert=True
        )

    text = plans_info_text(user_coins, active_sub)
    try:
        await callback.message.edit_text(# type: ignore
            text,
            reply_markup=subscription_keyboard(),
            parse_mode="HTML",
            disable_web_page_preview=True
        )
    except Exception:
        pass
