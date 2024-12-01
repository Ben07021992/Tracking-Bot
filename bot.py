import os
from telegram.ext import Updater, CommandHandler

TELEGRAM_BOT_TOKEN = "7857522311:AAG11rMPc_w8YlVoP5UZN4aJPdkbbRGnT3E"  # Replace with your token

def start(update, context):
    update.message.reply_text('Hello! I am your bot.')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
