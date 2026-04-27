"""
handlers/registration.py — Foydalanuvchi ro'yxatdan o'tish moduli

Bosqichlar (FSM States):
  1. Ism kiritish
  2. Familiya kiritish
  3. Yosh kiritish
  4. Telefon raqami
  5. Nechinchi sinf
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart

import database as db
from keyboards import main_menu_keyboard, registration_cancel_keyboard

router = Router()


class RegistrationStates(StatesGroup):
    """
    FSM (Finite State Machine) — bot holatlari.
    Har bir holat foydalanuvchi kiritadigan ma'lumotga mos keladi.
    """
    waiting_first_name  = State()  # Ism kutilmoqda
    waiting_last_name   = State()  # Familiya kutilmoqda
    waiting_age         = State()  # Yosh kutilmoqda
    waiting_phone       = State()  # Telefon kutilmoqda
    waiting_grade       = State()  # Sinf kutilmoqda


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """
    /start buyrug'i.
    Agar ro'yxatdan o'tgan bo'lsa — asosiy menyuni ko'rsatadi.
    Bo'lmasa — ro'yxatdan o'tishni boshlaydi.
    """
    user_id = message.from_user.id# type: ignore

    if db.is_registered(user_id):
        # Allaqachon ro'yxatdan o'tgan
        user = db.get_user(user_id)
        await message.answer(
            f"👋 Xush kelibsiz, <b>{user['first_name']}</b>!\n\n"
            f"🪙 Sizning coinlaringiz: <b>{user['coins']}</b>\n\n"
            f"Quyidagi menyudan tanlang:",
            reply_markup=main_menu_keyboard(),
            parse_mode="HTML"
        )
        await state.clear()
    else:
        # Yangi foydalanuvchi — ro'yxatdan o'tish
        await message.answer(
            "🇺🇿 <b>O'zbekiston Ta'lim Botiga Xush Kelibsiz!</b>\n\n"
            "Bu bot orqali siz:\n"
            "📍 O'zbekistonning barcha viloyatlari yodgorliklarini o'rganasiz\n"
            "📝 Bilimingizni quiz orqali sinab ko'rasiz\n"
            "🪙 Coin yig'ib, do'kondan sovg'alar olasiz\n\n"
            "━━━━━━━━━━━━━━━\n"
            "Boshlash uchun ro'yxatdan o'tishingiz kerak.\n\n"
            "👤 <b>Ismingizni kiriting:</b>",
            reply_markup=registration_cancel_keyboard(),
            parse_mode="HTML"
        )
        await state.set_state(RegistrationStates.waiting_first_name)


@router.callback_query(F.data == "cancel_registration")
async def cancel_registration(callback: CallbackQuery, state: FSMContext):
    """Ro'yxatdan o'tishni bekor qilish."""
    await state.clear()
    await callback.message.edit_text(# type: ignore
        "❌ Ro'yxatdan o'tish bekor qilindi.\n"
        "Qaytadan boshlash uchun /start yozing."
    )


@router.message(RegistrationStates.waiting_first_name)
async def process_first_name(message: Message, state: FSMContext):
    """Ism qabul qilish va keyingi holat."""
    first_name = message.text.strip()# type: ignore

    # Tekshiruv: ism kamida 2 harf bo'lishi kerak
    if len(first_name) < 2:
        await message.answer("⚠️ Ism kamida 2 harfdan iborat bo'lishi kerak. Qayta kiriting:")
        return
    if len(first_name) > 50:
        await message.answer("⚠️ Ism juda uzun. Iltimos qayta kiriting:")
        return

    # FSM ga ismni saqlaymiz
    await state.update_data(first_name=first_name)

    await message.answer(
        f"✅ Ism: <b>{first_name}</b>\n\n"
        "👤 <b>Familiyangizni kiriting:</b>",
        parse_mode="HTML"
    )
    await state.set_state(RegistrationStates.waiting_last_name)


@router.message(RegistrationStates.waiting_last_name)
async def process_last_name(message: Message, state: FSMContext):
    """Familiya qabul qilish."""
    last_name = message.text.strip()# type: ignore

    if len(last_name) < 2:
        await message.answer("⚠️ Familiya kamida 2 harfdan iborat bo'lishi kerak. Qayta kiriting:")
        return

    await state.update_data(last_name=last_name)

    await message.answer(
        f"✅ Familiya: <b>{last_name}</b>\n\n"
        "🔢 <b>Yoshingizni kiriting (faqat raqam, masalan: 12):</b>",
        parse_mode="HTML"
    )
    await state.set_state(RegistrationStates.waiting_age)


@router.message(RegistrationStates.waiting_age)
async def process_age(message: Message, state: FSMContext):
    """Yosh qabul qilish — faqat raqam bo'lishi kerak."""
    try:
        age = int(message.text.strip())# type: ignore
    except ValueError:
        await message.answer("⚠️ Yosh faqat raqam bo'lishi kerak! Masalan: 12")
        return

    # Maktab o'quvchisi uchun yosh 6-18 oralig'ida bo'lishi kerak
    if age < 6 or age > 18:
        await message.answer("⚠️ Yosh 6 dan 18 gacha bo'lishi kerak. Qayta kiriting:")
        return

    await state.update_data(age=age)

    await message.answer(
        f"✅ Yosh: <b>{age}</b>\n\n"
        "📱 <b>Telefon raqamingizni kiriting:</b>\n"
        "Misol: +998901234567",
        parse_mode="HTML"
    )
    await state.set_state(RegistrationStates.waiting_phone)


