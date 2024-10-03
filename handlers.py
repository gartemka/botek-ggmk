import os
from aiogram.types import InputFile, BufferedInputFile
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
from bs4 import BeautifulSoup
from io import BytesIO
# import sqlite3

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


# Обработчик кнопки "График практик"
@router.message(lambda message: message.text == "График практик 📄")
# async def handle_schedule_practices(message: Message):
    # user_id = message.from_user.id
    # user_state[user_id] = 'grafic_practic'
    # file_id = "18J8Tet0WRH3rsZ5TrDmuqc-lzmnwjvaT"  # Укажите свой ID файла на Google Drive
    # try:
    #     # Получаем поток файла с Google Drive
    #     file_stream = get_file_from_google_drive(file_id)
    #
    #     # Отправляем изображение напрямую в чат
    #     await message.answer_photo(photo=InputFile(file_stream, filename='practice_schedule.jpg'))
    # except Exception as e:
    #     await message.answer(f"Ошибка при получении файла: {e}")

# Обработка команды /help
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
    await message.answer("Выберите группу:", reply_markup=keyb.uchashimsia)

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

@router.message(F.text == 'Информация об оплате 💳')
async def show_message(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'infoObopl'
# async def get_photo(message: Message):
#     await message.answer_photo(photo='https://drive.google.com/file/d/1rpGBOA1M7rzzMR5T9TzVufnal_exhMHK/view', caption= 'Информация об оплате обучения')

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
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.menu_raspisanie)
    elif state == 'obch_rasp':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'uchashimsia'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.uchashimsia)
    elif state == 'obch_rasp':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'infoObopl'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.main)
    elif state == 'grafic_practic':
        user_state[user_id] = 'uchashimsia'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.uchashimsia)
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
        await message.answer("Возвращение в меню Расписание по группам:", reply_markup=keyb.raspisanie_katalog)
    elif state == 'colleg_katalog':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'main_menu'
        await message.answer("Возвращение в главное меню:", reply_markup=keyb.main)
    elif state == 'abiturientam':
        # Возвращаем пользователя в главное меню
        user_state[user_id] = 'main_menu'
        await message.answer("Возвращение в меню абитуриентов:", reply_markup=keyb.main)
    elif state == 'special':
        # Возвращаем пользователя в меню абитуриентам
        user_state[user_id] = 'abiturientam'
        await message.answer("Возвращение в меню специальностей:", reply_markup=keyb.abiturientam)
    elif state in ['MP', 'PC','PM','ED','RP','TR','TM','TC']:
        # Возвращаем пользователя в меню абитуриентам
        user_state[user_id] = 'abiturientam'
        await message.answer("Возвращение в меню специальностей:", reply_markup=keyb.abiturientam)
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


# Обработка кнопки "МП в специальностях"
@router.message(F.text == 'МП')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'MP'
    # Возвращаем пользователя в главное меню
    await message.answer('<b>Производство и переработка металлов\n'
                         'Специальность:</b>\n '
                         '5-04-0714-04 «Производство и переработка металлов»\n\n'
                         '<b>Квалификация специалиста:</b>\n'
                         '«Техник-технолог»\n\n'
                         '<b>Квалификация рабочего:</b>\n'
                         'Заливщик металлов – 3-4 разряд\n'
                         'Плавильщик металлов и сплавов – 3-4 разряд\n'
                         'Контролер в литейном производстве – 3-4 разряд\n'
                         'Слесарь-ремонтник – 3-4 разряд\n'
                         'Формовщик машинной формовки – 3-4 разряд\n\n'
                         '<b>Продолжительность обучения:</b>\n'
                         'общего базового образования — 3 года 7  месяцев\n\n'
                         '<b>Форма обучения:</b>\n'
                         'Дневная (бюджетная)\n', reply_markup=keyb.special, parse_mode="html")

# Обработка кнопки "ПС в специальностях"
@router.message(F.text == 'ПС')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'PC'
    # Возвращаем пользователя в главное меню
    await message.answer('<b>Предупреждение и ликвидация чрезвычайных ситуаций\n</b>'
                         '<b>Специальность:</b>\n'
                         '5-04-1033-01 «Предупреждение и ликвидация чрезвычайных ситуаций»\n\n'
                         '<b>Квалификация специалиста:</b>\n'
                         '«Техник»\n\n'
                         '<b>Квалификация рабочего:</b>\n'
                         'Спасатель-пожарный – 7-разряд\n\n'
                         '<b>Продолжительность обучения:</b>\n'
                         'На основе общего среднего образования — 2 года 7 месяцев\n\n'
                         '<b>Форма обучения:</b>\n'
                         'Дневная (бюджетная и платная)\n',
                         reply_markup=keyb.special, parse_mode="html")

# Обработка кнопки "ПМ в специальностях"
@router.message(F.text == 'ПМ')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'PM'
    # Возвращаем пользователя в главное меню
    await message.answer('<b>Программирование мобильных устройств\n</b>'
                         '<b>Специальность:</b>\n'
                         '5-04-0611-01 «Программирование мобильных устройств»\n\n'
                         '<b>Квалификация:</b>\n'
                         'техник-программист\n\n'
                         '<b>Срок получения образования по специальности составляет:</b>\n'
                         'на основе общего базового образования – 3 года 10 месяцев\n\n'
                         '<b>Форма получения образования:</b>\n'
                         'дневная\n\n'
                         '<b>Квалификация рабочего:</b>\n'
                         'оператор электронных вычислительных машин (персональных электронно-вычислительных машин), 5-й разряд\n',
                         reply_markup=keyb.special, parse_mode="html")

