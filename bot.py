import logging
import random

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from settings import TOKEN, full_list_of_the_excursions


async def start(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand'], ['/select'], ['/top']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,    # ожидание отправки сообщения
                                   text=f"Здравствуй, {format(update.message.chat.first_name)}! \n"
                                        "Вас приветствует Telegram-бот, который поможет с выбором экскурсии из списка "
                                        "музеев и выставочных залов, доступных для бесплатного посещения в рамках "
                                        "проекта мэра Москвы «МУЗЕИ - ДЕТЯМ». \n"
                                        "Выберите команду для продолжения работы с ботом: \n"
                                        "/rand - случайная экскурсия \n"
                                        "/select - выбрать экскурсии по темам \n"
                                        "/top - вывести лучшие экскурсии по мнению опрошенных"
                                        "", reply_markup=my_keyboard)


async def rand(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{random.choice(full_list_of_the_excursions)}")


async def select(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/заглушка0'], ['/заглушка1'], ['/заглушка2'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите тему экскурсии: \n"
                                        "/заглушка0 \n"
                                        "/заглушка1 \n"
                                        "/заглушка2 \n"
                                        "/back - возврат на экран выбора команд", reply_markup=my_keyboard)


async def top(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Топ по всем темам: \n"
                                        "1 \n"
                                        "2 \n"
                                        "3 \n"
                                        "4 \n"
                                        "5 \n")


async def back(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand'], ['/select'], ['/top']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand - случайная экскурсия \n"
                                        "/select - выбрать экскурсии по темам \n"
                                        "/top - вывести лучшие экскурсии по мнению опрошенных"
                                        "", reply_markup=my_keyboard)


if __name__ == '__main__':
    TOKEN
    application = ApplicationBuilder().token(TOKEN).build()    # создание экземпляра бота через `ApplicationBuilder`
    start_handler = CommandHandler('start', start)  # обработка команды '/start'
    rand_handler = CommandHandler('rand', rand)   # обработка команды '/rand'
    select_handler = CommandHandler('select', select)   # обработка команды '/select'
    top_handler = CommandHandler('top', top)  # обработка команды '/top'
    back_handler = CommandHandler('back', back)  # обработка команды 'back'
    application.add_handler(start_handler)  # регистрируем обработчик в приложение
    application.add_handler(rand_handler)
    application.add_handler(select_handler)
    application.add_handler(top_handler)
    application.add_handler(back_handler)
    application.run_polling()   # запуск
