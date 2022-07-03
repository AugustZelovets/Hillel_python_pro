@app.route('/doings_by_category/', methods=['GET', 'POST'])
def doings_by_category():
    with get_connection('db_sqlite3') as db:
        cursor = db.cursor()
        choices_list = cursor.execute("""
        SELECT * FROM category""").fetchall()
    DoingsByCategoryForm.category = SelectField('Category name', choices=choices_list, validators=[DataRequired()])
    # без этого перечень категорий обновляется только при рестарте приложения, а не сразу после создания новой категории

    form = DoingsByCategoryForm()
    if form.validate_on_submit():
        category_id = form.category.data
        with get_connection('db_sqlite3') as db:
            cursor = db.cursor()
            doings_list = cursor.execute("""
                    SELECT doing.title, doing.details, doing.date, category.name 
                    FROM doing, category
                    WHERE doing.category_id = category.id and category.id = (?)
                    """, (category_id,)).fetchall()

            category_name = cursor.execute("""
                    SELECT name 
                    FROM  category
                    WHERE category.id = (?)
                    """, (category_id,)).fetchone()[0]

        title = 'Doings by category ' + category_name
        return render_template('doings_list.html', doings_list=doings_list, title=title, headline=title)
    title = 'Search doings by category'

    return render_template('doings_by_category.html', form=form, title=title, headline=title)




#2
@app.route('/doings_by_category/category_id/', methods=['GET', 'POST'])
def doings_by_category(category_id):
    with get_connection('db_sqlite3') as db:
        cursor = db.cursor()
        doings_list = cursor.execute("""
                SELECT doing.id, doing.title, doing.details, doing.date, category.name 
                FROM doing, category
                WHERE doing.category_id = category.id and doing.category_id = (?)
                """, (category_id,)).fetchall()
        category_name = doings_list[-1]
        title = 'Doings by category ' + category_name
        return render_template('doings_list.html', doings_list=doings_list, title=title, headline=title)