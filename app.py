from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/calculo')
def calculo():
    return render_template('calculo.html')

@app.route('/operacoes')
def operacoes():
    return render_template('operacoes.html')

if __name__ == '__main__':
    app.run(debug=True)