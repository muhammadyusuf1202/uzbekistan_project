"""
handlers/shop.py — Coin do'koni va foydalanuvchi statistikasi
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

import database as db
from keyboards import shop_keyboard, confirm_buy_keyboard, main_menu_keyboard

router = Router()

# Do'kon mahsulotlari (ID -> ma'lumot)
SHOP_ITEMS = {
    "fifty_fifty": {
        "nomi": "🎯 50/50 Joker",
        "narx": 50,
        "tavsif": (
            "Quiz paytida istalgan savolda ishlating!\n"
            "4 ta javobdan 2 ta NOTO'G'RI o'chiriladi.\n"
            "Faqat 1 to'g'ri + 1 noto'g'ri javob qoladi.\n"
            "Tanlov osonlashadi! ✂️"
        ),
        "yetkazish": "Darhol hisobga qo'shiladi. Quizda 🎯 tugmasi ko'rinadi.",
        "tur": "joker",
    },
    "stiker_pack": {
        "nomi": "🎨 Maxsus Stiker To'plami",
        "narx": 0,
        "tavsif": "O'zbekiston yodgorliklariga bag'ishlangan 20 ta maxsus stiker.",
        "yetkazish": "Admin tomonidan 24 soat ichida yuboriladi.Hozircha yo'q.",
        "tur": "sovga",
    },
    "premium_badge": {
        "nomi": "⭐ Premium Nishon",
        "narx": 0,
        "tavsif": "Profilingizda maxsus ⭐ nishoni paydo bo'ladi.",
        "yetkazish": "Darhol qo'shiladi.1 yilda keladi",
        "tur": "sovga",
    },
    "extra_quiz": {
        "nomi": "📝 Qo'shimcha Quiz Urinish",
        "narx": 200,
        "tavsif": "Bugun allaqachon ishlagan quiz uchun yana bir urinish.",
        "yetkazish": "Darhol faollashadi.",
        "tur": "sovga",
    },
    "certificate": {
        "nomi": "🏆 O'rganish Sertifikati",
        "narx": 0,
        "tavsif": "Barcha joylarni o'rganganingiz uchun rasmiy sertifikat.",
        "yetkazish": "Admin tomonidan PDF ko'rinishida yuboriladi.Qolmadi.",
        "tur": "sovga",
    },
    "exclusive_info": {
        "nomi": "🔓 Maxsus Ma'lumotlar Paketi",
        "narx": 1500,
        "tavsif": "Har bir joy haqida qo'shimcha chuqur ma'lumotlar — tarixiy lavhalar, maxfiy faktlar.",
        "yetkazish": "Darhol ochiladi.Admin jo'natadi.",
        "tur": "sovga",
    },
    "support_bot": {
        "nomi": "💙 Botga Ko'mak",
        "narx": 300,
        "tavsif": "Botni rivojlantirish uchun xayriya.",
        "yetkazish": "Rahmat! ❤️",
        "tur": "sovga",
    },
}


@router.message(F.text == "🛒 Do'kon")
async def cmd_shop(message: Message):
    """Do'kon menyusi."""
    if not db.is_registered(message.from_user.id):# type: ignore
        await message.answer("❌ Avval /start orqali ro'yxatdan o'ting!")
        return

    user_id = message.from_user.id# type: ignore
    coins = db.get_user_coins(user_id)
    fifty_count = db.get_joker_count(user_id, "fifty_fifty")

    await message.answer(
        f"🛒 <b>Coin Do'koni</b>\n\n"
        f"💰 Sizning coinlaringiz: <b>{coins} 🪙</b>\n"
        f"🎯 50/50 Jokerlaringiz: <b>{fifty_count} ta</b>\n\n"
        f"Quyidagi sovg'alardan birini tanlang:",
        reply_markup=shop_keyboard(),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("buy_"))
