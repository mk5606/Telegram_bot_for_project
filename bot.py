import random
from random import randint
from glob import glob
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from settings import TOKEN
from lists import full_list_of_the_excursions, list_science, list_literature, list_cosmos, list_history, list_military
from lists import list_new_year, list_production


async def start(update, context):  # update связан с отправкой сообщений, context - с контекстом обработанного сообщения
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
    my_keyboard = ReplyKeyboardMarkup([['/New_Year', '/cosmonautics'], ['/historical', '/military_historical'],
                                       ['/literature', '/production'], ['/scientific'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите тему экскурсии: \n"
                                        "/New_Year - новогодние экскурсии \n"
                                        "/cosmonautics - экскурсии о космосе \n"
                                        "/historical - исторические экскурсии \n"
                                        "/military_historical - военно-исторические экскурсии \n"
                                        "/literature - экскурсии о писателях и литературных произведениях \n"
                                        "/production - экскурсии на производства \n"
                                        "/scientific - экскурсии о науке \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


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


async def New_Year(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand_new_year'], ['/lists_new_year'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_new_year - случайная экскурсия по выбранной тематике \n"
                                        "/lists_new_year - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def rand_new_year(update, context):
    num_in_our_list = randint(1, len(list_new_year))
    list_of_photo = glob('img/*')
    num = 1
    for j in full_list_of_the_excursions:
        if j != list_new_year[num_in_our_list - 1]:
            num += 1
        else:
            break
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


async def lists_new_year(update, context):
    spisok = 'Список всех экскурсий по выбранной теме:\n'
    for i in list_new_year:
        i.split('\n')
        spisok += i[0] + '\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{spisok}')


async def cosmonautics(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand_cosmos'], ['/lists_cosmos'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_cosmos - случайная экскурсия по выбранной тематике \n"
                                        "/lists_cosmos - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def rand_cosmos(update, context):
    num_in_our_list = randint(1, len(list_cosmos))
    list_of_photo = glob('img/*')
    num = 1
    for j in full_list_of_the_excursions:
        if j != list_cosmos[num_in_our_list - 1]:
            num += 1
        else:
            break
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{full_list_of_the_excursions[num - 1]}")


async def historical(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand_history'], ['/lists_history'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_history - случайная экскурсия по выбранной тематике \n"
                                        "/lists_history - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def rand_history(update, context):
    num_in_our_list = randint(1, len(list_history))
    list_of_photo = glob('img/*')
    num = 1
    for j in full_list_of_the_excursions:
        if j != list_history[num_in_our_list - 1]:
            num += 1
        else:
            break
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{full_list_of_the_excursions[num - 1]}")


async def military_historical(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand_mil_history'], ['/lists_mil_history'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_mil_history - случайная экскурсия по выбранной тематике \n"
                                        "/lists_mil_history - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def rand_mil_history(update, context):
    num_in_our_list = randint(1, len(list_military))
    list_of_photo = glob('img/*')
    num = 1
    for j in full_list_of_the_excursions:
        if j != list_military[num_in_our_list - 1]:
            num += 1
        else:
            break
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{full_list_of_the_excursions[num - 1]}")


async def literature(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand_lit'], ['/lists_lit'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_lit - случайная экскурсия по выбранной тематике \n"
                                        "/lists_lit - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def rand_lit(update, context):
    num_in_our_list = randint(1, len(list_literature))
    list_of_photo = glob('img/*')
    num = 1
    for j in full_list_of_the_excursions:
        if j != list_literature[num_in_our_list - 1]:
            num += 1
        else:
            break
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{full_list_of_the_excursions[num - 1]}")


async def production(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand_prod'], ['/lists_prod'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_prod - случайная экскурсия по выбранной тематике \n"
                                        "/lists_prod - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def rand_prod(update, context):
    num_in_our_list = randint(1, len(list_production))
    list_of_photo = glob('img/*')
    num = 1
    for j in full_list_of_the_excursions:
        if j != list_production[num_in_our_list - 1]:
            num += 1
        else:
            break
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{full_list_of_the_excursions[num - 1]}")


async def scientific(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/rand_sc'], ['/lists_sc'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_sc - случайная экскурсия по выбранной тематике \n"
                                        "/lists_sc - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def rand_sc(update, context):
    num_in_our_list = randint(1, len(list_science))
    list_of_photo = glob('img/*')
    num = 1
    for j in full_list_of_the_excursions:
        if j != list_science[num_in_our_list - 1]:
            num += 1
        else:
            break
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{full_list_of_the_excursions[num - 1]}")


if __name__ == '__main__':
    TOKEN
    application = ApplicationBuilder().token(TOKEN).build()    # создание экземпляра бота через `ApplicationBuilder`
    start_handler = CommandHandler('start', start)  # обработка команды '/start'
    rand_handler = CommandHandler('rand', rand)   # обработка команды '/rand'
    select_handler = CommandHandler('select', select)   # обработка команды '/select'
    top_handler = CommandHandler('top', top)  # обработка команды '/top'
    back_handler = CommandHandler('back', back)  # обработка команды '/back'
    ny_handler = CommandHandler('New_Year', New_Year)   # обработка команды '/New_Year'
    cosmos_handler = CommandHandler('cosmonautics', cosmonautics)   # обработка команды 'cosmonautics'
    hys_handler = CommandHandler('historical', historical)  # обработка команды 'historical'
    mihy_handler = CommandHandler('military_historical', military_historical)  # обработка команды 'military_historical'
    lit_handler = CommandHandler('literature', literature)  # обработка команды 'literature'
    prod_handler = CommandHandler('production', production)  # обработка команды 'production'
    sc_handler = CommandHandler('scientific', scientific)  # обработка команды 'production'
    rny_handler = CommandHandler('rand_new_year', rand_new_year)  # обработка команды 'rand_new_year'
    rcos_handler = CommandHandler('rand_cosmos', rand_cosmos)  # обработка команды 'rand_cosmos'
    rhis_handler = CommandHandler('rand_history', rand_history)  # обработка команды 'rand_history'
    rmil_handler = CommandHandler('rand_mil_history', rand_mil_history)  # обработка команды 'rand_mil_history'
    rlit_handler = CommandHandler('rand_lit', rand_lit)  # обработка команды 'rand_lit'
    rprod_handler = CommandHandler('rand_prod', rand_prod)  # обработка команды 'rand_prod'
    rsc_handler = CommandHandler('rand_sc', rand_sc)  # обработка команды 'rand_sc'
    #lny_handler = CommandHandler('lists_new_year', lists_new_year)  # обработка команды 'lists_new_year'
    application.add_handler(start_handler)  # регистрируем обработчики в приложение
    application.add_handler(rand_handler)
    application.add_handler(select_handler)
    application.add_handler(top_handler)
    application.add_handler(back_handler)
    application.add_handler(ny_handler)
    application.add_handler(cosmos_handler)
    application.add_handler(hys_handler)
    application.add_handler(mihy_handler)
    application.add_handler(lit_handler)
    application.add_handler(prod_handler)
    application.add_handler(sc_handler)
    application.add_handler(rny_handler)
    application.add_handler(rcos_handler)
    application.add_handler(rhis_handler)
    application.add_handler(rmil_handler)
    application.add_handler(rlit_handler)
    application.add_handler(rprod_handler)
    application.add_handler(rsc_handler)
    #application.add_handler(lny_handler)
    application.run_polling()   # запуск
