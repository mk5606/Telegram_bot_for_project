import random
from random import randint
from glob import glob
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from settings import TOKEN
from lists import full_list_of_the_excursions, list_science, list_literature, list_cosmos, list_history, list_military
from lists import list_new_year, list_production


sp_for_rand = random.sample(full_list_of_the_excursions, len(full_list_of_the_excursions))
theme = ''
count = 0
count1 = 0


async def start(update, context):  # update связан с отправкой сообщений, context - с контекстом обработанного сообщения
    my_keyboard = ReplyKeyboardMarkup([['/rand'], ['/select'], ['/top']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,    # ожидание отправки сообщения
                                   text=f"Здравствуй, {format(update.message.chat.first_name)}! \n"
                                        "Вас приветствует Telegram-бот, который поможет с выбором интересных "
                                        "и познавательных экскурсий в Москве (в том числе, связанных с учебными "
                                        "программами 5-7 классов). \n"
                                        "Выберите команду для продолжения работы с ботом: \n"
                                        "/rand - случайная экскурсия \n"
                                        "/select - выбрать экскурсии по темам \n"
                                        "/top - вывести лучшие экскурсии по мнению опрошенных"
                                        "", reply_markup=my_keyboard)


async def rand(update, context):
    global sp_for_rand, count1
    my_keyboard = ReplyKeyboardMarkup([['/back']], resize_keyboard=True)
    len_of_excursion = len(sp_for_rand)
    if count1 == len_of_excursion:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Вы ознакомились со всеми экскурсиями.")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Выберите команду для продолжения работы с ботом: \n"
                                            "/back - вернуться к выбору команд", reply_markup=my_keyboard)
    else:
        num = 1
        list_of_photo = glob('img/*')
        for j in full_list_of_the_excursions:
            if j != sp_for_rand[count1]:
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
        count1 += 1
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(picture, 'rb'))
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"{full_list_of_the_excursions[num - 1]}")


async def select(update, context):
    my_keyboard = ReplyKeyboardMarkup([['/New_Year', '/cosmonautics'],
                                       ['/literature', '/scientific', '/historical'],
                                       ['/military_historical', '/production'], ['/back']],
                                        resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите тему экскурсии: \n"
                                        "/New_Year - новогодние экскурсии \n"
                                        "/cosmonautics - экскурсии о космосе \n"
                                        "/literature - экскурсии о писателях и литературных произведениях \n"
                                        "/scientific - естественно-научные экскурсии \n"
                                        "/historical - исторические экскурсии \n"
                                        "/military_historical - военно-исторические экскурсии \n"
                                        "/production - экскурсии на производства \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def top(update, context):
    global theme, count
    theme = ''
    count = 0
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Топ по всем темам: \n"
                                        "1 \n"
                                        "2 \n"
                                        "3 \n"
                                        "4 \n"
                                        "5 \n")


async def back(update, context):
    global theme, count
    theme = ''
    count = 0
    my_keyboard = ReplyKeyboardMarkup([['/rand'], ['/select'], ['/top']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand - случайная экскурсия \n"
                                        "/select - выбрать экскурсии по темам \n"
                                        "/top - вывести лучшие экскурсии по мнению опрошенных"
                                        "", reply_markup=my_keyboard)


async def rand_theme(update, context):
    dict_rashifrovka = {'ny': list_new_year, 'cos': list_cosmos, 'hi': list_history, 'mi': list_military,
                        'li': list_literature, 'pr': list_production, 'sc': list_science}
    new_sp = dict_rashifrovka[theme]
    num_in_our_list = randint(1, len(new_sp))
    list_of_photo = glob('img/*')
    num = 1
    for j in full_list_of_the_excursions:
        if j != new_sp[num_in_our_list - 1]:
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


async def lists_theme(update, context):
    spisok = 'Список всех экскурсий по выбранной теме:\n'
    dict_rashifrovka = {'ny': list_new_year, 'cos': list_cosmos, 'hi': list_history, 'mi': list_military,
                        'li': list_literature, 'pr': list_production, 'sc': list_science}
    my_keyboard = ReplyKeyboardMarkup([['/next_excursion'], ['/rand_theme'], ['/back']], resize_keyboard=True)
    new_sp = dict_rashifrovka[theme]
    for i in new_sp:
        sp = i.split('\n')
        spisok += f'{new_sp.index(i) + 1}' + ') ' + sp[0] + '\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{spisok}")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/next_excursion - просмотр экскурсий из предложенного списка \n"
                                        "/rand_theme - случайная экскурсия по выбранной тематике \n"
                                        "", reply_markup=my_keyboard)


