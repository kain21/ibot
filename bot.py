# импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging  # включаем логгирование
import settings
# CommandHandler - добавляет команды боту

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log')


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(
        update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat: %s, Message: %s",
                 update.message.chat.username, update.message.chat.id, update.message.text)
    print(update.message)  # print(user_text) - бот отвечает тем же сообщением
    update.message.reply_text(user_text)


def main():  # функция, которая соединяется с платформой Телеграм
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add.handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()  # заходит в Телеграм, проверяет сообщения
    mybot.idle()  # будет работать до тех пор, пока не остановим


main()
