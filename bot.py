import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from settings import TOKEN


async def start(update, context):
    # ожидание отправки сообщения
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Здравствуй, {format(update.message.chat.first_name)}! \n"
                                        "Вас приветствует Telegram-бот, который поможет с выбором экскурсии. \n"
                                        "Выберите команду из списка, предложенного ниже:")


if __name__ == '__main__':
    TOKEN

    application = ApplicationBuilder().token(TOKEN).build()    # создание экземпляра бота через `ApplicationBuilder`
    start_handler = CommandHandler('start', start)  # обработка команды '/start'
    application.add_handler(start_handler)   # регистрируем обработчик в приложение
    application.run_polling()   # запуск
