import logging
import random

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from settings import TOKEN, full_list_of_the_excursions


async def start(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,    # ожидание отправки сообщения
                                   text=f"Здравствуй, {format(update.message.chat.first_name)}! \n"
                                        "Вас приветствует Telegram-бот, который поможет с выбором экскурсии из списка "
                                        "музеев и выставочных залов, доступных для бесплатного посещения в рамках "
                                        "проекта мэра Москвы «МУЗЕИ - ДЕТЯМ». \n"
                                        "Выберите команду для продолжения работы с ботом: \n"
                                        "/rand - случайная экскурсия", reply_markup=my_keyboard)


async def rand(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{random.choice(full_list_of_the_excursions)}")


if __name__ == '__main__':
    TOKEN
    application = ApplicationBuilder().token(TOKEN).build()    # создание экземпляра бота через `ApplicationBuilder`
    start_handler = CommandHandler('start', start)  # обработка команды '/start'
    rand_handler = CommandHandler('rand', rand)   # обработка команды '/rand'
    application.add_handler(rand_handler)   # регистрируем обработчик в приложение
    application.add_handler(start_handler)
    application.run_polling()   # запуск
