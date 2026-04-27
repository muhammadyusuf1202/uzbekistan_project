"""
handlers/quiz.py — Quiz moduli
Obuna limitlarini hisobga oladi:
  Pro:        2 marta qayta ishlash, 20 joker/kun
  Plus:       5 marta qayta ishlash, 50 joker/kun
  Ultra Plus: cheksiz qayta ishlash, cheksiz joker
  Obunasiz:   1 marta ishlash, 0 bepul joker
"""

import random
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import database as db
from keyboards import viloyatlar_keyboard, places_keyboard
from places_data import VILOYATLAR, PLACES, SAVOLLAR

router = Router()


class QuizStates(StatesGroup):
    answering = State()


def quiz_answer_keyboard(savol_index, joy_id, disabled_options=None,
                         joker_used=False, jokers_left=0):
    builder = InlineKeyboardBuilder()
    if disabled_options is None:
        disabled_options = []

    for harf in ['A', 'B', 'C', 'D']:
        if harf in disabled_options:
            builder.button(text="✖️", callback_data="joker_disabled")
        else:
            builder.button(text=harf,
                           callback_data=f"quiz_ans_{savol_index}_{joy_id}_{harf}")
    builder.adjust(4)

    if joker_used:
        builder.button(text="✅ Joker ishlatildi", callback_data="joker_used_info")
    elif jokers_left == -1:
        builder.button(text="🎯 50/50 Joker (cheksiz)",
                       callback_data=f"use_fifty_{savol_index}_{joy_id}")
    elif jokers_left > 0:
        builder.button(text=f"🎯 50/50 Joker ({jokers_left} ta qoldi)",
                       callback_data=f"use_fifty_{savol_index}_{joy_id}")
    else:
        builder.button(text="🎯 Joker yo'q — do'kondan oling",
                       callback_data="no_joker_hint")

    builder.adjust(4, 1)
    return builder.as_markup()


def build_question_text(place, savol_num, savol,
                        disabled_options=None,
                        natija_emoji=None, natija_text=None,
                        progress_bars=None):
    if disabled_options is None:
        disabled_options = []

    javoblar_lines = []
    for j in savol['javoblar']:
        harf = j[0]
        if harf in disabled_options:
            javoblar_lines.append(f"  ✖️ {j}")
        else:
            javoblar_lines.append(f"  {j}")

    header = (f"🎯 <b>{place.get('emoji','📍')} "
              f"{place.get('nomi','')} — Quiz</b>\n━━━━━━━━━━━━━━━\n")

    prev = f"{natija_emoji} <i>{natija_text}</i>\n\n" if natija_emoji else ""
    prog = f"{progress_bars}\n\n" if progress_bars else ""

    return (f"{header}{prev}{prog}"
            f"❓ <b>{savol_num}/10 savol:</b>\n\n"
            f"{savol['savol']}\n\n"
            f"{chr(10).join(javoblar_lines)}\n\n"
            f"Javobni tanlang:")


def get_retry_status_text(done, limit):
    """Qayta ishlash holati matni."""
    if limit == -1:
        return f"♾️ Cheksiz qayta ishlash ({done} marta ishlandi)"
    return f"🔁 Qayta ishlash: {done}/{limit}"


# ===================== HANDLERS =====================

@router.message(F.text == "📝 Quiz")
async def cmd_quiz(message: Message):
    if not db.is_registered(message.from_user.id):# type: ignore
        await message.answer("❌ Avval /start orqali ro'yxatdan o'ting!")
        return

    user_id = message.from_user.id# type: ignore
    limits = db.get_plan_limits(user_id)
    plan_id = limits["plan_id"]

    if plan_id:
        joker_info = ("cheksiz" if limits["joker_daily"] == -1
                      else f"kuniga {limits['joker_daily']} ta")
        retry_info = ("cheksiz" if limits["quiz_retry"] == -1
                      else f"kuniga {limits['quiz_retry']} marta")
        sub_text = (f"\n\n✨ <b>Obunangiz imtiyozlari:</b>\n"
                    f"  🎯 50/50 joker: {joker_info}\n"
                    f"  🔁 Qayta ishlash: {retry_info}")
    else:
        sub_text = "\n\n💡 <i>Obuna oling — ko'proq joker va qayta ishlash!</i>"

    await message.answer(
        f"📝 <b>Quiz — Bilimingizni Sinab Ko'ring!</b>\n\n"
        f"Har bir joy uchun <b>10 ta savol</b> beriladi.\n"
        f"Barcha joylardan <b>10/10</b> → <b>1000 🪙 coin</b>!"
        f"{sub_text}\n\n"
        f"📍 Viloyatni tanlang:",
        reply_markup=viloyatlar_keyboard(mode="quiz"),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("viloyat_quiz_"))
