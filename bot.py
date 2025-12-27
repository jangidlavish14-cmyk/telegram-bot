import telebot
import os
from telebot.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)

# ===== CONFIG =====
TOKEN = "7816401651:AAF9xWvCVLHDtTKitP28EKCnO8QFjlDIicw"
CHANNEL_USERNAME = "@DAYS2GO"   # join check channel
ADMIN_ID = 7348698420            # <-- yahan apna Telegram ID daalo
USERS_FILE = "users.txt"

bot = telebot.TeleBot(TOKEN)

# ===== USERS SAVE / LOAD =====
def load_users():
    if not os.path.exists(USERS_FILE):
        return set()
    with open(USERS_FILE, "r") as f:
        return set(map(int, f.read().split()))

def save_user(user_id):
    users = load_users()
    if user_id not in users:
        with open(USERS_FILE, "a") as f:
            f.write(f"{user_id}\n")

def total_users():
    return len(load_users())

# ===== FORCE JOIN CHECK =====
def is_joined(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_USERNAME, user_id).status
        return status in ["member", "administrator", "creator"]
    except:
        return False

# ===== MAIN MENU =====
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("🎬 CAPCUT PRO"),
        KeyboardButton("🎥 SCREEN RECORDER PRO")
    )
    markup.add(
        KeyboardButton("📱 APP CLONER"),
        KeyboardButton("🎞 KINEMASTER PRO")
    )
    markup.add(
        KeyboardButton("🎨 FILMORA PRO"),
        KeyboardButton("🏆 FF TOURNAMENT APK")
    )
    return markup

# ===== START =====
@bot.message_handler(commands=['start'])
def start(message):
    save_user(message.from_user.id)

    if not is_joined(message.from_user.id):
        join_markup = InlineKeyboardMarkup()
        join_markup.add(
            InlineKeyboardButton("🔗 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME[1:]}"),
            InlineKeyboardButton("✅ Joined", callback_data="check_join")
        )
        bot.send_message(
            message.chat.id,
            "❌ *Access Denied*\n\n👉 Pehle channel join karo:",
            parse_mode="Markdown",
            reply_markup=join_markup
        )
        return

    bot.send_message(
        message.chat.id,
        f"🔥 *WELCOME TO DAYS2GO BOT* 🔥\n\n👥 Total Users: *{total_users()}*",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

# ===== JOIN CHECK BUTTON =====
@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join(call):
    if is_joined(call.from_user.id):
        bot.send_message(
            call.message.chat.id,
            "✅ *Access Granted*",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )
    else:
        bot.answer_callback_query(call.id, "❌ Abhi join nahi kiya")

# ===== DOWNLOAD FUNCTION =====
def send_download(chat_id, title, link):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("📥 Download APK", url=link),
        InlineKeyboardButton("🔙 Main Menu", callback_data="menu")
    )
    bot.send_message(
        chat_id,
        f"{title}",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "menu")
def back_menu(call):
    bot.send_message(
        call.message.chat.id,
        "🏠 *Main Menu*",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

# ===== APP HANDLERS =====
@bot.message_handler(func=lambda m: m.text == "🎬 CAPCUT PRO")
def capcut(m):
    send_download(m.chat.id, "📥 *CAPCUT PRO*", "https://t.me/days2go/53")

@bot.message_handler(func=lambda m: m.text == "🎥 SCREEN RECORDER PRO")
def screenrec(m):
    send_download(m.chat.id, "📥 *SCREEN RECORDER PRO*", "https://t.me/days2go/54")

@bot.message_handler(func=lambda m: m.text == "📱 APP CLONER")
def appcloner(m):
    send_download(m.chat.id, "📥 *APP CLONER*", "https://t.me/days2go/47")

@bot.message_handler(func=lambda m: m.text == "🎞 KINEMASTER PRO")
def kinemaster(m):
    send_download(m.chat.id, "📥 *KINEMASTER PRO*", "https://t.me/days2go/46")

@bot.message_handler(func=lambda m: m.text == "🎨 FILMORA PRO")
def filmora(m):
    send_download(m.chat.id, "📥 *FILMORA PRO*", "https://t.me/days2go/23")

@bot.message_handler(func=lambda m: m.text == "🏆 FF TOURNAMENT APK")
def fftour(m):
    send_download(m.chat.id, "🏆 *FF TOURNAMENT APK*", "https://t.me/days2go/59")

# ===== ADMIN PANEL =====
@bot.message_handler(commands=['admin'])
def admin(m):
    if m.from_user.id != ADMIN_ID:
        return
    bot.send_message(
        m.chat.id,
        "👑 *Admin Panel*\n\n/stats\n/broadcast <msg>",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['stats'])
def stats(m):
    if m.from_user.id == ADMIN_ID:
        bot.send_message(m.chat.id, f"👥 Total Users: {total_users()}")

@bot.message_handler(commands=['broadcast'])
def broadcast(m):
    if m.from_user.id != ADMIN_ID:
        return
    msg = m.text.replace("/broadcast", "").strip()
    for uid in load_users():
        try:
            bot.send_message(uid, msg)
        except:
            pass

bot.infinity_polling()