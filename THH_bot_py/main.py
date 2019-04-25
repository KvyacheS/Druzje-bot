import logging
import datetime

from time import time


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def aboutGroup(update, context):
    update.message.reply_photo(photo=open("C:/Users/Alexander's PC/Desktop/GitHub/Druzje-bot/THH_bot_py", 'rb'))


def slu4ajnijFakt(update, context):
    update.message.reply_text('Сырник - токсичный хуй')


tjano4ki = ["ТЯНОЧКУ БЫ", "ТЯНОЧКУ ХОЧУ", "ХОЧУ ТЯНОЧКУ", "ЩАС БЫ ТЯНОЧКУ", "ТЯНОЧКУ ХОЧЕТСЯ", "ХОЧЕТСЯ ТЯНОЧКУ", "ТЯНОЧКУ ХОЧУ",
            "ТЯНУЧКУ БЫ", "ТЯНУЧКУ ХОЧУ", "ХОЧУ ТЯНУЧКУ", "ЩАС БЫ ТЯНУЧКУ", "ТЯНУЧКУ ХОЧЕТСЯ", "ХОЧЕТСЯ ТЯНУЧКУ", "ТЯНУЧКУ ХОЧУ",
            "ТЯН БЫ", "ТЯН ХОЧУ", "ТЯН ТЯНОЧКУ", "ЩАС БЫ ТЯН", "ТЯН ХОЧЕТСЯ", "ХОЧЕТСЯ ТЯН",  "ХОЧУ ТЯН",
            "ТЯНКУ БЫ", "ТЯНКУ ХОЧУ", "ХОЧУ ТЯНКУ", "ЩАС БЫ ТЯНКУ", "ТЯНКУ ХОЧЕТСЯ", "ХОЧЕТСЯ ТЯНКУ", "ХОЧУ ТЯНКУ"]


def tjan(update, context):
    update.message.reply_text('Отставить пиздастрадания, рядовой')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def noyou(update, context):
    update.message.reply_text('нет ты')


def unca(update, context):
    update.message.reply_text("не ной, блядь")


def newfag(update, context):
    if '@SMR_Konstantin_Sosnin' in update.message.new_chat_members.username:
        update.message.reply_text('ньюфаг, блядь')


def welcome(update, context):
    if update.message.new_chat_members.username.startswith('@KvyacheS'):
        update.message.reply_text('welcome')


class TjanFilter(BaseFilter):
    def filter(self, message):
        mes = message.text
        for t in tjano4ki:
            if t in mes.upper():
                return True
        return False


class NoYouFilter(BaseFilter):
    def filter(self, message):
        mes = message.text
        return 'НЕТ ТЫ' in mes.upper()


def main():
    print('Bot started')
    updater = Updater("842084881:AAElZKTtH0ZBFRtOvhsjQlGFv6aXPWdeBnY", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    tjan_filter = TjanFilter()
    no_you_filter = NoYouFilter()

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    dp.add_handler(CommandHandler("aboutGroup", aboutGroup, filters=Filters.chat(chat_id=-1001114719696)))
    dp.add_handler(MessageHandler(tjan_filter, tjan))
    dp.add_handler(MessageHandler(Filters.user(username='@Caendaley'), unca))
    # DruzjDruzishka Caendaley
    dp.add_handler(MessageHandler(no_you_filter, noyou))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling(clean=True)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

