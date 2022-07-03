from flask import Flask, render_template

app = Flask('Mysite')


@app.route('/list/')
def full_list():
    my_file = open("text_for_hw4", "r", encoding='utf-8')
    title = 'Весь текст'
    description = 'Весь текст:'
    text = []
    while True:
        line = my_file.readline()
        if not line:
            break
        text.append(line.strip())

    context = {
        'text': text,
        'title': title,
        'description': description,
    }
    my_file.close()
    return render_template('homework4.html', context=context)


@app.route('/filter/<string:word>/')
def filtered_list_by_word(word):
    my_file = open("text_for_hw4", "r", encoding='utf-8')
    text = []
    title = 'Фильтр по словам'
    description = f'Результаты поиска для "{word}":'

    while True:
        line = my_file.readline()
        if not line:
            break
        if str(word).lower() in line.lower():
            text.append(line.strip())

    context = {
        'text': text,
        'title': title,
        'description': description,
    }
    my_file.close()

    return render_template('homework4.html', context=context)


@app.route('/show/<int:number>/')
def list_by_number(number):
    my_file = open("text_for_hw4", "r", encoding='utf-8')
    text = []
    title = 'Фильтр по количеству строк'
    description = f'Первые {number} строк файла:'

    for i in range(number):
        line = my_file.readline()
        if not line:
            break
        text.append(line.strip())
    context = {
        'text': text,
        'title': title,
        'description': description,
    }
    my_file.close()

    return render_template('homework4.html', context=context)


app.run()
