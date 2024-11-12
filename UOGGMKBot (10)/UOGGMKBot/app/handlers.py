import os
from PIL import Image
from aiogram.types import InputFile, BufferedInputFile, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from datetime import datetime, time
import fitz  # PyMuPDF
import json
from . import keyb
import hashlib
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram import types

router = Router()
instagramm_GGMK = 'https://www.instagram.com/ggmk.gomel?igsh=MXdwOThlZWlrYWFrZA=='
VK_GGMK = 'https://vk.com/ggmk_club'
Telegram_GGMK = 'https://t.me/ggmk_gomel'
youtube_GGMK = 'https://www.youtube.com/channel/UCtlbFZ3FVvNSj4sIp7cmywA'
COLLEGE_WEBSITE = "http://uoggmk.by/"

IMAGE_DIR = '../UOGGMKBot/app/images'
IMAGE_DIR_CHUNK = '../UOGGMKBot/app/images/raspisane/chunki'

user_state = {}


# Обработка команды /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    # Отправляем приветственное сообщение и отображаем главную клавиатуру
    await message.reply(f'Социальные сети колледжа:!\n\nИнстаграмм: {instagramm_GGMK}\n\nВконакте: {VK_GGMK}\n\nТелеграмм:{Telegram_GGMK}\n\nЮтуб:{youtube_GGMK}',
                        reply_markup=keyb.main)
    

# Путь к изображению
image_path = os.path.join(IMAGE_DIR, 'prakt.jpg')

