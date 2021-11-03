from telegram.ext import Updater
updater = Updater(token='2065572942:AAF5bgFxR4phDBQXvwFI9fcQ9-F7eQs6sJM')
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)



def admin_entry(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите данные. Сначала L, потом P")
from telegram.ext import CommandHandler
start_handler = CommandHandler('admin_enter_shop', start)
dispatcher.add_handler(start_handler)
updater.start_polling()



def unknown(update, context): #добавлять последним!
    context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, эта команда мне ещё неизвестна")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)