async def buy_item_confirm(callback: CallbackQuery):
    """
    Xarid tasdiqlash oynasi.
    Format: buy_{item_id}_{price}
    """
    parts = callback.data.split("_")# type: ignore
    price = int(parts[-1])
    item_id = "_".join(parts[1:-1])

    item = SHOP_ITEMS.get(item_id)
    if not item:
        await callback.answer("❌ Mahsulot topilmadi!", show_alert=True)
        return

    user_id = callback.from_user.id
    user_coins = db.get_user_coins(user_id)

    if user_coins < price:
        await callback.answer(
            f"❌ Yetarli coin yo'q!\n"
            f"Kerak: {price} 🪙\n"
            f"Sizda: {user_coins} 🪙",
            show_alert=True
        )
        return

    # 50/50 uchun qo'shimcha ma'lumot
    extra = ""
    if item_id == "fifty_fifty":
        current = db.get_joker_count(user_id, "fifty_fifty")
        extra = f"📦 Hozir: {current} ta → Xariddan keyin: {current + 1} ta\n\n"

    await callback.message.edit_text(# type: ignore
        f"🛍 <b>Xaridni tasdiqlang</b>\n\n"
        f"📦 <b>Mahsulot:</b> {item['nomi']}\n"
        f"📝 {item['tavsif']}\n\n"
        f"📬 <b>Yetkazib berish:</b> {item['yetkazish']}\n\n"
        f"{extra}"
        f"💰 <b>Narx:</b> {price} 🪙\n"
        f"💳 <b>Sizda:</b> {user_coins} 🪙\n"
        f"📊 <b>Qoladi:</b> {user_coins - price} 🪙\n\n"
        f"Tasdiqlaysizmi?",
        reply_markup=confirm_buy_keyboard(item_id, item['nomi'], price),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("confirm_buy_"))
async def confirm_purchase(callback: CallbackQuery):
    """
    Xaridni amalga oshirish.
    Format: confirm_buy_{item_id}_{price}
    """
    parts = callback.data.split("_")# type: ignore
    price = int(parts[-1])
    item_id = "_".join(parts[2:-1])

    item = SHOP_ITEMS.get(item_id)
    if not item:
        await callback.answer("❌ Mahsulot topilmadi!", show_alert=True)
        return

    user_id = callback.from_user.id

    # 50/50 joker uchun alohida logika: joker hisobiga qo'shamiz
    if item_id == "fifty_fifty":
        success = db.buy_joker(user_id, "fifty_fifty", item['nomi'], price)
        if success:
            remaining_coins = db.get_user_coins(user_id)
            new_count = db.get_joker_count(user_id, "fifty_fifty")
            await callback.message.edit_text(# type: ignore
                f"✅ <b>50/50 Joker xarid qilindi!</b>\n\n"
                f"🎯 Jokerlaringiz: <b>{new_count} ta</b>\n\n"
                f"💡 <i>Quiz paytida 🎯 tugmasini bosing — "
                f"2 ta noto'g'ri javob o'chib ketadi!</i>\n\n"
                f"💰 Qolgan coinlar: <b>{remaining_coins} 🪙</b>",
                parse_mode="HTML"
            )
        else:
            await callback.answer("❌ Xarid bajarilmadi. Coin yetarli emas.", show_alert=True)
    else:
        success = db.buy_item(user_id, item_id, item['nomi'], price)
        if success:
            remaining_coins = db.get_user_coins(user_id)
            await callback.message.edit_text(# type: ignore
                f"✅ <b>Xarid muvaffaqiyatli!</b>\n\n"
                f"📦 {item['nomi']}\n"
                f"📬 {item['yetkazish']}\n\n"
                f"💰 Qolgan coinlar: <b>{remaining_coins} 🪙</b>",
                parse_mode="HTML"
            )
        else:
            await callback.answer("❌ Xarid bajarilmadi. Coin yetarli emas.", show_alert=True)


@router.callback_query(F.data == "cancel_buy")
async def cancel_purchase(callback: CallbackQuery):
    """Xaridni bekor qilish."""
    user_id = callback.from_user.id
    coins = db.get_user_coins(user_id)
    fifty_count = db.get_joker_count(user_id, "fifty_fifty")
    await callback.message.edit_text(# type: ignore
        f"❌ Xarid bekor qilindi.\n\n"
        f"💰 Sizning coinlaringiz: <b>{coins} 🪙</b>\n"
        f"🎯 50/50 Jokerlaringiz: <b>{fifty_count} ta</b>\n\n"
        f"Boshqa mahsulotni tanlang:",
        reply_markup=shop_keyboard(),
        parse_mode="HTML"
    )


