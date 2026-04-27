"""
keyboards.py - Barcha Telegram tugmalari (InlineKeyboard va ReplyKeyboard)
"""

from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from places_data import VILOYATLAR, PLACES


def main_menu_keyboard():
    """
    Asosiy menyu — ReplyKeyboard (pastki tugmalar).
    Har doim ekranda ko'rinib turadi.
    """
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="📚 O'rganish"),
        KeyboardButton(text="📝 Quiz")
    )
    builder.row(
        KeyboardButton(text="🪙 Mening Coinlarim"),
        KeyboardButton(text="🛒 Do'kon")
    )
    builder.row(
        KeyboardButton(text="📊 Statistikam"),
        KeyboardButton(text="ℹ️ Yordam")
    )
    builder.row(
        KeyboardButton(text="👑 Obuna"),
    )
    return builder.as_markup(resize_keyboard=True)


def viloyatlar_keyboard(mode="learn"):
    """
    Viloyatlar ro'yxati — Inline tugmalar.
    mode = 'learn' (o'rganish) yoki 'quiz' (savol ishlash)
    """
    builder = InlineKeyboardBuilder()
    for viloyat_nomi in VILOYATLAR.keys():
        # callback_data: "viloyat_learn_Buxoro viloyati" kabi format
        builder.button(
            text=f"📍 {viloyat_nomi}",
            callback_data=f"viloyat_{mode}_{viloyat_nomi}"
        )
    builder.adjust(1)  # Har bir qatorda 1 ta tugma
    return builder.as_markup()


def places_keyboard(viloyat_nomi, mode="learn"):
    """
    Ma'lum viloyatdagi joylar ro'yxati.
    """
    builder = InlineKeyboardBuilder()
    place_ids = VILOYATLAR.get(viloyat_nomi, [])
    for place_id in place_ids:
        place = PLACES.get(place_id)
        if place:
            builder.button(
                text=f"{place['emoji']} {place['nomi']}",
                callback_data=f"place_{mode}_{place_id}"
            )
    builder.button(text="⬅️ Orqaga", callback_data=f"back_viloyatlar_{mode}")
    builder.adjust(1)
    return builder.as_markup()


def place_action_keyboard(place_id):
    """
    Joy ma'lumotini ko'rgandan keyin — amallar.
    """
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📝 Bu joy bo'yicha quiz ishlash",
        callback_data=f"start_quiz_{place_id}"
    )
    builder.button(
        text="📋 Boshqa joylarni ko'rish",
        callback_data="back_to_learn"
    )
    builder.adjust(1)
    return builder.as_markup()


def quiz_answer_keyboard(savol_index, joy_id):
    """
    Quiz javobi uchun A, B, C, D tugmalar.
    """
    builder = InlineKeyboardBuilder()
    for harf in ['A', 'B', 'C', 'D']:
        builder.button(
            text=harf,
            callback_data=f"quiz_ans_{savol_index}_{joy_id}_{harf}"
        )
    builder.adjust(4)  # Barcha 4 ta bir qatorda
    return builder.as_markup()


def shop_keyboard():
    """
    Do'kon mahsulotlari — Inline tugmalar.
    """
    builder = InlineKeyboardBuilder()

    # Mahsulotlar ro'yxati: (id, nomi, narxi)
    shop_items = [
        ("fifty_fifty", "🎯 50/50 Joker (2 noto'g'ri o'chadi)", 50),
        ("stiker_pack", "🎨 Maxsus Stiker To'plami", 500),
        ("premium_badge", "⭐ Premium Nishon", 1000),
        ("extra_quiz", "📝 Qo'shimcha Quiz Urinish", 200),
        ("certificate", "🏆 O'rganish Sertifikati", 2000),
        ("exclusive_info", "🔓 Maxsus Ma'lumotlar Paketi", 1500),
        ("support_bot", "💙 Botga Ko'mak (Xayriya)", 300),
    ]

    for item_id, item_name, price in shop_items:
        builder.button(
            text=f"{item_name} — {price} 🪙",
            callback_data=f"buy_{item_id}_{price}"
        )
    builder.adjust(1)
    return builder.as_markup()


def confirm_buy_keyboard(item_id, item_name, price):
    """Xaridni tasdiqlash."""
    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"✅ Ha, {price} 🪙 sarflash",
        callback_data=f"confirm_buy_{item_id}_{price}"
    )
    builder.button(
        text="❌ Bekor qilish",
        callback_data="cancel_buy"
    )
    builder.adjust(1)
    return builder.as_markup()


def registration_cancel_keyboard():
    """Ro'yxatdan o'tishni bekor qilish."""
    builder = InlineKeyboardBuilder()
    builder.button(text="❌ Bekor qilish", callback_data="cancel_registration")
    return builder.as_markup()


def skip_keyboard():
    """O'tkazib yuborish tugmasi (optional maydonlar uchun)."""
    builder = ReplyKeyboardBuilder()
    builder.button(text="⏩ O'tkazib yuborish")
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def admin_panel_keyboard():
    """Admin panel tugmalari."""
    builder = InlineKeyboardBuilder()
    builder.button(text="👥 Barcha foydalanuvchilar", callback_data="admin_all_users")
    builder.button(text="📊 Umumiy statistika", callback_data="admin_stats")
    builder.button(text="🏆 Top 10 o'quvchi", callback_data="admin_top")
    builder.button(text="📅 Bugungi faollik", callback_data="admin_today")
    builder.adjust(1)
    return builder.as_markup()
