from flask import Flask, render_template

app = Flask(__name__)

# Exercise 1 ___________________________________________________

@app.route('/')
def index():
    return "This is the Index page"

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/members')
def members():
    return "Members page"




# Exercise 2 ___________________________________________________


@app.route('/score/<int:score>')
def score(score):
    return  render_template('index.html', a = score)



# Exercise 2 ___________________________________________________

@app.route('/css')
def css():
    return render_template('css.html')


if __name__ == '__main__':
    app.run(debug = True)
