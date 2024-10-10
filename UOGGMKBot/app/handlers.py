import os
from aiogram.types import InputFile, BufferedInputFile
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
from bs4 import BeautifulSoup
from io import BytesIO
# import sqlite3
import json
from . import keyb

router = Router()
instagramm_GGMK = 'https://www.instagram.com/ggmk.gomel?igsh=MXdwOThlZWlrYWFrZA=='
VK_GGMK = 'https://vk.com/ggmk_club'
Telegram_GGMK = 'https://t.me/ggmk_gomel'
youtube_GGMK = 'https://www.youtube.com/channel/UCtlbFZ3FVvNSj4sIp7cmywA'
# con = sqlite3.connect('Название бд')
# sqlite3.connect(database, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
# cursor = con.cursor()

user_state = {}

# Переменная для хранения состояния последнего запроса
last_state = {
    "last_date": None,
    "tomorrow_position": None  # 'left' или 'right'
}

# Обработка команды /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    # Отправляем приветственное сообщение и отображаем главную клавиатуру
    await message.reply(f'Социальные сети колледжа:!\n\nИнстаграмм: {instagramm_GGMK}\n\nВконакте: {VK_GGMK}\n\nТелеграмм:{Telegram_GGMK}\n\nЮтуб:{youtube_GGMK}',
                        reply_markup=keyb.main)

IMAGE_DIR = '/home/gamer/Загрузки/Telegram Desktop/UOGGMKBot (8)/UOGGMKBot/images'

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

    # Извлекаем ссылки на изображения
    img_urls = [item.find('img').get('src') for item in items]

    # Отправляем каждую картинку как файл (документ)
    for img_url in img_urls:
        img_data = session.get(img_url).content  # Получаем содержимое изображения
        img_io = BytesIO(img_data)  # Преобразуем в объект BytesIO
        img_io.name = 'image.png'  # Указываем имя файла

        # Используем BufferedInputFile для отправки байтов напрямую
        document = BufferedInputFile(file=img_io.getvalue(), filename="image.png")
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
    await message.answer("Выберите группу:", reply_markup=keyb.menu_raspisanie)

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


# Путь к изображению
IMAGE_DIR = '/home/gamer/Загрузки/Telegram Desktop/UOGGMKBot (8)/UOGGMKBot/images'


# Обработчик кнопки "Информация об оплате 💳"
@router.message(lambda message: message.text == 'Информация об оплате 💳')
async def handle_payment_info(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'payment_info'

    # Пути к изображениям
    image_files = ['oplata.jpg', 'pres.jpg']

    # Чтение и отправка изображений
    for image_file in image_files:
        image_path = os.path.join(IMAGE_DIR, image_file)

        # Чтение изображения из файла
        with open(image_path, 'rb') as file:
            img_data = file.read()  # Читаем содержимое изображения
            img_io = BytesIO(img_data)  # Преобразуем в объект BytesIO

            # Используем BufferedInputFile для отправки байтов напрямую
            document = BufferedInputFile(file=img_io.getvalue(), filename=image_file)
            await message.answer_document(document=document, caption="Информация об оплате")


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
        await message.answer("Возвращение в в меню учащимся:", reply_markup=keyb.uchashimsia)
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
    elif state in ['MP', 'PC','PM','ED','RP','TR','TM','TC']:
        # Возвращаем пользователя в меню абитуриентам
        user_state[user_id] = 'abiturientam'
        await message.answer("Возвращение в еню абитуриетам:", reply_markup=keyb.abiturientam)
    else:
        # По умолчанию возвращаем в главное меню
        user_state[user_id] = 'main_menu'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.main)


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
    with open('/home/gamer/Загрузки/Telegram Desktop/UOGGMKBot (8)/UOGGMKBot/app/spec.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Загружаем данные из JSON один раз, чтобы не загружать каждый раз при вызове
specialities_data = load_specialities()
# Универсальная функция для отображения информации о специальности
async def show_speciality_info(message: Message, speciality_code: str):
    data = specialities_data["specialities"].get(speciality_code)
    if data:
        await message.answer(
            f"<b>{data['title']}</b>\n"
            f"<b>Специальность:</b> {data['speciality']}\n\n"
            f"<b>Квалификация специалиста:</b> {data['qualification_specialist']}\n\n"
            f"<b>Квалификация рабочего:</b> {data.get('qualification_worker', 'Нет данных')}\n\n"
            f"<b>Продолжительность обучения:</b> {data['duration']}\n\n"
            f"<b>Форма обучения:</b> {data['study_form']}\n",
            reply_markup=keyb.special,
            parse_mode="html"
        )

# Обработчики для каждой специальности

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

# Обработка кнопки "МП"
# @router.message(F.text == 'МП')
# async def go_back(message: Message):
#     user_id = message.from_user.id
#     user_state[user_id] = 'abiturientam'
#     # Возвращаем пользователя в главное меню
#     await message.answer("Выберите интересующий раздел:", reply_markup=keyb.abiturientam)