from telegram.ext import Updater
updater = Updater(token='2065572942:AAF5bgFxR4phDBQXvwFI9fcQ9-F7eQs6sJM')
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def starter(update,context):
    context.send_message(сhat_id=update.effective_chat.id, text="Для начала отправь мне /start")
starter
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Приветствую в магазине одноразовых электронных сигарет 'Одноразовый шоп'. Здесь можно узнать наличие (команда /stock ), оставить заявку на товар не из списка доступных (команда /ordernew ), а также узнать время работы сегодня (команда /worktime ). Приятных покупок! ")
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()




def admin_entry(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите данные. Сначала L, потом P")
from telegram.ext import CommandHandler
admin_handler = CommandHandler('admin_enter_shop', admin_entry)
dispatcher.add_handler(admin_handler)
updater.start_polling()
admin_login = 'Alibaba' ###
admin_password = 'Work' ###

from telegram.ext import MessageHandler, Filters
#def login(update, context):

#echo_handler = MessageHandler(Filters.text & (~Filters.command), login)
#dispatcher.add_handler(echo_handler)

def unknown(update, context): #добавлять последним!
    context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, эта команда мне ещё неизвестна")
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)