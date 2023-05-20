from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/website_2/buttons')
def buttons():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
