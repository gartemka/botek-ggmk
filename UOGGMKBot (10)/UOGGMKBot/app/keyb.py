from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Учащимся 👨🏼‍🎓')],
    [KeyboardButton(text='О колледже 🏨'), KeyboardButton(text='Абитуриентам ✒')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')

# [KeyboardButton(text='Расписание ⌛')]

uchashimsia = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расписание 🗓️')],
    [KeyboardButton(text='Для оплаты обучения 💳')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')

menu_raspisanie = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расписание по группам 🗂'), KeyboardButton(text='Расписание звонков 🔔')],
    [KeyboardButton(text='Общее расписание 🔔'), KeyboardButton(text='График практик 📄')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')

raspisanie_katalog = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='1 курс 😎'), KeyboardButton(text='2 курс 😠')],
    [KeyboardButton(text='3 курс 😡'), KeyboardButton(text='4 курс 😵')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)

pervi_kurs_katalog = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='РП-11'), KeyboardButton(text='РП-12')],
    [KeyboardButton(text='ПМ-11'), KeyboardButton(text='ТМ-11')],
    [KeyboardButton(text='ТМ-12'), KeyboardButton(text='ТР-11')],
    [KeyboardButton(text='ЭД-12'), KeyboardButton(text='МП-11')],
    [KeyboardButton(text='ТС-11')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)

vtoroy_kurs_katalog = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='РП-21'), KeyboardButton(text='РП-22')],
    [KeyboardButton(text='ПМ-21'), KeyboardButton(text='ТМ-21')],
    [KeyboardButton(text='ТМ-201'), KeyboardButton(text='ЭД-22')],
    [KeyboardButton(text='ТР-21'), KeyboardButton(text='ТР-201')],
    [KeyboardButton(text='МП-21'), KeyboardButton(text='ТС-21')],
    [KeyboardButton(text='ПС-201')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)

tretiy_kurs_katalog = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='ПК-31'), KeyboardButton(text='ПК-32')],
    [KeyboardButton(text='ПСк-31'), KeyboardButton(text='ТОМ-32')],
    [KeyboardButton(text='ЭК-32'), KeyboardButton(text='ЭТ-31')],
    [KeyboardButton(text='ТОС-31'), KeyboardButton(text='ТР-301')],
    [KeyboardButton(text='ПС-301')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)

chetvertiy_kurs_katalog = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='ПК-41'), KeyboardButton(text='ПК-42')],
    [KeyboardButton(text='ПСк-41'), KeyboardButton(text='ТОМ-42')],
    [KeyboardButton(text='ТОМ-401'), KeyboardButton(text='ТОС-41')],
    [KeyboardButton(text='ТОС-401'), KeyboardButton(text='Л-401')],
    [KeyboardButton(text='ЛЧС-401'), KeyboardButton(text='ЭТ-41')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дополнительные контакты:', url='http://uoggmk.by/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D1%8B/')]
])

colleg_katalog = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Контакты 📞'), KeyboardButton(text='Локация 🚩')],
    [KeyboardButton(text='Краткая информация 📖')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)

abiturientam = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Специальности 📋'), KeyboardButton(text='Приемная комиссия ☎')],
    [KeyboardButton(text='Общежитие 🏠'), KeyboardButton(text='Часто задаваемые вопросы ❓')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)

special = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='МП'), KeyboardButton(text='ПС')],
    [KeyboardButton(text='ПМ'), KeyboardButton(text='ЭД')],
    [KeyboardButton(text='РП'), KeyboardButton(text='ТР')],
    [KeyboardButton(text='ТМ'), KeyboardButton(text='ТС')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)

oplata_kartinki = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Реквизиты для оплаты'), KeyboardButton(text='Оплата задолженностей')],
    [KeyboardButton(text='Стоимость обучения'), KeyboardButton(text='Оплата общежития')],
    [KeyboardButton(text='Вернуться назад ↩')]
], resize_keyboard=True)