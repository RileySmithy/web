from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
    
    btn_pressed = request.form.get('press')
    if btn_pressed:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
