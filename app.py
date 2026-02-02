from flask import Flask, flash
from flask import render_template, redirect, request, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/calculo')
def calculo():
    return render_template('calculo.html')

@app.route('/operaçoes')
def operacoes():
    return render_template('operacoes.html')

@app.route('/soma', methods=['GET','POST'])
def soma():
    if request.method == 'POST':
        if not request.form['form_num_1'] or not request.form['form_num_2']:
            flash("preencha o campo dos numeros", "error")
        num1 = request.form['form_num_1']
        num2 = request.form['form_num_2']
        try:
            num1 = int(num1)
            num2 = int(num2)
            result = num1 + num2
            print('resultado: ', result)
            return redirect(url_for('resultado',result=result))
        except:
            flash("preencha o campo dos numeros", "error")
    return render_template('soma.html')

@app.route('/subtracao')
def subtracao():
    return render_template('subtacao.html')

@app.route('/multiplicacao')
def multiplicacao():
    return render_template('multiplicacao.html')

@app.route('/divisao')
def divisao():
    return render_template('divisao.html')


@app.route('/resultado')
def resultado():
    return render_template('resultado.html')


if __name__ == '__main__':
    app.run(debug=True)