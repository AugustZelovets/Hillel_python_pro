from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired

from db import get_connection


class AddCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    enter = SubmitField('Enter')


class AddDoingForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    details = TextAreaField('Details')
    category = SelectField(choices=[], validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])
    enter = SubmitField('Enter')


class DoingsByCategoryForm(FlaskForm):
    with get_connection('db_sqlite3') as db:
        cursor = db.cursor()
        choices_list = cursor.execute("""
        SELECT * FROM category""").fetchall()
    category = SelectField('Category name', choices=choices_list, validators=[DataRequired()])
    search = SubmitField('Search')

