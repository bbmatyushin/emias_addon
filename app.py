import hashlib
from flask import Flask, render_template, url_for, request, redirect, session, abort, flash


app = Flask(__name__)
app.secret_key = 'this_is_secret'

def get_rows(surname, name, patron, birth, vmeda_id):
    if surname:
        return True
    else:
        return False


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    """Страница авторизации пользователя"""
    if request.form.get('password'):
        password = hashlib.md5(request.form.get('password').encode()).hexdigest()
    else:
        password = None

    if 'user_logged' in session:
        print(session['user_logged'])
        return render_template('index.html')
    elif request.form.get('username') == 'addon' and \
            password == '5ed7c8e723fb6c53dd302312792bdeb0':
        session['user_logged'] = request.form['username']
        return render_template('index.html')
    # print(1)
    elif request.form.get('username') or request.form.get('password'):
        flash('Неверный логин или пароль!', 'error')
        return render_template('login.html')
    else:
        # flash('Необходимо указать Имя пользователя и пароль для входа.', 'error')
        return render_template('login.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'user_logged' in session:  # проверка авторизированного пользователя
        if request.method == 'POST':
            surname = request.form['surname'] if request.form['surname'] else None
            name = request.form['name'] if request.form['name'] else None
            patron = request.form['patron'] if request.form['patron'] else None
            birth = request.form['birth'] if request.form['birth'] else None
            vmeda_id = request.form['vmeda_id'] if request.form['vmeda_id'] else None

            print(surname, name, patron, birth, vmeda_id)

            show_rows = get_rows(surname, name, patron, birth, vmeda_id)
            # return redirect('/')
            return render_template('index.html', show_rows=show_rows,
                                   surname=surname,
                                   name=name,
                                   patron=patron)
        else:
            return render_template('index.html')
    else:
        abort(401)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5055)