async def next_excursion(update, context):
    global count
    dict_rashifrovka = {'ny': list_new_year, 'cos': list_cosmos, 'hi': list_history, 'mi': list_military,
                        'li': list_literature, 'pr': list_production, 'sc': list_science}
    my_keyboard = ReplyKeyboardMarkup([['/back']], resize_keyboard=True)
    new_sp = dict_rashifrovka[theme]
    len_of_excursion = len(new_sp)
    if count == len_of_excursion:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Вы ознакомились со всеми экскурсиями по данной теме \n")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Выберите команду для продолжения работы с ботом: \n"
                                            "/back - вернуться к выбору команд", reply_markup=my_keyboard)
    else:
        num = 1
        list_of_photo = glob('img/*')
        for j in full_list_of_the_excursions:
            if j != new_sp[count]:
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
        count += 1
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(picture, 'rb'))
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"{full_list_of_the_excursions[num - 1]}")


async def New_Year(update, context):
    global theme, count
    theme = 'ny'
    count = 0
    my_keyboard = ReplyKeyboardMarkup([['/rand_theme'], ['/lists_theme'], ['/back']],
                                      resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_theme - случайная экскурсия по выбранной тематике \n"
                                        "/lists_theme - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def cosmonautics(update, context):
    global theme, count
    theme = 'cos'
    count = 0
    my_keyboard = ReplyKeyboardMarkup([['/rand_theme'], ['/lists_theme'], ['/back']],
                                      resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_theme - случайная экскурсия по выбранной тематике \n"
                                        "/lists_theme - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def historical(update, context):
    global theme, count
    theme = 'hi'
    count = 0
    my_keyboard = ReplyKeyboardMarkup([['/rand_theme'], ['/lists_theme'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_theme - случайная экскурсия по выбранной тематике \n"
                                        "/lists_theme - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def military_historical(update, context):
    global theme, count
    theme = 'mi'
    count = 0
    my_keyboard = ReplyKeyboardMarkup([['/rand_theme'], ['/lists_theme'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_theme - случайная экскурсия по выбранной тематике \n"
                                        "/lists_theme - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def literature(update, context):
    global theme, count
    theme = 'li'
    count = 0
    my_keyboard = ReplyKeyboardMarkup([['/rand_theme'], ['/lists_theme'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_theme - случайная экскурсия по выбранной тематике \n"
                                        "/lists_theme - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def production(update, context):
    global theme, count
    theme = 'pr'
    count = 0
    my_keyboard = ReplyKeyboardMarkup([['/rand_theme'], ['/lists_theme'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_theme - случайная экскурсия по выбранной тематике \n"
                                        "/lists_theme - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


async def scientific(update, context):
    global theme, count
    theme = 'sc'
    count = 0
    my_keyboard = ReplyKeyboardMarkup([['/rand_theme'], ['/lists_theme'], ['/back']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Выберите команду для продолжения работы с ботом: \n"
                                        "/rand_theme - случайная экскурсия по выбранной тематике \n"
                                        "/lists_theme - вывести список всех экскурсий по теме \n"
                                        "/back - вернуться к выбору команд", reply_markup=my_keyboard)


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
    rth_handler = CommandHandler('rand_theme', rand_theme)    # обработка команды 'rand_theme'
    lth_handler = CommandHandler('lists_theme', lists_theme)    # обработка команды 'lists_theme'
    next_handler = CommandHandler('next_excursion', next_excursion)     # обработка команды 'next_excursion'
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
    application.add_handler(rth_handler)
    application.add_handler(lth_handler)
    application.add_handler(next_handler)
    application.run_polling()   # запуск
