from flask import Flask, render_template

app = Flask('Mysite')


@app.route('/list/')
def full_list():
    title = 'Весь текст'
    description = 'Весь текст:'

    with open('text_for_hw4', "r", encoding='utf-8') as i:
        lines = i.readlines()

    context = {
        'title': title,
        'description': description,
        'lines': lines,
    }

    return render_template('homework4.html', context=context)


@app.route('/filter/<string:word>/')
def filtered_list_by_word(word):
    title = 'Фильтр по словам'
    description = f'Результаты поиска для "{word}":'

    with open('text_for_hw4', "r", encoding='utf-8') as i:
        lines = [line for line in i.readlines() if str(word).lower() in line]

    context = {
        'title': title,
        'lines': lines,
        'description': description,
    }

    return render_template('homework4.html', context=context)


@app.route('/show/<int:number>/')
def list_by_number(number):
    title = 'Фильтр по количеству строк'
    description = f'Первые {number} строк файла:'

    with open('text_for_hw4', "r", encoding='utf-8') as i:
        lines = i.readlines()[:number]

    context = {
        'title': title,
        'description': description,
        'lines': lines,
    }

    return render_template('homework4.html', context=context)


app.run()
