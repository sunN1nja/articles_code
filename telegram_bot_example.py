from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Привет! Я ваш Телеграмм бот.')

def main():
    # Замените 'YOUR_TOKEN' на токен, полученный от BotFather
    updater = Updater("YOUR_TOKEN", use_context=True)

    dp = updater.dispatcher

    # Добавляем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Начинаем поиск обновлений
    updater.start_polling()

    # Останавливаем бота при прерывании программы
    updater.idle()

if __name__ == '__main__':
    main()