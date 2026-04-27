"""
shared_config.py — Bot va web sayt uchun umumiy sozlamalar
"""

BOT_TOKEN    = "8787543439:AAHg1NFEh1gciXZApCRB5BOF8K22QjrJMmU"
BOT_USERNAME = "test119991_bot"   # @ belgisisiz

ADMIN_IDS = [
    123456789,
    987654321,
]

WEB_SECRET_KEY = "o'zbekiston_maktab_2026"
SITE_URL = "https://pinokioai.onrender.com"  # Render URL
DB_NAME  = "uzbekistan_bot.db"
DAILY_COIN_REWARD = 1000

# ==========================================
# OBUNA REJALARI + IMTIYOZLAR
# ==========================================
# joker_daily   = kunlik bepul joker soni  (-1 = cheksiz)
# quiz_retry    = bir kunda bir joyni qayta ishlash limiti (-1 = cheksiz)
# bonus_coin    = har kuni bonus coin
# ==========================================
SUBSCRIPTION_PLANS = {
    "pro": {
        "id": "pro",
        "nomi": "Pro",
        "narx_coin": 1000,
        "rang": "#378ADD",
        "rang_light": "#E6F1FB",
        "rang_dark":  "#0C447C",
        "muddat_kun": 30,
        "emoji": "💙",
        "joker_daily":  20,
        "quiz_retry":    2,
        "bonus_coin":   50,
        "imtiyozlar": [
            "Har kuni 20 ta bepul 50/50 joker",
            "1 joyni kuniga 2 marta qayta ishlash",
            "Har kuni +50 bonus coin",
            "Pro 💙 nishon profilda",
        ],
    },
    "plus": {
        "id": "plus",
        "nomi": "Plus",
        "narx_coin": 1500,
        "rang": "#7F77DD",
        "rang_light": "#EEEDFE",
        "rang_dark":  "#3C3489",
        "muddat_kun": 30,
        "emoji": "💜",
        "joker_daily":  50,
        "quiz_retry":    5,
        "bonus_coin":  150,
        "imtiyozlar": [
            "Har kuni 50 ta bepul 50/50 joker",
            "1 joyni kuniga 5 marta qayta ishlash",
            "Har kuni +150 bonus coin",
            "Plus 💜 nishon profilda",
            "Maxsus ma'lumotlar paketi",
        ],
    },
    "ultra_plus": {
        "id": "ultra_plus",
        "nomi": "Ultra Plus",
        "narx_coin": 20000,
        "rang": "#BA7517",
        "rang_light": "#FAEEDA",
        "rang_dark":  "#633806",
        "muddat_kun": 30,
        "emoji": "👑",
        "joker_daily":  -1,   # cheksiz
        "quiz_retry":   -1,   # cheksiz
        "bonus_coin":  500,
        "imtiyozlar": [
            "Cheksiz 50/50 joker",
            "Joylarni cheksiz qayta ishlash",
            "Har kuni +500 bonus coin",
            "Ultra Plus 👑 oltin nishon",
            "Admin bilan to'g'ridan to'g'ri aloqa",
            "Maxsus sertifikat va diplomlar",
        ],
    },
}