@router.message(F.text == "🪙 Mening Coinlarim")
async def cmd_my_coins(message: Message):
    """Coin va statistika ko'rish."""
    if not db.is_registered(message.from_user.id):# type: ignore
        await message.answer("❌ Avval /start orqali ro'yxatdan o'ting!")
        return

    user_id = message.from_user.id# type: ignore
    user = db.get_user(user_id)
    stats = db.get_user_quiz_stats(user_id)
    purchases = db.get_user_purchases(user_id)
    fifty_count = db.get_joker_count(user_id, "fifty_fifty")

    total_quizzes = stats['total_quizzes'] or 0
    perfect_scores = stats['perfect_scores'] or 0

    purchase_text = ""
    if purchases:
        purchase_text = "\n\n🛍 <b>So'nggi xaridlar:</b>\n"
        for p in purchases[:3]:
            purchase_text += f"  • {p['item_name']} ({p['cost_coins']} 🪙)\n"
    else:
        purchase_text = "\n\n🛍 <i>Hali xarid qilmadingiz</i>"

    await message.answer(
        f"💰 <b>Mening Hisobim</b>\n"
        f"━━━━━━━━━━━━━━━\n"
        f"👤 <b>{user['first_name']} {user['last_name'] or ''}</b>\n"
        f"🏫 {user['school_grade']}-sinf o'quvchisi\n\n"
        f"🪙 <b>Coinlar:</b> {user['coins']}\n"
        f"🎯 <b>50/50 Joker:</b> {fifty_count} ta\n\n"
        f"📊 <b>Quiz statistikasi:</b>\n"
        f"  📝 Jami quiz: {total_quizzes}\n"
        f"  ⭐ 10/10 ball: {perfect_scores}\n\n"
        f"💡 <i>Har kuni barcha joylardan 10/10 olsangiz — 1000 🪙!</i>"
        f"{purchase_text}",
        parse_mode="HTML"
    )


@router.message(F.text == "📊 Statistikam")
async def cmd_my_stats(message: Message):
    """Foydalanuvchi o'z statistikasini ko'radi."""
    if not db.is_registered(message.from_user.id):# type: ignore
        await message.answer("❌ Avval /start orqali ro'yxatdan o'ting!")
        return

    user_id = message.from_user.id# type: ignore
    learned = db.get_learned_places(user_id)
    stats = db.get_user_quiz_stats(user_id)
    top = db.get_top_users(10)
    fifty_count = db.get_joker_count(user_id, "fifty_fifty")

    total_places = 21
    learned_count = len(learned)
    progress_pct = int((learned_count / total_places) * 100)

    filled = int(progress_pct / 10)
    bar = "🟩" * filled + "⬜" * (10 - filled)

    user_rank = "—"
    my_user = db.get_user(user_id)
    for i, u in enumerate(top, 1):
        if u['first_name'] == my_user['first_name']:
            user_rank = str(i)
            break

    await message.answer(
        f"📊 <b>Mening Statistikam</b>\n"
        f"━━━━━━━━━━━━━━━\n\n"
        f"📚 <b>O'rganish:</b>\n"
        f"  {bar}\n"
        f"  {learned_count}/{total_places} joy o'rganildi ({progress_pct}%)\n\n"
        f"📝 <b>Quizlar:</b>\n"
        f"  Jami: {stats['total_quizzes'] or 0}\n"
        f"  10/10 ball: {stats['perfect_scores'] or 0} marta\n\n"
        f"🎯 <b>50/50 Joker:</b> {fifty_count} ta qoldi\n\n"
        f"🏆 <b>Reyting:</b> Top {user_rank}\n"
        f"🪙 <b>Coinlar:</b> {db.get_user_coins(user_id)}\n\n"
        f"💡 <i>Barcha joylarni o'rganing va top o'rinni egallang!</i>",
        parse_mode="HTML"
    )


@router.message(F.text == "ℹ️ Yordam")
async def cmd_help(message: Message):
    """Yordam matni."""
    await message.answer(
        "ℹ️ <b>Bot Haqida</b>\n"
        "━━━━━━━━━━━━━━━\n\n"
        "🇺🇿 <b>O'zbekiston Ta'lim Boti</b> — maktab o'quvchilari uchun\n\n"
        "📚 <b>O'rganish</b> — har bir viloyat yodgorliklarini rasm va ma'lumot bilan o'rganing\n\n"
        "📝 <b>Quiz</b> — har bir joy uchun 10 savol; to'g'ri javob uchun coin topasiz\n\n"
        "🎯 <b>50/50 Joker</b> — do'kondan 50 🪙 ga sotib oling.\n"
        "Quiz paytida 🎯 tugmasini bosing — 4 ta javobdan 2 ta noto'g'ri o'chib ketadi!\n\n"
        "🪙 <b>Coinlar tizimi:</b>\n"
        "  • 5+ ball = ball × 10 coin\n"
        "  • Barcha joylar 10/10 = +1000 coin\n\n"
        "🛒 <b>Do'kon</b> — coinlarga sovg'alar sotib oling\n\n"
        "━━━━━━━━━━━━━━━\n"
        "🆘 Muammo bo'lsa — /start yozing",
        parse_mode="HTML"
    )
