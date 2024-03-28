from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


def get_rows(surname, name, patron, birth, vmeda_id):
    if surname:
        return True
    else:
        return False


@app.route('/', methods=['GET', 'POST'])
def index():
    # show_rows = False
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


if __name__ == '__main__':
    app.run(debug=True)
