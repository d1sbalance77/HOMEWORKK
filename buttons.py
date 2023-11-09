from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def menu():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)

    service_button = KeyboardButton('Заказать услугу')

    buttons.add(service_button)

    return buttons

def number_button():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    phone_send  = KeyboardButton('Поделится контактом', request_contact=True)

    buttons.add(phone_send)

    return buttons
