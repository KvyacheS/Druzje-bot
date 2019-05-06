import logging
import datetime
from random import randint

from time import time


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def aboutGroup(update, context):
    update.message.reply_photo(photo=open("C:/Users/Alexander's PC/Desktop/GitHub/Druzje-bot/THH_bot_py/vg_under.jpg", 'rb'))


def slu4ajnijFakt(update, context):
    update.message.reply_text('Сырник - токсичный хуй')


tjano4ki = ["ТЯНОЧКУ БЫ", "ТЯНОЧКУ ХОЧУ", "ХОЧУ ТЯНОЧКУ", "ЩАС БЫ ТЯНОЧКУ", "ТЯНОЧКУ ХОЧЕТСЯ", "ХОЧЕТСЯ ТЯНОЧКУ", "ТЯНОЧКУ ХОЧУ",
            "ТЯНУЧКУ БЫ", "ТЯНУЧКУ ХОЧУ", "ХОЧУ ТЯНУЧКУ", "ЩАС БЫ ТЯНУЧКУ", "ТЯНУЧКУ ХОЧЕТСЯ", "ХОЧЕТСЯ ТЯНУЧКУ", "ТЯНУЧКУ ХОЧУ",
            "ТЯН БЫ", "ТЯН ХОЧУ", "ТЯН ТЯНОЧКУ", "ЩАС БЫ ТЯН", "ТЯН ХОЧЕТСЯ", "ХОЧЕТСЯ ТЯН",  "ХОЧУ ТЯН",
            "ТЯНКУ БЫ", "ТЯНКУ ХОЧУ", "ХОЧУ ТЯНКУ", "ЩАС БЫ ТЯНКУ", "ТЯНКУ ХОЧЕТСЯ", "ХОЧЕТСЯ ТЯНКУ", "ХОЧУ ТЯНКУ"]


newfags = ['KvyacheS', 'solarechoes', 'eempee', 'huemrath', 'salv4tion', 'kartofelnyy_dzhem', 'KingPaimon', 'Podzhog_S',
           'giphochka', 'laAZYYZ', 'CUCKOLDINHO', 'Fractal_Tree', 'alex_owl', 'TEHEBOU', 'Frank671']


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
    update.message.reply_text('ньюфаг, блядь')


def poloznjak(update, context):
    update.message.reply_text('Дота - шахматы 21го века. Аниме для пидаразов. Пельмени надо жарить. '
                              'Тян не нужны. Дристани - говно для дибилов.')


def numbers_to_strings(argument):
    switcher = {
        0: "ПРИДУРОК ЛАГЕРНЫЙ",
        1: "СДОХНИ НАХ",
        2: "СЛЫШ ХУЕГОЛОВЫЙ",
        3: 'ДРОЧЕР НЕДОДЕЛАННЫЙ',
        4: 'КОЗЁЛ СМЕРДЯЩИЙ',
        5: 'ХУЙ С БУГРА',
        6: 'ПИЗДАДУЙ ХУЕВ',
        7: 'УДРУЧАЮЩИЙ ЗАСРАНЕЦ',
        8: 'ШКОЛЬНИЦА-НЕГОДНИЦА',
        9: 'СТАРШЕКЛАССНИЦА-БЕЗОБРАЗНИЦА',
        10: 'ПИЗДЁНЫШЬ-ДОЛБАЁБЫШЬ',
        11: 'ПИЗДА НЕСТРОЕВАЯ',
        12: 'ПИЗДОДУЙ ХУЕВ',
        13: 'ПРОБЛЯДЬ',
        14: 'СУЧАРА ГНИЛОСНАЯ',
        15: 'МАЛЕНЬКИЙ ОБОСРЫШЬ',
        16: 'ХУЕГОЛОВЫЙ',
        17: 'ПИЗДА С УШАМИ',
        18: 'ЧУДОВИЩЕ МАЛЕНЬКОЕ',
        19: 'ЦЕЛКА СМЕРДЯЩАЯ',
        20: 'ДРОЧИЛА ГНИЛОСТНЫЙ',
        21: 'СУКА ЁБАНАЯ',
        22: 'БОТАНИК ХУЕВ',
        23: 'УТЫРОК ЭДАКИЙ',
        24: 'ПИЗДОЧЁС',
        25: 'ОНАНИСТ ЁБАНЫЙ',
        26: 'МАЛЕНЬКИЙ ОБОСРЫШ',
        27: 'ОПИЗДОЛ',

    }
    return switcher.get(argument, "nothing")


def otbros(update, context):
    rand = randint(0, 27)
    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text('ТЫ ' + numbers_to_strings(rand))
    else:
        update.message.reply_text('плейстейшн мне купи, ' + numbers_to_strings(rand))


def welcome(update, context):
    last_new_user = update.message.new_chat_members[-1]
    for oldi in newfags:
        if last_new_user['username'] == oldi:
            update.message.reply_text('ньюфаг, блядь')


class TjanFilter(BaseFilter):
    def filter(self, message):
        if message.text:
            mes = message.text
            for t in tjano4ki:
                if t in mes.upper():
                    return True
            return False


class NoYouFilter(BaseFilter):
    def filter(self, message):
        if message.text:
            mes = message.text
            return 'НЕТ ТЫ' in mes.upper()


def main():
    print('Bot started')
    updater = Updater("884268402:AAHekHDw4T3Badp3LKmBSnsNQ9BUDiwf56M",use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    tjan_filter = TjanFilter()
    no_you_filter = NoYouFilter()

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    # & Filters.chat(chat_id=-1001114719696), welcome))
    dp.add_handler(CommandHandler("aboutGroup", aboutGroup, filters=Filters.chat(chat_id=-1001114719696)))
    dp.add_handler(MessageHandler(tjan_filter, tjan))
    dp.add_handler(MessageHandler(Filters.user(username='@Caendaley'), unca))
    # DruzjDruzishka Caendaley
    dp.add_handler(MessageHandler(no_you_filter, noyou))
    dp.add_handler(CommandHandler('poloznjak', poloznjak))
    dp.add_handler(CommandHandler('otbros', otbros))

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

