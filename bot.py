import os
from telegram.ext import Updater, CommandHandler
import xrpl

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def get_trending_tokens():
    client = xrpl.clients.JsonRpcClient("https://s2.ripple.com:51234")
    try:
        issuing_account = "rEXAMPLE..."  # Replace with a valid XRP issuer address
        request = xrpl.models.requests.AccountCurrencies(account=issuing_account)
        response = client.request(request)
        tokens = response.result.get("receive_currencies", [])
        trending_tokens = tokens[:5]  # Get top 5 tokens
        return trending_tokens
    except Exception as e:
        return [f"Error: {str(e)}"]

def trending(update, context):
    tokens = get_trending_tokens()
    if tokens:
        message = "Trending Tokens on XRP:\n" + "\n".join(tokens)
    else:
        message = "No trending tokens found."
    update.message.reply_text(message)

def start(update, context):
    update.message.reply_text('Hello! I am your XRP Trending Bot.')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("trending", trending))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
