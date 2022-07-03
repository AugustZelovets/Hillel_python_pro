import random
import sqlite3
import re
import requests
from pandas.core.common import flatten

# створить базу даних (довільне ім'я)
with sqlite3.connect('people.sqlite') as db_connection:
    cursor = db_connection.cursor()
    cursor.execute('''
            DROP TABLE IF EXISTS gender;
        ''')
    cursor.execute('''
            DROP TABLE IF EXISTS people;
        ''')
    cursor.execute('''
            DROP TABLE IF EXISTS profession;
        ''')
# Створить таблицю з професіями (записати рандомні значення)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS profession(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL
        )""")
    cursor.execute(
        """
        INSERT INTO profession(name)
        VALUES ('therapeutist'), ('driver'), ('baker'), ('hairdresser'), ('mason'), ('postman'), ('lawyer'), ('producer')
        """)
# Створить таблицю з гендерами (має бути як мінімум два гендери, інші на ваш вибір)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS gender(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL
        )""")
    cursor.execute(
        """
        INSERT INTO gender(name)
        VALUES ('man'), ('woman')
        """)


# Створить таблицю people з атрибутами id (обов'язково), ім'я(обов'язково), прізвище(обов'язково), стать(обов'язково)
# foreign key на таблицю з гендерами, зарплата, посада як foreign key на таблицю з професіями, email, вік(обов'язково)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS people(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            sex VARCHAR(50) NOT NULL,
            gender_id INTEGER,
            salary REAL,
            profession_id INTEGER,
            email VARCHAR(50),
            age INTEGER NOT NULL,
            FOREIGN KEY(gender_id) REFERENCES gender(id),
            FOREIGN KEY(profession_id) REFERENCES profession(id)
        )""")

# Згенерує 20 записів на ваш смак причому для тих полів які не обов'язкові вказувати дані вибірково наприклад з 20 тільки
# 5 мають email, 10 посада тощо, а зарплата і вік генерується за допомогою функції рандом.
    professions_number = cursor.execute("""
        SELECT count(id) from profession
        """).fetchone()[0]
    print(professions_number)
    # db_conn = sqlite3.connect('profession.sl3')
    # db_conn.row_factory = sqlite3.Row
    #
    #
    # f = db_conn.cursor().execute("""
    #         SELECT count(*) AS cnt profession user LIMIT 1
    #         """).fetchone()

    genders_number = cursor.execute("""
        SELECT count(id) from gender
        """).fetchone()[0]

    count = 0
    while count < 21:
        data = requests.get('https://randomuser.me/api')
        random_user = data.json()['results'][0]
        name = random_user['name']['first']
        if not bool(re.search('[a-zA-Z]', name[0])):  # проверка на нелатиницу,т.к. апи выдает имена на арабском
            continue
        surname = random_user['name']['last']
        sex = random_user['gender']
        gender_id = random.randint(1, genders_number)
        age = random.randint(20, 80)
        email = random_user['email'] if count < 5 else None
        if count in range(4, 14):
            salary = random.randint(100, 5000)
            profession_id = random.randint(1, professions_number)
        else:
            salary = None
            profession_id = None

        cursor.execute("""
        INSERT INTO people (name,surname,sex,gender_id,salary,profession_id,email,age)
        VALUES ((?),(?), (?), (?), (?), (?), (?), (?))""",
                       (name, surname, sex, gender_id, salary, profession_id, email, age))
        count += 1

# - Додати два записи для Laurence Wachowski та Andrew Wachowski стать чоловік інші дані довільні
    cursor.execute("""
            INSERT INTO people (name,surname,sex,gender_id,profession_id, salary, age)
            VALUES ('Laurence', 'Wachowski', 'man', 1, 10000, 8, 56),
                   ('Andrew', 'Wachowski', 'man', 1, 10010, 8, 56) """)

# Змінити стать для Laurence Wachowski та Andrew Wachowski на жінка
    cursor.execute('''
    UPDATE people
    SET sex = 'woman'
    WHERE name IN ('Laurence', 'Andrew') and surname = 'Wachowski'
    ''')

# Змінити ім'я для Laurence Wachowski на Lana
    cursor.execute('''
    UPDATE people
    SET name = 'Lana'
    WHERE name = 'Laurence' and surname = 'Wachowski'
    ''')

# Змінити ім'я для Andrew Wachowski на Lilly
    cursor.execute('''
    UPDATE people
    SET name = 'Lilly'
    WHERE name = 'Andrew' and surname = 'Wachowski'
    ''')

# Додати новий гендер
    cursor.execute('''
    INSERT INTO gender('name')
    VALUES ('neutrois')
    ''')
# Змінити довільний людині гендер на новий
    cursor.execute("""
    UPDATE people
    SET gender_id = 3
    WHERE id = 2
    """)
# додати для всіх записів в яких немає email - email який складатиметься з імені, прізвища та довільного хосту
    cursor.execute("""
    UPDATE people 
    SET email = lower(name || '.' || surname || '@gmail.com')
    WHERE email IS NULL;
    """)

# Вивести всіх людей з новим гендером
with sqlite3.connect('people.sqlite') as db_connection:
    db_connection.row_factory = sqlite3.Row
    cursor = db_connection.cursor()
    gender3 = cursor.execute("""
     SELECT name, surname, sex, gender_id, profession_id, salary, age
     FROM people
     WHERE gender_id = 3
     """)
    for item in gender3:
        print(dict(item))