async def show_quiz_places(callback: CallbackQuery):
    viloyat = callback.data.replace("viloyat_quiz_", "")# type: ignore
    await callback.message.edit_text(# type: ignore
        f"📍 <b>{viloyat}</b>\n\nJoyni tanlang:",
        reply_markup=places_keyboard(viloyat, mode="quiz"),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("back_viloyatlar_quiz"))
async def back_viloyatlar_quiz(callback: CallbackQuery):
    await callback.message.edit_text(# type: ignore
        "📍 <b>Viloyatni tanlang:</b>",
        reply_markup=viloyatlar_keyboard(mode="quiz"),
        parse_mode="HTML"
    )


async def _begin_quiz(callback: CallbackQuery, state: FSMContext, place_id: str):
    """Quiz boshlash logikasi — ikkala handler ham shu funksiyani chaqiradi."""
    user_id = callback.from_user.id

    # ---- Limit tekshiruvi ----
    can, done, limit = db.can_retry_quiz(user_id, place_id)
    if not can:
        limit_txt = str(limit)
        await callback.answer(
            f"🚫 Bu joyni bugun {limit_txt} martadan ko'p ishlash mumkin emas!\n"
            f"Obuna oling yoki ertaga qayta urinib ko'ring.",
            show_alert=True
        )
        return

    place = PLACES.get(place_id)
    if not place:
        await callback.answer("❌ Joy topilmadi!", show_alert=True)
        return

    savollar = SAVOLLAR.get(place_id, [])
    if len(savollar) < 10:
        await callback.answer("❌ Bu joy uchun savollar tayyorlanmagan.", show_alert=True)
        return

    tanlangan = random.sample(savollar, 10)
    jokers_left = db.get_jokers_left_today(user_id)

    await state.update_data(
        place_id=place_id,
        savollar=tanlangan,
        joriy_savol=0,
        togri_javoblar=0,
        joker_used_on=None,
        disabled_options=[],
    )
    await state.set_state(QuizStates.answering)

    # Qayta ishlash info
    if done > 0:
        retry_txt = get_retry_status_text(done, limit)
        retry_note = f"\n<i>{retry_txt}</i>\n\n"
    else:
        retry_note = ""

    text = (f"🎯 <b>{place['emoji']} {place['nomi']} — Quiz</b>\n"
            f"━━━━━━━━━━━━━━━\n"
            f"{retry_note}"
            f"❓ <b>1/10 savol:</b>\n\n"
            f"{tanlangan[0]['savol']}\n\n"
            f"{chr(10).join('  ' + j for j in tanlangan[0]['javoblar'])}\n\n"
            f"Javobni tanlang:")

    await callback.message.edit_text(# type: ignore
        text,
        reply_markup=quiz_answer_keyboard(0, place_id, jokers_left=jokers_left),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("place_quiz_"))
async def start_place_quiz(callback: CallbackQuery, state: FSMContext):
    place_id = callback.data.replace("place_quiz_", "")# type: ignore
    await _begin_quiz(callback, state, place_id)


@router.callback_query(F.data.startswith("start_quiz_"))
async def start_quiz_from_learn(callback: CallbackQuery, state: FSMContext):
    place_id = callback.data.replace("start_quiz_", "")# type: ignore
    await _begin_quiz(callback, state, place_id)


# ====== JOKER ======

