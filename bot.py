import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from xrpl.clients import JsonRpcClient
from xrpl.models import AccountInfo

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# XRP Ledger Client
xrp_client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

# Replace with your new Telegram Bot token
TELEGRAM_TOKEN = "7857522311:AAG11rMPc_w8YlVoP5UZN4aJPdkbbRGnT3E"  # Example token (should be kept private)

# Function to get the balance of XRP account
def get_xrp_balance(account: str):
    account_info = AccountInfo(account=account, ledger_index="validated")
    response = xrp_client.request(account_info)
    if "result" in response:
        xrp_balance = response["result"]["account_data"]["Balance"]
        return xrp_balance
    return None

# Command handler for /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the XRP Tending Token Tracker Bot!")

# Command handler to track balance
def track_balance(update: Update, context: CallbackContext) -> None:
    try:
        account = context.args[0]  # The user provides the XRP account as an argument
        balance = get_xrp_balance(account)
        if balance is not None:
            update.message.reply_text(f"The balance for account {account} is {balance} XRP.")
        else:
            update.message.reply_text(f"Could not retrieve balance for account {account}.")
    except IndexError:
        update.message.reply_te
