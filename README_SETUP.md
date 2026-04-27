# O'zbekiston Ta'lim — Bot + Sayt O'rnatish

## Fayl tuzilmasi
```
uzbekistan_project/
├── shared_config.py     ← BIRINCHI shu faylni to'ldiring
├── bot/                 ← Telegram bot
│   ├── bot.py           ← Bot ishga tushirish
│   └── handlers/
│       └── subscription.py  ← Yangi (obuna ko'rish)
└── web/                 ← Web sayt
    ├── app.py           ← Sayt ishga tushirish
    └── ...
```

---

## 1-qadam: shared_config.py ni to'ldirish

```python
BOT_TOKEN    = "123456:ABC..."       # @BotFather tokeningiz
BOT_USERNAME = "uzbekistan_edu_bot"  # @ siz
ADMIN_IDS    = [123456789]           # Sizning Telegram ID ingiz
SITE_URL     = "http://127.0.0.1:5000"  # Localhost uchun
```

---

## 2-qadam: Kutubxonalarni o'rnatish

```bash
# Bot uchun
pip install aiogram==3.7.0

# Sayt uchun
pip install flask
```

---

## 3-qadam: Ishga tushirish (2 ta terminal)

**Terminal 1 — Bot:**
```bash
cd uzbekistan_project/bot
python bot.py
```

**Terminal 2 — Sayt:**
```bash
cd uzbekistan_project/web
python app.py
```

---

## 4-qadam: Telegram Login sozlash

BotFather ga borib:
```
/setdomain → @sizning_botingiz → 127.0.0.1
```
(Production uchun real domenni kiriting)

---

## Qanday ishlaydi?

1. Foydalanuvchi botda `/start` — coin yig'adi
2. Bot menyusida **👑 Obuna** tugmasini bosadi
3. Sayt havolasiga o'tadi: `http://127.0.0.1:5000`
4. **"Telegram bilan kirish"** tugmasini bosadi
5. Obuna reja tanlaydi — coinlar avtomatik ayiriladi
6. Botda **👑 Obuna** → **🔄 Yangilash** — faol obunasi ko'rinadi

---

## Obuna narxlari

| Reja | Narx | Muddat |
|------|------|--------|
| 💙 Pro | 1,000 coin | 30 kun |
| 💜 Plus | 1,500 coin | 30 kun |
| 👑 Ultra Plus | 20,000 coin | 30 kun |

---

## VPS ga o'rnatish (ixtiyoriy)

1. `SITE_URL` ni real domenge o'zgartiring
2. Nginx + Gunicorn o'rnating
3. BotFather da domenni ro'yxatdan o'tkazing
4. SSL sertifikat oling (Let's Encrypt)