@router.callback_query(F.data == "no_joker_hint")
async def no_joker_hint(callback: CallbackQuery):
    await callback.answer(
        "🎯 Joker tugadi!\n"
        "Do'kondan 50 🪙 ga sotib oling\n"
        "yoki obuna oling.",
        show_alert=True
    )


@router.callback_query(F.data == "joker_disabled")
async def joker_disabled(callback: CallbackQuery):
    await callback.answer("Bu variant 50/50 bilan o'chirilgan ✖️")


@router.callback_query(F.data == "joker_used_info")
async def joker_used_info(callback: CallbackQuery):
    await callback.answer("✅ Joker bu savolda ishlatildi!")


@router.callback_query(QuizStates.answering, F.data.startswith("use_fifty_"))
async def use_fifty_fifty(callback: CallbackQuery, state: FSMContext):
    parts = callback.data.split("_")# type: ignore
    savol_index = int(parts[2])
    place_id = "_".join(parts[3:])

    data = await state.get_data()
    if savol_index != data['joriy_savol']:
        await callback.answer("⚠️ Bu savol o'tib ketgan!")
        return
    if data.get('joker_used_on') == savol_index:
        await callback.answer("✅ Joker bu savolda allaqachon ishlatildi!")
        return

    user_id = callback.from_user.id
    if not db.use_joker(user_id, "fifty_fifty"):
        await callback.answer(
            "❌ Joker qolmadi!\nDo'kondan sotib oling yoki obuna oling.",
            show_alert=True
        )
        return

    savol = data['savollar'][savol_index]
    togri = savol['togri']
    notogrilar = [h for h in ['A', 'B', 'C', 'D'] if h != togri]
    ochirilgan = random.sample(notogrilar, 2)

    await state.update_data(joker_used_on=savol_index, disabled_options=ochirilgan)

    jokers_left = db.get_jokers_left_today(user_id)
    left_txt = "cheksiz" if jokers_left == -1 else str(jokers_left)
    await callback.answer(f"🎯 50/50! 2 noto'g'ri o'chirildi. Qoldi: {left_txt}")

    place = PLACES.get(place_id, {})
    text = build_question_text(place, savol_index + 1, savol,
                               disabled_options=ochirilgan)
    await callback.message.edit_text(# type: ignore
        text,
        reply_markup=quiz_answer_keyboard(savol_index, place_id,
                                          disabled_options=ochirilgan,
                                          joker_used=True),
        parse_mode="HTML"
    )


# ====== JAVOB ======

@router.callback_query(QuizStates.answering, F.data.startswith("quiz_ans_"))
async def process_answer(callback: CallbackQuery, state: FSMContext):
    parts = callback.data.split("_")# type: ignore
    savol_index = int(parts[2])
    selected = parts[-1]

    data = await state.get_data()
    if savol_index != data['joriy_savol']:
        await callback.answer("⚠️ Bu savol allaqachon javoblangan!")
        return

    savollar       = data['savollar']
    togri_javoblar = data['togri_javoblar']
    place_id       = data['place_id']
    joriy          = savollar[savol_index]
    togri_harf     = joriy['togri']

    if selected == togri_harf:
        togri_javoblar += 1
        n_emoji, n_text = "✅", "To'g'ri!"
    else:
        togri_javob = joriy['javoblar'][ord(togri_harf) - ord('A')]
        n_emoji = "❌"
        n_text  = f"Noto'g'ri! To'g'ri: {togri_harf}) {togri_javob}"

    keyingi = savol_index + 1

    if keyingi >= 10:
        await state.update_data(togri_javoblar=togri_javoblar)
        await finish_quiz(callback, state, togri_javoblar, place_id, n_emoji, n_text)
        return

    await state.update_data(joriy_savol=keyingi,
                            togri_javoblar=togri_javoblar,
                            disabled_options=[])

    # Progress bar
    bars = ""
    for i in range(10):
        if i < keyingi:
            bars += "🟩" if (i < savol_index or selected == togri_harf) else "🟥"
        elif i == keyingi:
            bars += "🟨"
        else:
            bars += "⬜"
    bars += f" {keyingi}/10"

    place = PLACES.get(place_id, {})
    jokers_left = db.get_jokers_left_today(callback.from_user.id)

    text = build_question_text(place, keyingi + 1, savollar[keyingi],
                               natija_emoji=n_emoji, natija_text=n_text,
                               progress_bars=bars)
    await callback.message.edit_text(# type: ignore
        text,
        reply_markup=quiz_answer_keyboard(keyingi, place_id,
                                          jokers_left=jokers_left),
        parse_mode="HTML"
    )


