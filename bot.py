import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7816401651:AAF9xWvCVLHDtTKitP28EKCnO8QFjlDIicw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("CAPCUT PRO"),
        KeyboardButton("SCREEN RECORDER PRO"),
        KeyboardButton("APP CLONER")
        KeyboardButton("KINEMASTER PRO")
        KeyboardButton("FILMORA PRO")
        KeyboardButton("FF TOURNAMENT APK")
    )

    bot.send_message(
        message.chat.id,
        "🔥 *WELCOME TO DAYS2GO BOT* 🔥\n\nSelect an option 👇",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.message_handler(func=lambda m: m.text == "CAPCUT PRO")
def np_manager(message):
    bot.send_message(
        message.chat.id,
        "📥 *Download CAPCUT PRO*\n\n👉 https://t.me/days2go/53",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda m: m.text == "FILMORA PRO")
def sketchware(message):
    bot.send_message(
        message.chat.id,
        "📥 *Download FILMORA PRO*\n\n👉 https://t.me/days2go/23",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda m: m.text == "APP CLONER")
def dev_tools(message):
    bot.send_message(
        message.chat.id,
        "📥 *Download APP CLONER*\n\n👉 https://t.me/days2go/47",
        parse_mode="Markdown"
    )
    
@bot.message_handler(func=lambda m: m.text == "FF TOURNAMENT APK")
def dev_tools(message):
    bot.send_message(
        message.chat.id,
        "📥 *Download FF TOURNAMENT and Get Winning Prize 🏆*\n\n👉 https://t.me/days2go/59",
        parse_mode="Markdown"
    )
   
@bot.message_handler(func=lambda m: m.text == "SCREEN RECORDER PRO")
def dev_tools(message):
    bot.send_message(
        message.chat.id,
        "📥 *Download SCREEN RECORDER PRO*\n\n👉 https://t.me/days2go/54",
        parse_mode="Markdown"
    )
    
@bot.message_handler(func=lambda m: m.text == "KINEMASTER PRO")
def dev_tools(message):
    bot.send_message(
        message.chat.id,
        "📥 *Download KINEMASTER PRO*\n\n👉 https://t.me/days2go/46",
        parse_mode="Markdown"
    )
    

bot.infinity_polling()