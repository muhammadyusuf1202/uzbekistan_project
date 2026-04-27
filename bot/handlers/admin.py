"""
handlers/admin.py — Admin panel
Faqat config.py dagi ADMIN_IDS ro'yxatidagi adminlar foydalanishi mumkin.
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import database as db
from config import ADMIN_IDS
from keyboards import admin_panel_keyboard

router = Router()


def is_admin(user_id: int) -> bool:
    """Bu foydalanuvchi admin ekanini tekshiradi."""
    return user_id in ADMIN_IDS


@router.message(Command("admin"))
async def cmd_admin(message: Message):
    """/admin buyrug'i — faqat adminlar uchun."""
    if not is_admin(message.from_user.id): # type: ignore
        await message.answer("❌ Siz admin emassiz!")
        return

    stats = db.get_total_stats()

    await message.answer(
        f"🛡 <b>Admin Panel</b>\n"
        f"━━━━━━━━━━━━━━━\n\n"
        f"👥 Jami foydalanuvchilar: <b>{stats['total_users']}</b>\n"
        f"📝 Jami quizlar: <b>{stats['total_quizzes']}</b>\n"
        f"🪙 Jami coinlar: <b>{stats['total_coins']}</b>\n\n"
        f"📅 <b>Bugun:</b>\n"
        f"  Yangi foydalanuvchilar: {stats['today_new_users']}\n"
        f"  Quizlar: {stats['today_quizzes']}\n\n"
        f"Quyidagi amallardan birini tanlang:",
        reply_markup=admin_panel_keyboard(),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "admin_stats")
async def admin_stats(callback: CallbackQuery):
    """Umumiy statistika."""
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Ruxsat yo'q!", show_alert=True)
        return

    stats = db.get_total_stats()

    await callback.message.edit_text(# type: ignore
        f"📊 <b>Umumiy Statistika</b>\n"
        f"━━━━━━━━━━━━━━━\n\n"
        f"👥 Jami foydalanuvchilar: <b>{stats['total_users']}</b>\n"
        f"📝 Jami ishlangan quizlar: <b>{stats['total_quizzes']}</b>\n"
        f"🪙 Botda muomaladagi coinlar: <b>{stats['total_coins']}</b>\n\n"
        f"📅 <b>Bugungi faollik:</b>\n"
        f"  🆕 Yangi foydalanuvchilar: <b>{stats['today_new_users']}</b>\n"
        f"  📝 Quizlar: <b>{stats['today_quizzes']}</b>",
        reply_markup=admin_panel_keyboard(),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "admin_top")
async def admin_top_users(callback: CallbackQuery):
    """Top 10 foydalanuvchilar."""
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Ruxsat yo'q!", show_alert=True)
        return

    top = db.get_top_users(10)

    if not top:
        await callback.message.edit_text(# type: ignore
            "📊 Hali foydalanuvchilar yo'q.",
            reply_markup=admin_panel_keyboard()
        )
        return

    text = "🏆 <b>Top 10 O'quvchi (Coinlar bo'yicha)</b>\n━━━━━━━━━━━━━━━\n\n"
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    for i, user in enumerate(top):
        medal = medals[i] if i < len(medals) else f"{i+1}."
        full_name = f"{user['first_name']}"
        if user['last_name']:
            full_name += f" {user['last_name']}"
        text += (
            f"{medal} <b>{full_name}</b>\n"
            f"   🏫 {user['school_grade']}-sinf | 🪙 {user['coins']}\n\n"
        )

    await callback.message.edit_text(# type: ignore
        text,
        reply_markup=admin_panel_keyboard(),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "admin_all_users")
async def admin_all_users(callback: CallbackQuery):
    """Barcha foydalanuvchilar ro'yxati."""
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Ruxsat yo'q!", show_alert=True)
        return

    users = db.get_all_users()

    if not users:
        await callback.message.edit_text(# type: ignore
            "👥 Hali foydalanuvchilar yo'q.",
            reply_markup=admin_panel_keyboard()
        )
        return

    text = f"👥 <b>Barcha Foydalanuvchilar ({len(users)} ta)</b>\n━━━━━━━━━━━━━━━\n\n"

    # Telegram xabar chegarasi = 4096 belgi
    # Agar ko'p bo'lsa, faqat birinchi 20 tasini ko'rsatamiz
    for user in users[:20]:
        full_name = user['first_name']
        if user['last_name']:
            full_name += f" {user['last_name']}"
        username = f"@{user['username']}" if user['username'] else "username yo'q"
        text += (
            f"👤 <b>{full_name}</b> ({username})\n"
            f"   🏫 {user['school_grade']}-sinf | 🎂 {user['age']} yosh\n"
            f"   📱 {user['phone']} | 🪙 {user['coins']}\n"
            f"   📝 Quiz: {user['quizzes_done']} ta\n\n"
        )

    if len(users) > 20:
        text += f"\n... va yana {len(users) - 20} ta foydalanuvchi"

    await callback.message.edit_text(# type: ignore
        text,
        reply_markup=admin_panel_keyboard(),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "admin_today")
async def admin_today_activity(callback: CallbackQuery):
    """Bugungi faollik."""
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Ruxsat yo'q!", show_alert=True)
        return

    stats = db.get_total_stats()
    top = db.get_top_users(5)

    text = (
        f"📅 <b>Bugungi Faollik</b>\n"
        f"━━━━━━━━━━━━━━━\n\n"
        f"🆕 Yangi foydalanuvchilar: <b>{stats['today_new_users']}</b>\n"
        f"📝 Ishlangan quizlar: <b>{stats['today_quizzes']}</b>\n\n"
        f"🏆 <b>Top 5 (Jami coinlar):</b>\n"
    )

    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
    for i, user in enumerate(top[:5]):
        medal = medals[i] if i < len(medals) else f"{i+1}."
        text += f"{medal} {user['first_name']} — {user['coins']} 🪙\n"

    await callback.message.edit_text(# type: ignore
        text,
        reply_markup=admin_panel_keyboard(),
        parse_mode="HTML"
    )


@router.message(Command("broadcast"))
async def cmd_broadcast(message: Message):
    """
    /broadcast <xabar> — barcha foydalanuvchilarga xabar yuborish.
    Faqat admin uchun.
    """
    if not is_admin(message.from_user.id):# type: ignore
        await message.answer("❌ Siz admin emassiz!")
        return

    # /broadcast dan keyingi matnni olamiz
    text = message.text.removeprefix("/broadcast").strip()# type: ignore

    if not text:
        await message.answer(
            "⚠️ Xabar matni yo'q!\n"
            "Foydalanish: /broadcast Xabar matni bu yerga"
        )
        return

    users = db.get_all_users()
    sent = 0
    failed = 0

    await message.answer(f"📤 Xabar {len(users)} ta foydalanuvchiga yuborilmoqda...")

    for user in users:
        try:
            await message.bot.send_message(# type: ignore
                chat_id=user['user_id'],
                text=f"📢 <b>Bot Xabari:</b>\n\n{text}",
                parse_mode="HTML"
            )
            sent += 1
        except Exception:
            failed += 1  # Foydalanuvchi botni bloklagan bo'lishi mumkin

    await message.answer(
        f"✅ <b>Broadcast yakunlandi!</b>\n"
        f"✅ Yuborildi: {sent}\n"
        f"❌ Xato: {failed}",
        parse_mode="HTML"
    )
