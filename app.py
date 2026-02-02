from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-soma_1'] and request.form['form-soma_2']:
            n1 = int(request.form['form-soma_1'])
            n2 = int(request.form['form-soma_2'])
            soma = n1 + n2
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
    return render_template("operacoes.html")

@app.route('/subtrarir', methods=['GET', 'POST'])
def subtrarir():
    if request.method == 'POST':
        if request.form['form-sub_1'] and request.form['form-sub_2']:
            n1 = int(request.form['form-sub_1'])
            n2 = int(request.form['form-sub_2'])
            subtracao = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)
    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        if request.form['form-mult_1'] and request.form['form-mult_2']:
            n1 = int(request.form['form-mult_1'])
            n2 = int(request.form['form-mult_2'])
            multiplicar = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)
    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-divi_1'] and request.form['form-divi_2']:
            n1 = int(request.form['form-divi_1'])
            n2 = int(request.form['form-divi_2'])
            divisao = n1 / n2
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)
    return render_template("operacoes.html")

#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)