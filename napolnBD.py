import sqlite3
import os

# Подключение к базе данных (создать новую или подключиться к существующей)
conn = sqlite3.connect('specialties.db')
cursor = conn.cursor()

# Создание таблицы для специальностей, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS specialties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT NOT NULL,
    qualification TEXT NOT NULL,
    worker_qualification TEXT,
    duration TEXT NOT NULL,
    education_form TEXT NOT NULL,
    description TEXT
)
''')

# Создание таблицы для колледжа, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS college (
    id INTEGER PRIMARY KEY,
    description TEXT
)
''')

# Данные о колледже
college_description = '''Гомельский государственный машиностроительный колледж,
основанный в 1955 году, за более чем 65 лет стал одним из ведущих учебных заведений региона. 
Колледж гордится своими традициями, профессиональным коллективом и выпускниками,
которые внесли значительный вклад в развитие машиностроительной отрасли Беларуси.

Сегодня образовательный процесс здесь осуществляют более 80 педагогов,
среди которых есть кандидаты наук, магистры и отличники образования.
Колледж предлагает современные и востребованные специальности, активно сотрудничает с
предприятиями региона и учреждениями высшего образования, внедряет инновационные образовательные
технологии и участвует в республиканских и международных проектах.

Колледж известен высоким уровнем подготовки специалистов, многолетними успехами в конкурсах и олимпиадах,
а также активной научной и социально-культурной деятельностью.
Выпускники учебного заведения успешно работают на предприятиях Беларуси и за её пределами,
продолжая укреплять добрую репутацию колледжа.'''

# Вставка данных о колледже
cursor.execute('''
INSERT OR IGNORE INTO college (id, description)
VALUES (1, ?)
''', (college_description,))

# Данные по специальностям
specialties = [
    ("Программирование мобильных устройств", "5-04-0611-01", "Техник-программист", "Оператор ЭВМ (5-й разряд)", "3 года 10 месяцев", "Дневная", "Описание специальности для ПМ."),
    ("Разработка и сопровождение ПО", "5-04-0612-02", "Техник-программист", "Оператор ЭВМ (5-й разряд)", "3 года 10 месяцев", "Дневная", "Описание специальности для РП."),
    ("Производство и переработка металлов", "5-04-0714-04", "Техник-технолог", "Заливщик, Плавильщик и др.", "3 года 7 месяцев", "Дневная", "Описание специальности для МП."),
    ("Предупреждение и ликвидация ЧС", "5-04-1033-01", "Техник", "Спасатель-пожарный (7 разряд)", "2 года 7 месяцев", "Дневная", "Описание специальности для ПС."),
    ("Технологическое обеспечение машиностроительного производства", "5-04-0714-01", "Техник", "Оператор станков с ПУ и др.", "3 года 7 месяцев", "Дневная", "Описание специальности для ТМ."),
    ("Техническое обслуживание техн. оборудования и робототехники", "5-04-0713-08", "Техник-электроник", "Оператор станков с ПУ и др.", "3 года 7 месяцев", "Дневная", "Описание специальности для ТР."),
    ("Планово-экономическая и аналитическая деятельность", "5-04-0311-01", "Техник-экономист", "", "3 года", "Дневная", "Описание специальности для ЭД."),
    ("Техническое обслуживание электронных систем транспортных средств", "5-04-0715-05", "Техник-электроник", "Слесарь-электрик и др.", "3 года 7 месяцев", "Дневная", "Описание специальности для ТС.")
]

# Вставка данных в таблицу специальностей
cursor.executemany('''
INSERT INTO specialties (name, code, qualification, worker_qualification, duration, education_form, description)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', specialties)

cursor.execute('''
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    image BLOB NOT NULL
)
''')

# Функция загрузки изображений
def load_image(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Данные изображений
images = []
image_filenames = ['oplata.jpg', 'pres.jpg', 'prakt.jpg']
image_names = ['oplata', 'pres', 'prakt']

# Загрузка изображений
for name, filename in zip(image_names, image_filenames):
    try:
        images.append((name, load_image(filename)))
    except FileNotFoundError as e:
        print(f"Ошибка: файл '{filename}' не найден. {e}")

# Вставка данных изображений в таблицу
if images:  # Проверка, есть ли изображения для вставки
    cursor.executemany('''
    INSERT INTO images (name, image)
    VALUES (?, ?)
    ''', images)
else:
    print("Нет изображений для вставки в базу данных.")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()