@router.message(RegistrationStates.waiting_phone)
async def process_phone(message: Message, state: FSMContext):
    """Telefon raqami qabul qilish."""
    phone = message.text.strip()# type: ignore

    # Telefon raqami tekshiruvi — +998 bilan boshlanishi yoki oddiy raqam
    cleaned = phone.replace('+', '').replace(' ', '').replace('-', '')
    if not cleaned.isdigit() or len(cleaned) < 9:
        await message.answer(
            "⚠️ Telefon raqami noto'g'ri. Iltimos qayta kiriting.\n"
            "Misol: +998901234567"
        )
        return

    await state.update_data(phone=phone)

    await message.answer(
        f"✅ Telefon: <b>{phone}</b>\n\n"
        "🏫 <b>Nechinchi sinfda o'qiyasiz?</b>\n"
        "Raqam kiriting (1 dan 11 gacha):",
        parse_mode="HTML"
    )
    await state.set_state(RegistrationStates.waiting_grade)


@router.message(RegistrationStates.waiting_grade)
async def process_grade(message: Message, state: FSMContext):
    """Sinf qabul qilish va ro'yxatdan o'tishni yakunlash."""
    try:
        grade = int(message.text.strip())# type: ignore
    except ValueError:
        await message.answer("⚠️ Sinf faqat raqam bo'lishi kerak! Masalan: 7")
        return

    if grade < 1 or grade > 11:
        await message.answer("⚠️ Sinf 1 dan 11 gacha bo'lishi kerak. Qayta kiriting:")
        return

    # FSM dan barcha ma'lumotlarni olamiz
    data = await state.get_data()

    # Ma'lumotlar bazasiga saqlaymiz
    db.register_user(
        user_id=message.from_user.id,# type: ignore
        username=message.from_user.username or "",# type: ignore
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        phone=data['phone'],
        school_grade=grade
    )

    await state.clear()  # FSM holatini tozalaymiz

    await message.answer(
        f"🎉 <b>Tabriklaymiz! Ro'yxatdan muvaffaqiyatli o'tdingiz!</b>\n\n"
        f"👤 Ism: <b>{data['first_name']} {data['last_name']}</b>\n"
        f"🎂 Yosh: <b>{data['age']}</b>\n"
        f"📱 Telefon: <b>{data['phone']}</b>\n"
        f"🏫 Sinf: <b>{grade}-sinf</b>\n\n"
        f"🪙 Boshlang'ich coinlar: <b>0</b>\n\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📚 O'rganishni boshlang va quiz ishlang!\n"
        f"Har kuni barcha joylardan 10/10 ball olsangiz — <b>1000 coin</b> topasiz! 🚀",
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML"
    )
