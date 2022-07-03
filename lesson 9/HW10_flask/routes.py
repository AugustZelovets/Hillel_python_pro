import random
import sqlite3
from datetime import datetime
import requests
from flask import render_template, request

from app import app
from forms import *
from db import get_connection


@app.route('/all_doings/')
def all_doings():
    with get_connection('db_sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        doings_list = cursor.execute("""
        SELECT doing.id, doing.title, doing.details, doing.date, doing.category_id, category.name as category_name
        FROM doing, category
        WHERE doing.category_id = category.id 
        ORDER BY doing.id DESC
        """).fetchall()

        title = 'All doings'
    return render_template('doings_list.html', doings_list=doings_list, title=title, headline=title)


@app.route('/today_doings/')
def today_doings():
    with get_connection('db_sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        today = datetime.today().strftime("%Y-%m-%d")
        doings_list = cursor.execute("""
        SELECT doing.id, doing.title, doing.details, doing.date, doing.category_id, category.name as category_name
        FROM doing, category
        WHERE doing.category_id = category.id and doing.date = (?)
        """, (today,)).fetchall()

        title = 'Doings for today'
    return render_template('doings_list.html', doings_list=doings_list, title=title, headline=title)


@app.route('/all_categories/')
def all_categories():
    with get_connection('db_sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        categories_list = cursor.execute("""
        SELECT id, name 
        FROM category 
        ORDER BY name
        """).fetchall()

        # cat_dict = []
        # for i in categories_list:
        #     keys = ['id', 'name']
        #     cat_dict.append(dict(zip(keys, i)))

        title = 'All categories'
    return render_template('categories_list.html', categories_list=categories_list,  title=title, headline=title)


@app.route('/doings_by_category/<int:searching_category_id>/', methods=['GET'])
def doings_by_category(searching_category_id):
    with get_connection('db_sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        doings_list = cursor.execute("""
            SELECT  
                doing.id, 
                doing.title, 
                doing.details, 
                doing.date, 
                doing.category_id, 
                category.id,
                category.name as category_name
            FROM doing
            JOIN category 
            ON category_id=category.id
            WHERE doing.category_id = (?)
            """, (searching_category_id,)).fetchall()
        category_name = cursor.execute("""   
                SELECT name 
                FROM  category
                WHERE category.id = (?)
                """, (searching_category_id,)).fetchone()[0]  # если не будет записи по этой кат., то и с записи не
        # получится взять имя категории, что приведет к ошибке, потому отд. запрос

        title = 'Doings by category ' + category_name
        return render_template('doings_list.html', doings_list=doings_list, title=title,
                               headline=title)


@app.route('/add_doing/', methods=['GET', 'POST'])
def add_doing():
    with get_connection('db_sqlite3') as db:
        cursor = db.cursor()
        choices_list = cursor.execute("""
        SELECT * FROM category""").fetchall()
    AddDoingForm.category = SelectField(choices=choices_list, validators=[DataRequired()])
    # без этого перечень категорий обновляется только при рестарте приложения, а не сразу после создания новой категории

    form = AddDoingForm()
    if form.validate_on_submit():
        with get_connection('db_sqlite3') as db:
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO doing(title, details, category_id, date) VALUES (?, ?, ?, ?);""",
                           (form.title.data, form.details.data, form.category.data, form.date.data,))
        return render_template('doing_created.html')

    random_category = random.choice(["education", "recreational", "social", "diy", "charity", "cooking", "relaxation",
                                     "music", "busywork"])
    data = requests.get('https://www.boredapi.com/api/activity/', params=f'?type={random_category}')
    random_activity = data.json()

    activity = random_activity['activity']
    activity_category = random_activity['type']
    title = 'Add doing'
    context = {'form': form,
               'activity_category': activity_category,
               'activity': activity,
               'title': title,
               }
    return render_template('add_doing.html', title=title, context=context)


@app.route('/add_category/', methods=['GET', 'POST'])
def add_category():
    method = request.method
    form = AddCategoryForm()
    if form.validate_on_submit():
        with get_connection('db_sqlite3') as db:
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO category(name) VALUES (?);""", (form.name.data,))
            return render_template('category_created.html')

    title = 'Add category'
    return render_template('add_category.html', form=form, title=title)
