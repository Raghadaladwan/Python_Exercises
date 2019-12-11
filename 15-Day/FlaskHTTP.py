from flask import *
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'abc'


@app.route('/')
def success():
    return render_template("show.html")


@app.route('/show', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        info = request.form
        return render_template('print.html', info=info)


@app.route('/')
def index():
    return "<a href='/list'> List </a>"


@app.route('/list')
def list():
    con = sql.connect("stocks.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from stocks")

    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)