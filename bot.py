import random
from random import randint
from glob import glob
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from settings import TOKEN
from lists import full_list_of_the_excursions


async def start(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand'], ['/select'], ['/top']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,    # ожидание отправки сообщения
                                   text=f"Здравствуй, {format(update.message.chat.first_name)}! \n"
                                        "Вас приветствует Telegram-бот, который поможет с выбором интересных "
                                        "экскурсий в Москве \n"
                                        "Выберите команду для продолжения работы с ботом: \n"
                                        "/rand - случайная экскурсия \n"
                                        "/select - выбрать экскурсии по темам \n"
                                        "/top - вывести лучшие экскурсии по мнению опрошенных"
                                        "", reply_markup=my_keyboard)


async def rand(update, context):
    num = randint(1, len(full_list_of_the_excursions))
    list_of_photo = glob('img/*')
    for i in list_of_photo:
        if len(str(num)) == 1:
            if i[4] == str(num):
                picture = i
                break
        if len(str(num)) == 2:
            if i[4:6] == str(num):
                picture = i
                break
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(picture, 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{full_list_of_the_excursions[num - 1]}")


async def select(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/военно-исторические'], ['/исторические'], [''], ['/back']],
                                      resize_keyboard=True)
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
    back_handler = CommandHandler('back', back)  # обработка команды '/back'
    application.add_handler(start_handler)  # регистрируем обработчик в приложение
    application.add_handler(rand_handler)
    application.add_handler(select_handler)
    application.add_handler(top_handler)
    application.add_handler(back_handler)
    application.run_polling()   # запуск