# Обработка кнопки "ЭД в специальностях"
@router.message(F.text == 'ЭД')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'ED'
    # Возвращаем пользователя в главное меню
    await message.answer('<b>Планово-экономическая и аналитическая деятельность\n</b>'
                         '<b>Специальность:</b>\n'
                         '5-04-0311-01 «Планово-экономическая и аналитическая деятельность»\n\n'
                         '<b>Квалификация специалиста:</b>\n'
                         'Техник-экономист\n\n'
                         '<b>Продолжительность обучения:</b>\n'
                         'на основе общего базового образования — 3 года\n\n'
                         '<b>Форма обучения:</b>\n'
                         'Дневная (платная)\n',
                         reply_markup=keyb.special, parse_mode="html")

# Обработка кнопки "РП в специальностях"
@router.message(F.text == 'РП')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'RP'
    # Возвращаем пользователя в главное меню
    await message.answer('<b>Разработка и сопровождение программного обеспечения информационных систем\n</b>'
                         '<b>Специальность:</b>\n'
                         '5-04-0612-02 «Разработка и сопровождение программного обеспечения информационных систем»\n\n'
                         '<b>Квалификация:</b>\n'
                         'техник-программист\n\n'
                         '<b>Срок получения образования по специальности составляет:</b>\n'
                         'на основе общего базового образования – 3 года 10 месяцев\n\n'
                         '<b>Форма получения образования:</b>\n'
                         'дневная\n\n'
                         '<b>Квалификация рабочего:</b>\n'
                         'оператор электронных вычислительных машин (персональных электронно-вычислительных машин), 5-й разряд\n',
                         reply_markup=keyb.special, parse_mode="html")

# Обработка кнопки "ТР в специальностях"
@router.message(F.text == 'ТР')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'TR'
    # Возвращаем пользователя в главное меню
    await message.answer('<b>Техническое обслуживание технологического оборудования и средств робототехники в автоматизированном производстве\n</b>'
                         '<b>Специальность:</b>\n'
                         '5-04-0713-08  «Техническая эксплуатация технологического оборудования и средств робототехники в автоматизированном производстве»\n\n'
                         '<b>Квалификация специалиста:</b>\n'
                         'Техник-электроник\n\n'
                         '<b>Квалификации рабочего:</b>\n'
                         'Оператор станков с ПУ (3,4 разряда);\n'
                         'Слесарь-электромонтажник (2-3 разряд);\n'
                         'Слесарь контрольно-измерительных приборов и автоматики (3-4 разряд);\n'
                         'Наладчик технологического оборудования (3-4 разряд);\n'
                         'Наладчик контрольно-измерительных приборов и автоматики (4 разряд);\n'
                         'Оператор автоматических и полуавтоматических линий станков и установок (3-4 разряд);\n'
                         'Электромонтер по ремонту и обслуживанию электрооборудования (3-4 разряд).\n\n'
                         '<b>Продолжительность обучения:</b>\n'
                         '3 года 7 месяцев (на базе 9 классов)\n'
                         '2 года 7 месяцев (на базе 11 классов)\n\n'
                         '<b>Форма обучения:</b>\n'
                         'Дневная (бюджетная)\n', reply_markup=keyb.special, parse_mode="html")

# Обработка кнопки "ТМ в специальностях"
@router.message(F.text == 'ТМ')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'TM'
    # Возвращаем пользователя в главное меню
    await message.answer('<b>Технологическое обеспечение машиностроительного производства\n</b>'
                         '<b>Специальность:</b>\n'
                         '5-04-0714-01 Технологическое обеспечение машиностроительного производства\n\n'
                         '<b>Квалификация специалиста:</b>\n'
                         'Техник\n\n'
                         '<b>Квалификации рабочего:</b>\n'
                         'Оператор станков с программным управлением — 3-4 разряд\n'
                         'Токарь — 3-4 разряд\n'
                         'Фрезеровщик — 3-4 разряд\n'
                         'Контролер станочных и слесарных работ — 3-4 разряд\n'
                         'Контролер измерительных приборов и специального инструмента — 3-4 разряд\n\n'
                         '<b>Продолжительность обучения:</b>\n'
                         'на основе общего базового образования – 3 года 7 месяцев\n'
                         'на основе общего среднего (специального) образования (лица с ОПФР) – 2 года 7 месяцев\n\n'
                         '<b>Форма обучения:</b>\n'
                         'Дневная (бюджетная)\n',
                         reply_markup=keyb.special, parse_mode="html")

# Обработка кнопки "ТС в специальностях"
@router.message(F.text == 'ТС')
async def go_back(message: Message):
    user_id = message.from_user.id
    user_state[user_id] = 'TC'
    # Возвращаем пользователя в главное меню
    await message.answer('<b>Техническое обслуживание электронных систем транспортных средств\n</b>'
                         '<b>Специальность:</b>\n'
                         '5-04-0715-05 «Техническое обслуживание электронных систем транспортных средств»\n\n'
                         '<b>Квалификация:</b>\n'
                         'техник-электроник\n\n'
                         '<b>Наименование профессии рабочего:</b>\n'
                         'Слесарь-электрик по ремонту электрооборудования, 3-4 разряд;\n'
                         'Электромонтер по ремонту и обслуживанию электрооборудования, 3-4 разряд;\n'
                         'Слесарь по контрольно-измерительным приборам и автоматике, 3-4 разряд;\n'
                         'Слесарь по ремонту автомобилей, 3-4 разряд;\n'
                         'Наладчик контрольно-измерительных приборов и систем автоматики, 4 разряд.\n\n'
                         '<b>Срок получения образования по специальности составляет:</b>\n'
                         'на основе общего базового образования (9-ти классов) – 3 года 7 месяцев\n\n'
                         '<b>Форма получения образования:</b>\n'
                         'дневная (бюджет)\n',
                         reply_markup=keyb.special, parse_mode="html")


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