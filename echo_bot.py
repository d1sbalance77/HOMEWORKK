import telebot

import buttons

bot = telebot.TeleBot('6308789629:AAGXOZS0mmCbDXUQrJsguwFFgMtEl1-7S_U')


# commands=['start']
# @bot.message_handler(content_types=['text'])
# def send_welcome(message):
#     uid = message.from_user.id
#     if message.text == 'Википедия':
#         bot.send_message(uid, "Введите слово:", reply_markup=buttons.menu())
#     elif message.text == 'Переводчик':
#         bot.send_message(uid, "Введите слово для перевода:", reply_markup=buttons.menu())
@bot.message_handler(commands=['start'])
def start(message):
    global uid
    uid = message.from_user.id
    bot.send_message(uid, f'Добро пожаловать в наш бот!', reply_markup=buttons.menu())

@bot.message_handler(content_types=['text'])
def start_mybot(message):
    if message.text == 'Заказать услугу':
        bot.send_message(uid, 'Отправьте свое имя', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_name = message.text
    print(user_name)
    bot.send_message(uid, 'Отлично отправьте номер телефона', reply_markup=buttons.number_button())
    bot.register_next_step_handler(message, get_number, user_name)


def get_number(message, user_name):
    if message.contact and message.contact.phone_number:
        user_number = message.contact.phone_number
        bot.send_message(uid, 'Выберите услугу', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_service, user_name, user_number)
    else:
        bot.send_message(uid, 'Отправьте номер с помощью кнопки')
        bot.register_next_step_handler(message, get_number, user_name)


def get_service(message, user_name, user_number):
    user_service = message.text
    bot.send_message(uid, 'Какой срок?')
    bot.register_next_step_handler(message, get_deadline, user_name, user_number, user_service)

def get_deadline(message, user_name, user_number, user_service):
    user_deadline = message.text
    bot.send_message('-1002024951945', f'Новая заявка!\n\nИмя: {user_name}\n'
                                  f'Номер телефона: {user_number}\n'
                                  f'Услуга: {user_service}\n'
                                  f'Срок: {user_deadline}\n')

    bot.send_message(uid, 'Успешно принята ваша заявка!')


bot.infinity_polling()
