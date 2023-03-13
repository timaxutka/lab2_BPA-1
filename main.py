import telebot
import random
# Токен для доступа к API телеграм бота
TOKEN = '5814095646:AAFts8qT6ien7ts7yZ2e4shhPNMCOzyhpDY'
# Создаем экземпляр TeleBot по токену
bot = telebot.TeleBot(TOKEN)
# Список путей к картинкам
image_paths = [
    '1.jpg',
    '2.jpg',
    '3.png',
    '4.jpg'
]
# Создаем клавиатуру
keyboard = telebot.types.ReplyKeyboardMarkup()
# Добавляем кнопку на клавиатуру
keyboard.add(telebot.types.KeyboardButton('Картинка'))
# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я мотивирующий бот. Нажми на кнопку, чтобы получить случайную мотивационную картинку.", reply_markup=keyboard)
# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Нажми на кнопку, чтобы получить случайную мотивационную картинку.", reply_markup=keyboard)
# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def send_image(message):
    if message.text == 'Картинка':
        # Выбираем случайную картинку
        image_path = random.choice(image_paths)
        # Открываем файл с картинкой
        photo = open(image_path, 'rb')
        # Отправляем картинку пользователю
        bot.send_photo(message.chat.id, photo, reply_markup=keyboard)
    else:
        bot.reply_to(message, "Я не понимаю, что ты хочешь сказать. Нажми на кнопку, чтобы получить случайную мотивационную картинку.", reply_markup=keyboard)
# Запускаем бота
bot.polling()