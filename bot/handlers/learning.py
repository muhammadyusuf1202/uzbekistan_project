"""
handlers/learning.py — Joy haqida ma'lumot berish moduli
Rasm + tavsif + faktlar ko'rsatadi
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InputMediaPhoto
import database as db
from keyboards import (
    viloyatlar_keyboard, places_keyboard,
    place_action_keyboard, main_menu_keyboard
)
from places_data import VILOYATLAR, PLACES

router = Router()


def check_registered(user_id):
    """Ro'yxatdan o'tganini tekshirish yordamchi funksiyasi."""
    return db.is_registered(user_id)


@router.message(F.text == "📚 O'rganish")
async def cmd_learn(message: Message):
    """O'rganish tugmasi — viloyatlar ro'yxatini ko'rsatadi."""
    if not check_registered(message.from_user.id):# type: ignore
        await message.answer("❌ Avval /start orqali ro'yxatdan o'ting!")
        return

    await message.answer(
        "📍 <b>O'zbekiston Viloyatlari</b>\n\n"
        "O'rganmoqchi bo'lgan viloyatingizni tanlang:",
        reply_markup=viloyatlar_keyboard(mode="learn"),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("viloyat_learn_"))
async def show_places(callback: CallbackQuery):
    """Viloyat tanlanganda — o'sha viloyatdagi joylarni ko'rsatadi."""
    # callback_data dan viloyat nomini ajratamiz
    # Format: "viloyat_learn_Buxoro viloyati"
    viloyat_nomi = callback.data.replace("viloyat_learn_", "")# type: ignore

    place_ids = VILOYATLAR.get(viloyat_nomi, [])
    joy_soni = len(place_ids)

    await callback.message.edit_text(# type: ignore
        f"📍 <b>{viloyat_nomi}</b>\n\n"
        f"Bu viloyatda <b>{joy_soni} ta</b> o'quv joyi mavjud.\n"
        f"O'rganmoqchi bo'lgan joyni tanlang:",
        reply_markup=places_keyboard(viloyat_nomi, mode="learn"),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "back_to_learn")
async def back_to_viloyatlar(callback: CallbackQuery):
    """Viloyatlar ro'yxatiga qaytish."""
    await callback.message.edit_text(# type: ignore
        "📍 <b>O'zbekiston Viloyatlari</b>\n\n"
        "O'rganmoqchi bo'lgan viloyatingizni tanlang:",
        reply_markup=viloyatlar_keyboard(mode="learn"),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("back_viloyatlar_learn"))
async def back_to_viloyatlar_from_places(callback: CallbackQuery):
    """Viloyatlar ro'yxatiga qaytish."""
    await callback.message.edit_text(# type: ignore
        "📍 <b>O'zbekiston Viloyatlari</b>\n\n"
        "O'rganmoqchi bo'lgan viloyatingizni tanlang:",
        reply_markup=viloyatlar_keyboard(mode="learn"),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("place_learn_"))
async def show_place_info(callback: CallbackQuery):
    """
    Joy haqida to'liq ma'lumot berish.
    Rasm + tavsif + faktlar ko'rsatadi.
    """
    place_id = callback.data.replace("place_learn_", "")# type: ignore
    place = PLACES.get(place_id)

    if not place:
        await callback.answer("❌ Joy topilmadi!", show_alert=True)
        return

    user_id = callback.from_user.id

    # O'rganilgan deb belgilaymiz
    db.mark_place_learned(user_id, place_id)

    # Faktlarni chiroyli formatlash
    faktlar_text = "\n".join([f"  • {f}" for f in place['faktlar']])

    caption = (
        f"{place['emoji']} <b>{place['nomi']}</b>\n"
        f"📍 {place['viloyat']}\n\n"
        f"📖 <b>Tavsif:</b>\n{place['tavsif']}\n\n"
        f"💡 <b>Qiziqarli faktlar:</b>\n{faktlar_text}\n\n"
        f"⭐ <b>Qiziqarli:</b>\n{place['qiziqarli']}"
    )

    # Rasm bilan ma'lumot yuborish
    try:
        await callback.message.answer_photo(# type: ignore
            photo=place['rasm_url'],
            caption=caption,
            reply_markup=place_action_keyboard(place_id),
            parse_mode="HTML"
        )
        # Oldingi xabarni o'chirish
        await callback.message.delete()# type: ignore
    except Exception:
        # Agar rasm yuklanmasa — matnsiz yuboramiz
        await callback.message.edit_text(# type: ignore
            caption + "\n\n🖼 (Rasm mavjud emas)",
            reply_markup=place_action_keyboard(place_id),
            parse_mode="HTML"
        )