# Обработчик кнопки "График практик"
@router.message(lambda message: message.text == "График практик 📄")
async def handle_schedule_practices(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'practice'

    # Чтение изображения из файла
    with open(image_path, 'rb') as image_file:
        img_data = image_file.read()  # Читаем содержимое изображения
        img_io = BytesIO(img_data)  # Преобразуем в объект BytesIO

        # Используем BufferedInputFile для отправки байтов напрямую
        document = BufferedInputFile(file=img_io.getvalue(), filename='prakt.jpg')
        await message.answer_document(document=document, caption="График практик 📄")

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

# Обработчики для каждой группы
@router.message(lambda message: message.text == 'РП-11')
async def handle_group_rp_11(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_0.png')
    await send_group_image(message, image_path, 'РП-11')

@router.message(lambda message: message.text == 'РП-12')
async def handle_group_rp_12(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_1.png')
    await send_group_image(message, image_path, 'РП-12')

@router.message(lambda message: message.text == 'ПМ-11')
async def handle_group_pm_11(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_2.png')
    await send_group_image(message, image_path, 'ПМ-11')

@router.message(lambda message: message.text == 'ТМ-11')
async def handle_group_tm_11(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_3.png')
    await send_group_image(message, image_path, 'ТМ-11')

@router.message(lambda message: message.text == 'ТМ-12')
async def handle_group_tm_12(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_4.png')
    await send_group_image(message, image_path, 'ТМ-12')

@router.message(lambda message: message.text == 'ТР-11')
async def handle_group_tr_11(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_5.png')
    await send_group_image(message, image_path, 'ТР-11')

@router.message(lambda message: message.text == 'ЭД-12')
async def handle_group_ed_12(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_6.png')
    await send_group_image(message, image_path, 'ЭД-12')

@router.message(lambda message: message.text == 'МП-11')
async def handle_group_mp_11(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_7.png')
    await send_group_image(message, image_path, 'МП-11')

@router.message(lambda message: message.text == 'ТС-11')
async def handle_group_ts_11(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_8.png')
    await send_group_image(message, image_path, 'ТС-11')

@router.message(lambda message: message.text == 'РП-21')
async def handle_group_rp_21(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_9.png')
    await send_group_image(message, image_path, 'РП-21')

@router.message(lambda message: message.text == 'РП-22')
async def handle_group_rp_22(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_10.png')
    await send_group_image(message, image_path, 'РП-22')

@router.message(lambda message: message.text == 'ПМ-21')
async def handle_group_pm_21(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_11.png')
    await send_group_image(message, image_path, 'ПМ-21')

@router.message(lambda message: message.text == 'ТМ-21')
async def handle_group_tm_21(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_12.png')
    await send_group_image(message, image_path, 'ТМ-21')

@router.message(lambda message: message.text == 'ТМ-201')
async def handle_group_tm_201(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_13.png')
    await send_group_image(message, image_path, 'ТМ-201')

@router.message(lambda message: message.text == 'ЭД-22')
async def handle_group_ed_22(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_14.png')
    await send_group_image(message, image_path, 'ЭД-22')

@router.message(lambda message: message.text == 'ТР-21')
async def handle_group_tr_21(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_15.png')
    await send_group_image(message, image_path, 'ТР-21')

@router.message(lambda message: message.text == 'ТР-201')
async def handle_group_tr_201(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_16.png')
    await send_group_image(message, image_path, 'ТР-201')

@router.message(lambda message: message.text == 'МП-21')
async def handle_group_mp_21(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_17.png')
    await send_group_image(message, image_path, 'МП-21')

@router.message(lambda message: message.text == 'ТС-21')
async def handle_group_ts_21(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_18.png')
    await send_group_image(message, image_path, 'ТС-21')

@router.message(lambda message: message.text == 'ПС-201')
async def handle_group_ps_201(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_19.png')
    await send_group_image(message, image_path, 'ПС-201')

@router.message(lambda message: message.text == 'ПК-31')
async def handle_group_pk_31(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_20.png')
    await send_group_image(message, image_path, 'ПК-31')

@router.message(lambda message: message.text == 'ПК-32')
async def handle_group_pk_32(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_21.png')
    await send_group_image(message, image_path, 'ПК-32')

@router.message(lambda message: message.text == 'ПСк-31')
async def handle_group_psk_31(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_22.png')
    await send_group_image(message, image_path, 'ПСк-31')

@router.message(lambda message: message.text == 'ТОМ-32')
async def handle_group_tom_32(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_23.png')
    await send_group_image(message, image_path, 'ТОМ-32')

@router.message(lambda message: message.text == 'ЭК-32')
async def handle_group_ek_32(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_24.png')
    await send_group_image(message, image_path, 'ЭК-32')

@router.message(lambda message: message.text == 'ЭТ-31')
async def handle_group_et_31(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_25.png')
    await send_group_image(message, image_path, 'ЭТ-31')

@router.message(lambda message: message.text == 'ТОС-31')
async def handle_group_tos_31(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_26.png')
    await send_group_image(message, image_path, 'ТОС-31')

@router.message(lambda message: message.text == 'ТР-301')
async def handle_group_tr_301(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_27.png')
    await send_group_image(message, image_path, 'ТР-301')

@router.message(lambda message: message.text == 'ПС-301')
async def handle_group_ps_301(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_28.png')
    await send_group_image(message, image_path, 'ПС-301')

@router.message(lambda message: message.text == 'ПК-41')
async def handle_group_pk_41(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_29.png')
    await send_group_image(message, image_path, 'ПК-41')

@router.message(lambda message: message.text == 'ПК-42')
async def handle_group_pk_42(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_30.png')
    await send_group_image(message, image_path, 'ПК-42')

@router.message(lambda message: message.text == 'ПСк-41')
async def handle_group_psk_41(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_31.png')
    await send_group_image(message, image_path, 'ПСк-41')

@router.message(lambda message: message.text == 'ТОМ-42')
async def handle_group_tom_42(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_32.png')
    await send_group_image(message, image_path, 'ТОМ-42')

@router.message(lambda message: message.text == 'ТОМ-401')
async def handle_group_tom_401(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_33.png')
    await send_group_image(message, image_path, 'ТОМ-401')

@router.message(lambda message: message.text == 'ТОС-41')
async def handle_group_tos_41(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_34.png')
    await send_group_image(message, image_path, 'ТОС-41')

@router.message(lambda message: message.text == 'ТОС-401')
async def handle_group_tos_401(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_35.png')
    await send_group_image(message, image_path, 'ТОС-401')

@router.message(lambda message: message.text == 'Л-401')
async def handle_group_l_401(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_36.png')
    await send_group_image(message, image_path, 'Л-401')

@router.message(lambda message: message.text == 'ЛЧС-401')
async def handle_group_lchs_401(message: Message):
    image_path = os.path.join(IMAGE_DIR_CHUNK, 'chunk_37.png')
    await send_group_image(message, image_path, 'ЛЧС-401')

# Общая функция для отправки изображения
async def send_group_image(message, image_path, group_name):
    with open(image_path, 'rb') as image_file:
        img_data = image_file.read()
        img_io = BytesIO(img_data)
        document = BufferedInputFile(file=img_io.getvalue(), filename=f'{group_name}.png')
        await message.answer_document(document=document, caption=f'Группа {group_name}')


# Переменная, которая отслеживает, какое расписание на "сегодня" и "завтра"
cyclic_switch = False  # False - первое фото на сегодня, True - второе фото на сегодня

# Функция, которая будет вызываться каждый день в 16:00
def toggle_schedule():
    global cyclic_switch
    cyclic_switch = not cyclic_switch  # Меняем состояние

# Настройка планировщика
scheduler = AsyncIOScheduler()
scheduler.add_job(toggle_schedule, CronTrigger(hour=17))  # Каждый день в 16:00
scheduler.start()
# Пример расписания звонков
schedule = [
    ("1", "8:30 — 9:15"),
    ("2", "9:25 — 10:10"),
    ("3", "10:20 — 11:05"),
    ("4", "11:15 — 12:00"),
    ("Обед", "12:00 — 12:30"),
    ("5", "12:30 — 13:15"),
    ("6", "13:25 — 14:10"),
    ("7", "14:20 — 15:05"),
    ("8", "15:15 — 16:00"),
    ("9", "16:10 — 16:55"),
    ("10", "17:05 — 17:50"),
    ("11", "18:00 — 18:45"),
    ("12", "18:55 — 19:40"),
]

@router.message(F.text == 'Расписание звонков 🔔')
async def show_bell_schedule(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'bell_schedule'

    # Создаем текст расписания
    schedule_text = "📅 <b>Расписание звонков</b> 📅\n\n"
    schedule_text += "<b>Понедельник — Суббота</b>\n\n"
    for lesson, time in schedule:
        schedule_text += f"🔹 <b>Урок {lesson}</b>: {time}\n"

    # Отправляем сообщение с расписанием
    await message.answer(schedule_text, parse_mode="HTML")

# Обработка кнопки "Общее расписание"
@router.message(F.text == 'Общее расписание 🔔')
async def show_catalog(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'obch_rasp'

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    })

    # Получаем страницу с расписанием
    response = session.get('http://uoggmk.by/%D1%80%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5/')

    # Разбираем HTML контент
    soup = BeautifulSoup(response.content, 'html.parser')

    # Находим все картинки
    items = soup.findAll('div', class_='elementor-image')
    img_urls = []
    for item in items:
        img_tag = item.find('img')
        img_url = img_tag.get('src')
        if img_tag.has_attr('data-src'):
            img_url = img_tag.get('data-src')
        elif img_tag.has_attr('srcset'):
            img_url = img_tag.get('srcset').split(',')[-1].split()[0]
        img_urls.append(img_url)

    save_dir = '../UOGGMKBot/app/images/raspisane/'

    # Удаляем старые изображения
    if os.path.exists(save_dir):
        for old_file in os.listdir(save_dir):
            old_file_path = os.path.join(save_dir, old_file)
            if os.path.isfile(old_file_path):
                os.remove(old_file_path)

    # Функция для вычисления хеша изображения
    def hash_image(image_bytes):
        hasher = hashlib.md5()
        hasher.update(image_bytes)
        return hasher.hexdigest()

    # Храним хеши изображений для сравнения
    image_hashes = []
    modification_times = []

    for idx, img_url in enumerate(img_urls):
        img_data = session.get(img_url).content
        img_io = BytesIO(img_data)

        # Сохраняем новое изображение на диск
        save_path = os.path.join(save_dir, f'image_{idx}.png')
        with open(save_path, 'wb') as f:
            f.write(img_data)

        # Получаем хеш изображения
        img_hash = hash_image(img_data)
        image_hashes.append((save_path, img_hash))

        # Устанавливаем новое время модификации (текущее время)
        current_time = datetime.now().timestamp()
        os.utime(save_path, (current_time, current_time))

        # Получаем время модификации
        modification_datetime = datetime.fromtimestamp(current_time)
        modification_times.append((save_path, modification_datetime))

    # Сортируем изображения по времени изменения
    modification_times.sort(key=lambda x: x[1])

    # Определяем текущий день недели (0 - понедельник, 5 - суббота, 6 - воскресенье)
    current_day = datetime.now().weekday()

    # Получаем текущее время
    current_time = datetime.now().time()

    # Проверка на понедельник
    if current_day == 0:
        # Если текущее время позже 17:00
        if current_time >= time(17, 0):
            file_name = 'raspisanie_na_zavtra.png'
            await message.answer("Расписание на завтра:")
        else:
            file_name = 'raspisanie_na_subbotu.png'
            await message.answer("Расписание на субботу:")

        with open(image_hashes[0][0], 'rb') as f:
            img_data = f.read()
        img_io = BytesIO(img_data)
        document = BufferedInputFile(file=img_io.getvalue(), filename=file_name)
        await message.answer_document(document=document)

        await message.answer("Расписание на сегодня:")
        with open(image_hashes[1][0], 'rb') as f:
            img_data = f.read()
        img_io = BytesIO(img_data)
        document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_ponedelnik.png")
        await message.answer_document(document=document)

    # Проверка на субботу
    elif current_day == 5:
        await message.answer("Расписание на субботу:")
        with open(image_hashes[0][0], 'rb') as f:
            img_data = f.read()
        img_io = BytesIO(img_data)
        document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_subbotu.png")
        await message.answer_document(document=document)

        await message.answer("Расписание на понедельник:")
        with open(image_hashes[1][0], 'rb') as f:
            img_data = f.read()
        img_io = BytesIO(img_data)
        document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_ponedelnik.png")
        await message.answer_document(document=document)

    # Проверка на пятницу
    elif current_day == 4:
        await message.answer("Расписание на субботу:")
        with open(image_hashes[0][0], 'rb') as f:
            img_data = f.read()
        img_io = BytesIO(img_data)
        document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_subbotu.png")
        await message.answer_document(document=document)

        await message.answer("Расписание на понедельник:")
        with open(image_hashes[1][0], 'rb') as f:
            img_data = f.read()
        img_io = BytesIO(img_data)
        document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_ponedelnik.png")
        await message.answer_document(document=document)

    else:
        # Определяем расписание на сегодня и завтра в зависимости от cyclic_switch
        if cyclic_switch:
            await message.answer("Расписание на сегодня:")
            with open(image_hashes[1][0], 'rb') as f:
                img_data = f.read()
            img_io = BytesIO(img_data)
            document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_segodnya.png")
            await message.answer_document(document=document)

            await message.answer("Расписание на завтра:")
            with open(image_hashes[0][0], 'rb') as f:
                img_data = f.read()
            img_io = BytesIO(img_data)
            document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_zavtra.png")
            await message.answer_document(document=document)
        else:
            await message.answer("Расписание на сегодня:")
            with open(image_hashes[0][0], 'rb') as f:
                img_data = f.read()
            img_io = BytesIO(img_data)
            document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_segodnya.png")
            await message.answer_document(document=document)

            await message.answer("Расписание на завтра:")
            with open(image_hashes[1][0], 'rb') as f:
                img_data = f.read()
            img_io = BytesIO(img_data)
            document = BufferedInputFile(file=img_io.getvalue(), filename="raspisanie_na_zavtra.png")
            await message.answer_document(document=document)

# Обработка кнопки "1 курс"
@router.message(F.text == '1 курс 😎')
async def show_catalog(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'kurs1'
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Выберите группу:", reply_markup=keyb.pervi_kurs_katalog)

# Обработка кнопки "Учащимся 👨🏼‍🎓"
@router.message(F.text == 'Учащимся 👨🏼‍🎓')
async def show_catalog(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'uchaschimsia'
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Выберите раздел:", reply_markup=keyb.uchashimsia)

# Обработка кнопки "Расписание"
@router.message(F.text == 'Расписание 🗓️')
async def show_catalog(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'menu_raspisanie'
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Выберите расписание:", reply_markup=keyb.menu_raspisanie)

# Обработка кнопки "Расписание по группам"
@router.message(F.text == 'Расписание по группам 🗂')
async def show_catalog(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'vibor_grupi'
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Выберите группу:", reply_markup=keyb.raspisanie_katalog)

# Обработка кнопки "2 курс"
@router.message(F.text == '2 курс 😠')
async def show_catalog(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'kurs2'
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Выберите группу:", reply_markup=keyb.vtoroy_kurs_katalog)

# Обработка кнопки "3 курс"
@router.message(F.text == '3 курс 😡')
async def show_catalog(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'kurs3'
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Выберите группу:", reply_markup=keyb.tretiy_kurs_katalog)

# Обработка кнопки "4 курс"
@router.message(F.text == '4 курс 😵')
async def show_catalog(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'kurs4'
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Выберите группу:", reply_markup=keyb.chetvertiy_kurs_katalog)

# Обработка кнопки "Краткая информация"
@router.message(F.text == 'Краткая информация 📖')
async def show_catalog(message: Message):
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Гомельский государственный машиностроительный колледж,\n"
                         "основанный в 1955 году, за более чем 65 лет стал одним из ведущих учебных заведений региона. \n"
                         "Колледж гордится своими традициями, профессиональным коллективом и выпускниками,\n"
                         "которые внесли значительный вклад в развитие машиностроительной отрасли Беларуси.\n"
                         "\nСегодня образовательный процесс здесь осуществляют более 80 педагогов,\n"
                         "среди которых есть кандидаты наук, магистры и отличники образования.\n"
                         "Колледж предлагает современные и востребованные специальности, активно сотрудничает с\n"
                         "предприятиями региона и учреждениями высшего образования, внедряет инновационные образовательные\n"
                         "технологии и участвует в республиканских и международных проектах.\n"
                         "\nКолледж известен высоким уровнем подготовки специалистов, многолетними успехами в конкурсах и олимпиадах,\n"
                         "а также активной научной и социально-культурной деятельностью.\n"
                         "Выпускники учебного заведения успешно работают на предприятиях Беларуси и за её пределами,\n"
                         "продолжая укреплять добрую репутацию колледжа.")

# Обработка кнопки "Контакты"
@router.message(F.text == 'Контакты 📞')
async def show_contacts(message: Message):
    # Отправляем сообщение с контактами и клавиатурой в одном сообщении
    await message.answer(
        "Контакты:\n\n"
        "Приёмная директора:\n"
        "8 (0232) 50-12-71;\n\n"
        "Приёмная комиссия:\n"
        "8 (0232) 50-12-73.",
        reply_markup=keyb.settings
    )


@router.message(F.text == 'Для оплаты обучения 💳')
async def handle_image_info(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'oplat_info'

    await message.answer("Выберите раздел:", reply_markup=keyb.oplata_kartinki)

# Обработка кнопки "Реквизиты для оплаты"
@router.message(F.text == 'Реквизиты для оплаты')
async def handle_image_info(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'image_info'

    # URL страницы с изображением
    page_url = 'https://drive.google.com/file/d/1rpGBOA1M7rzzMR5T9TzVufnal_exhMHK/view'

    # Получаем HTML-код страницы
    response = requests.get(page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим все изображения на странице
        img_tags = soup.find_all('img')

        # Если изображений нет, отправляем сообщение
        if not img_tags:
            await message.answer("Изображения не найдены на странице.")
            return

        # Получаем первое изображение
        img_url = img_tags[0]['src']
        if not img_url.startswith('http'):
            img_url = requests.compat.urljoin(page_url, img_url)  # Корректируем относительный URL

        # Загружаем изображение
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            image_data = BytesIO(img_response.content)

            # Отправляем изображение как документ
            document = BufferedInputFile(file=image_data.getvalue(), filename="image.jpg")  # Можно изменить на .png
            await message.answer_document(document=document, caption="Реквизиты для оплаты обучения")

# Обработка кнопки "Оплата задолженностей"
@router.message(F.text == 'Оплата задолженностей')
async def handle_image_info(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'image_info'

    # URL для прямого скачивания изображения
    img_url = 'https://drive.google.com/uc?export=download&id=1cFM2jJAx6bBMLqQQ8yf7WvgxHV6YVeJR'

    # Загружаем изображение
    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        image_data = BytesIO(img_response.content)

        # Отправляем изображение как документ
        document = BufferedInputFile(file=image_data.getvalue(), filename="image.jpg")
        await message.answer_document(document=document, caption="Реквизиты для оплаты задолжностей")
    else:
        await message.answer("Не удалось загрузить изображение.")

@router.message(F.text == 'Оплата общежития')
async def handle_image_info(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'image_info'

    # Исправленная ссылка для прямого скачивания изображения
    img_url = 'https://drive.google.com/uc?export=download&id=1A_7zCdlpyfwLP_WnnE1aV2WRNtIlAoEe'

    # Загружаем изображение
    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        image_data = BytesIO(img_response.content)

        # Отправляем изображение как документ
        document = BufferedInputFile(file=image_data.getvalue(), filename="image.jpg")
        await message.answer_document(document=document, caption="Реквизиты для оплаты задолженностей")
    else:
        await message.answer("Не удалось загрузить изображение.")


@router.message(F.text == 'Стоимость обучения')
async def handle_image_info(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'image_info'

    # Прямая ссылка на PDF-файл
    pdf_url = 'https://drive.google.com/uc?id=1JSkEIS8Qn2_5vQQ2yXEyhBpbRx5NaX1v&export=download'

    # Загружаем PDF-файл
    pdf_response = requests.get(pdf_url)
    if pdf_response.status_code == 200:
        pdf_data = pdf_response.content

        # Открываем PDF с помощью PyMuPDF
        pdf_document = fitz.open(stream=pdf_data, filetype="pdf")

        # Перебираем страницы и конвертируем их в изображения
        for i in range(len(pdf_document)):
            page = pdf_document.load_page(i)  # Загружаем страницу
            pix = page.get_pixmap()  # Конвертируем страницу в изображение
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # Сохраняем изображение во временный буфер
            image_data = BytesIO()
            img.save(image_data, format='JPEG')  # Сохраняем как JPEG
            image_data.seek(0)  # Возвращаем указатель в начало

            # Отправляем изображение в чат
            document = BufferedInputFile(file=image_data.getvalue(), filename=f"page_{i + 1}.jpg")
            await message.answer_document(document=document, caption=f"Страница {i + 1}")

    else:
        await message.answer("Не удалось загрузить PDF-файл.")

# Обработка кнопки "О колледже"
@router.message(F.text == 'О колледже 🏨')
async def show_message(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'colleg_katalog'
    # Отправляем сообщение и отображаем клавиатуру для каталога
    await message.answer("Выберите раздел:", reply_markup=keyb.colleg_katalog)

# Обработка кнопки "Геолокация"
@router.message(F.text == 'Локация 🚩')
async def send_location(message: Message):
    # Координаты колледжа
    latitude = 52.4057356  # Широта
    longitude = 30.907618  # Долгота
    # Отправляем сообщение с геолокацией
    await message.answer("Республика Беларусь, инд. 246027, г. Гомель, ул. Объездная, 2.")
    await message.answer_location(latitude=latitude, longitude=longitude)

# Обработка кнопки "Общежитие"
@router.message(F.text == 'Общежитие 🏠')
async def send_location(message: Message):
    # Координаты колледжа
    latitude = 52.407899  # Широта
    longitude = 30.904875  # Долгота
    # Отправляем сообщение с геолокацией
    await message.answer("Республика Беларусь, инд. 246027, г. Гомель, ул. Объездная, 4, корпус 2.")
    await message.answer_location(latitude=latitude, longitude=longitude)

# Обработка кнопки "Вернуться назад"
@router.message(F.text == 'Вернуться назад ↩')
async def go_back(message: Message):
    user_id = message.from_user.id
    state = user_state.get(user_id, 'main_menu')
    if state == 'vibor_grupi':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'menu_raspisanie'
        await message.answer("Возвращение в меню расписание:", reply_markup=keyb.menu_raspisanie)
    elif state == 'obch_rasp':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'uchashimsia'
        await message.answer("Возвращение в меню учащимся:", reply_markup=keyb.uchashimsia)
    elif state == 'practice':
        user_state[user_id] = 'uchashimsia'
        await message.answer("Возвращение в меню учащимся:", reply_markup=keyb.uchashimsia)
    elif state == 'menu_raspisanie':
        # Возвращаем пользователя в меню учащимся
        user_state[user_id] = 'uchashimsia'
        await message.answer("Возвращение в меню учащимся:", reply_markup=keyb.uchashimsia)
    elif state == 'uchashimsia':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'main_menu'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.main)
    elif state in ['kurs1', 'kurs2', 'kurs3', 'kurs4']:
        # Возвращаем пользователя в меню выбора курса в расписании
        user_state[user_id] = 'vibor_grupi'
        await message.answer("Возвращение в меню расписание по группам:", reply_markup=keyb.raspisanie_katalog)
    elif state == 'colleg_katalog':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'main_menu'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.main)
    elif state == 'abiturientam':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'main_menu'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.main)
    elif state == 'special':
        # Возвращаем пользователя в меню абитуриентам
        user_state[user_id] = 'abiturientam'
        await message.answer("Возвращение в меню абитуриетам:", reply_markup=keyb.abiturientam)
    elif state == 'oplat_info':
        # Возвращаем пользователя в меню абитуриентам
        user_state[user_id] = 'abiturientam'
        await message.answer("Возвращение в меню учащимся:", reply_markup=keyb.uchashimsia)
    elif state == 'image_info':
        # Возвращаем пользователя в меню абитуриентам
        user_state[user_id] = 'abiturientam'
        await message.answer("Возвращение в меню учащимся:", reply_markup=keyb.uchashimsia)
    elif state in ['MP', 'PC','PM','ED','RP','TR','TM','TC']:
        # Возвращаем пользователя в меню абитуриентам
        user_state[user_id] = 'abiturientam'
        await message.answer("Возвращение в меню абитуриетам:", reply_markup=keyb.abiturientam)
    else:
        # По умолчанию возвращаем в главное меню
        user_state[user_id] = 'main_menu'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.main)

# Функция для загрузки вопросов и ответов с кэшированием
def load_faq():
    if not hasattr(load_faq, 'cache'):
        # Загружаем данные из файла только один раз
        with open('../UOGGMKBot/app/faq_data.json', 'r', encoding='utf-8') as file:
            load_faq.cache = json.load(file)
    return load_faq.cache

# Функция для загрузки вопросов и ответов с кэшированием
def load_faq():
    if not hasattr(load_faq, 'cache'):
        # Загружаем данные из файла только один раз
        with open('../UOGGMKBot/app/faq_data.json', 'r', encoding='utf-8') as file:
            load_faq.cache = json.load(file)
    return load_faq.cache

# Использование функции для загрузки данных
faq_data = load_faq()

@router.message(F.text == 'Часто задаваемые вопросы ❓')
async def send_faq(message: types.Message):
    await show_faq(message, 0)

async def show_faq(message: types.Message, question_index: int):
    print(f"Current question index: {question_index}")  # Логирование индекса

    try:
        # Проверяем корректность индекса
        question = faq_data[question_index]["question"]
        answer = faq_data[question_index]["answer"]

        faq_text = f"<b>{question}</b>\n<i>{answer}</i>"

        # Формируем кнопки вперед и назад
        buttons = [
            [types.InlineKeyboardButton(text='⬅️ Назад', callback_data=f'previous_{question_index}')],
            [types.InlineKeyboardButton(text='Вперед ➡️', callback_data=f'next_{question_index}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

        await message.answer(faq_text, parse_mode="html", reply_markup=keyboard)

    except IndexError:
        print(f"IndexError: The question index {question_index} is out of range.")
        await message.answer("Ошибка: индекс вопроса вышел за пределы допустимого диапазона.")
    except Exception as e:
        print(f"Error occurred: {e}")
        await message.answer("Произошла ошибка при обработке запроса.")

# Обработка нажатий на кнопки
@router.callback_query(lambda c: c.data.startswith('previous') or c.data.startswith('next'))
async def navigate_faq(callback_query: types.CallbackQuery):
    # Извлекаем текущее значение вопроса из callback_data
    action, question_index = callback_query.data.split('_')
    question_index = int(question_index)

    # Определяем направление навигации
    if action == 'next':
        question_index = (question_index + 1) % len(faq_data)  # Следующий вопрос
    elif action == 'previous':
        question_index = (question_index - 1) % len(faq_data)  # Предыдущий вопрос

    # Удаление предыдущего сообщения и отправка нового
    await callback_query.message.delete()
    await show_faq(callback_query.message, question_index)

# Обработка кнопки "Абитурьенту"
@router.message(F.text == 'Абитуриентам ✒')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'abiturientam'
    # Возвращаем пользователя в главное меню
    await message.answer("Выберите интересующий раздел:", reply_markup=keyb.abiturientam)

# Обработка кнопки "Специальности"
@router.message(F.text == 'Специальности 📋')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'special'
    # Возвращаем пользователя в главное меню
    await message.answer("<b>Отделение информационных технологий:</b>'\n"
                         "5-04-0611-01 «Программирование мобильных устройств» - «ПМ»\n"
                         "5-04-0612-02 «Разработка и сопровождение программного обеспечения информационных систем» - «РП»\n\n"
                         "<b>Электронико-техническое отделение</b>\n"
                         "5-04-0713-08 «Техническая эксплуатация технологического оборудования и средств робототехники в автоматизированном производств» - «ТР»\n"
                         "5-04-0715-05 «Техническое обслуживание электронных систем транспортных средств» -«ТС»\n\n"
                         "<b>Технико-экономическое отделение</b>\n"
                         "5-04-0714-01 «Технологическое обеспечение машиностроительного производства» - «ТМ»\n"
                         "5-04-0311-01 «Планово-экономическая и аналитическая деятельность» - «ЭД»\n\n"
                         "<b>Технологическое отделение</b>\n"
                         "5-04-0714-04 «Производство и переработка металлов» - «МП»\n"
                         "5-04-1033-01 «Предупреждение и ликвидация чрезвычайных ситуаций» - «ПС»"
                         "\n\n\n<b>Выберите интересующий раздел:</b>", reply_markup=keyb.special, parse_mode="html")


# Функция для загрузки данных из JSON файла
def load_specialities():
    with open('../UOGGMKBot/app/spec.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Загружаем данные из JSON один раз, чтобы не загружать каждый раз при вызове
specialities_data = load_specialities()

# Универсальная функция для отображения информации о специальности
async def show_speciality_info(message: Message, speciality_code: str):
    data = specialities_data["specialities"].get(speciality_code)

    if data:
        # Формируем текст с информацией о специальности
        text = (
            f"<b>{data['title']}</b>\n\n"
            f"<b>Специальность:</b> {data['speciality']}\n\n"
            f"<b>Квалификация специалиста:</b> {data['qualification_specialist']}\n\n"
            f"<b>Квалификация рабочего:</b> {data.get('qualification_worker', 'Нет данных')}\n\n"
            f"<b>Продолжительность обучения:</b> {data['duration']}\n\n"
            f"<b>Форма обучения:</b> {data['study_form']}\n\n"
            f"<b>Видео:</b> {data['ssilka']}\n"
        )

        # Отправляем текст с информацией
        await message.answer(
            text,
            reply_markup=keyb.special,
            parse_mode="html"
        )

# Обработка кнопки "МП"
@router.message(F.text == 'МП')
async def go_mp(message: Message):
    await show_speciality_info(message, "MP")

# Обработка кнопки "ПС"
@router.message(F.text == 'ПС')
async def go_ps(message: Message):
    await show_speciality_info(message, "PS")

# Обработка кнопки "ПМ"
@router.message(F.text == 'ПМ')
async def go_pm(message: Message):
    await show_speciality_info(message, "PM")

# Обработка кнопки "ЭД"
@router.message(F.text == 'ЭД')
async def go_ed(message: Message):
    await show_speciality_info(message, "ED")

# Обработка кнопки "РП"
@router.message(F.text == 'РП')
async def go_rp(message: Message):
    await show_speciality_info(message, "RP")

# Обработка кнопки "ТР"
@router.message(F.text == 'ТР')
async def go_tr(message: Message):
    await show_speciality_info(message, "TR")

# Обработка кнопки "ТМ"
@router.message(F.text == 'ТМ')
async def go_tm(message: Message):
    await show_speciality_info(message, "TM")

# Обработка кнопки "ТС"
@router.message(F.text == 'ТС')
async def go_tc(message: Message):
    await show_speciality_info(message, "TC")


# Обработка текста "Как дела?"
@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')

# Обработка фото
@router.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

# Обработка команды /get_photo
@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://telegram.org/img/t_logo.png',  # Пример фото
                               caption='Это лого ТГ')

# Обработка кнопки "Приемная комиссия"
@router.message(F.text == 'Приемная комиссия ☎')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'priemnaya'
    # Возвращаем пользователя в главное меню
    await message.answer("<b>Гомельский государственный машиностроительный колледж расположен по адресу: г. Гомель, ул. Объездная, 2.\n"
                     "Работаем с понедельника по субботу с 9:00 до 18:00. Телефон для справок: 50-12-73.</b>\n"
                     "\n<b>Абитуриенты подают в приемную комиссию следующие документы:</b>\n"
                     "1. Заявление на имя руководителя колледжа по установленной форме.\n"
                     "2. Оригиналы документа об образовании и приложения к нему.\n"
                     "3. Медицинскую справку по форме, установленной Министерством здравоохранения.\n"
                     "4. Документы, подтверждающие право абитуриента на льготы при приеме на обучение.\n"
                     "5. Шесть фотографий размером 3х4 см.\n"
                     "\n<b>При необходимости дополнительно представляются:</b>\n"
                     "1. Заключение врачебно-консультационной или медико-реабилитационной экспертной комиссии об отсутствии противопоказаний для обучения по выбранной специальности (для лиц, закончивших учреждения, обеспечивающие получение специального образования, детей-инвалидов до 18 лет, инвалидов I, II и III группы).\n"
                     "2. Заключение государственного центра коррекционно-развивающего обучения и реабилитации по рекомендации обучения в учреждениях, обеспечивающих получение специального образования (для лиц с нарушениями зрения, слуха, функций опорно-двигательного аппарата).\n"
                     "3. Паспорт или заменяющий его документ предъявляется абитуриентом отдельно.\n"
                     "\nАбитуриенты, поступающие на все специальности на основе общего базового образования и общего среднего образования, на дневную форму получения образования, зачисляются по конкурсу среднего балла документа об образовании.\n"
                     "\n<b>Иногородним учащимся предоставляется общежитие.</b>", reply_markup=keyb.abiturientam, parse_mode="html")