async def finish_quiz(callback, state, togri_javoblar, place_id, n_emoji, n_text):
    user_id = callback.from_user.id
    place   = PLACES.get(place_id, {})
    ball    = togri_javoblar

    coin_earned = ball * 10 if ball >= 5 else 0
    db.save_quiz_result(user_id, place_id, ball, coin_earned)

    if ball == 10:   yulduz, rang = "⭐⭐⭐ MUKAMMAL!", "🟢"
    elif ball >= 8:  yulduz, rang = "⭐⭐ A'lo!", "🟢"
    elif ball >= 6:  yulduz, rang = "⭐ Yaxshi", "🟡"
    elif ball >= 4:  yulduz, rang = "😐 Qoniqarli", "🟠"
    else:            yulduz, rang = "😔 O'qishni davom eting", "🔴"

    coin_txt = f"+{coin_earned} 🪙" if coin_earned > 0 else "0 🪙 (5 dan past ball)"

    # Qayta ishlash imkoniyati
    can, done, limit = db.can_retry_quiz(user_id, place_id)
    if limit == -1:
        retry_txt = "♾️ Yana ishlashingiz mumkin (cheksiz)"
    elif can:
        retry_txt = f"🔁 Yana ishlashingiz mumkin ({done}/{limit})"
    else:
        retry_txt = f"🚫 Bugungi limit tugadi ({done}/{limit}) — ertaga qaytib keling"

    jokers_left = db.get_jokers_left_today(user_id)
    j_txt = "cheksiz" if jokers_left == -1 else str(jokers_left)

    result_text = (
        f"🏁 <b>Quiz Yakunlandi!</b>\n━━━━━━━━━━━━━━━\n"
        f"{n_emoji} <i>{n_text}</i>\n\n"
        f"📍 <b>{place.get('emoji','')} {place.get('nomi','')}</b>\n\n"
        f"{rang} <b>Natija: {ball}/10</b> — {yulduz}\n"
        f"🪙 Coin: {coin_txt}\n"
        f"🎯 Joker qoldi: {j_txt} ta\n\n"
        f"{retry_txt}\n\n"
        f"💰 Jami coinlar: <b>{db.get_user_coins(user_id)} 🪙</b>"
    )

    daily = db.check_and_award_daily_coin(user_id)
    if daily:
        result_text += ("\n\n🎉 <b>TABRIKLAYMIZ!</b> Bugun barcha joylardan "
                        "10/10 oldingiz!\n<b>+1000 🪙 mukofot!</b>")

    await state.clear()

    builder = InlineKeyboardBuilder()
    if can or limit == -1:
        builder.button(text="🔄 Shu joyni qayta ishlash",
                       callback_data=f"place_quiz_{place_id}")
    builder.button(text="📝 Boshqa joy quizi", callback_data="go_to_quiz_menu")
    builder.button(text="📚 O'rganishga qaytish", callback_data="go_to_learn_menu")
    builder.adjust(1)

    await callback.message.edit_text(result_text,
                                     reply_markup=builder.as_markup(),
                                     parse_mode="HTML")


@router.callback_query(F.data == "go_to_quiz_menu")
async def go_quiz_menu(callback: CallbackQuery):
    await callback.message.edit_text(# type: ignore
        "📝 <b>Viloyatni tanlang:</b>",
        reply_markup=viloyatlar_keyboard(mode="quiz"),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "go_to_learn_menu")
async def go_learn_menu(callback: CallbackQuery):
    await callback.message.edit_text(# type: ignore
        "📍 <b>Viloyatni tanlang:</b>",
        reply_markup=viloyatlar_keyboard(mode="learn"),
        parse_mode="HTML"
    )
