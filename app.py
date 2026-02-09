from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flamingo'


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
            flash('Soma Realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            flash('Preencha todos os campos para fazer a Soma', 'alert-danger')
    return render_template("operacoes.html")


@app.route('/subtrarir', methods=['GET', 'POST'])
def subtrarir():
    if request.method == 'POST':
        if request.form['form-sub_1'] and request.form['form-sub_2']:
            n1 = int(request.form['form-sub_1'])
            n2 = int(request.form['form-sub_2'])
            subtracao = n1 - n2
            flash('Subtração Realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)
        else:
            flash('Preencha todos os campos para fazer a Subtração', 'alert-danger')
    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        if request.form['form-mult_1'] and request.form['form-mult_2']:
            n1 = int(request.form['form-mult_1'])
            n2 = int(request.form['form-mult_2'])
            multiplicar = n1 * n2
            flash('Multiplicação Realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)
        else:
            flash('Preencha todos os campos para fazer a Multiplicação', 'alert-danger')
    return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-divi_1'] and request.form['form-divi_2']:
            n1 = int(request.form['form-divi_1'])
            n2 = int(request.form['form-divi_2'])
            divisao = n1 / n2
            flash('Divisão Realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)
        else:
            flash('Preencha todos os campos para fazer a Divisão', 'alert-danger')
    return render_template("operacoes.html")


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/area_triangulo', methods=['GET', 'POST'])
def area_triangulo():
    if request.method == 'POST':
        if request.form['form_lado_t']:
            lado_t = float(request.form['form_lado_t'])
            area_t = (pow(lado_t, 2) * 3 ** 0.5) / 4
            flash('Área do Triangulo Calculado', 'alert-success')
            return render_template('geometria.html', lado_t=lado_t, area_t=round(area_t, 2))
        else:
            flash('Preencha todos os campos para calcular o Área do Triangulo', 'alert-danger')
            return render_template('geometria.html')


@app.route('/perimetro_triangulo', methods=['GET', 'POST'])
def perimetro_triangulo():
    if request.method == 'POST':
        if request.form['form_lado_t']:
            lado_t = float(request.form['form_lado_t'])
            perime_t = lado_t * 3
            flash('Perímetro do Triangulo Calculado', 'alert-success')
            return render_template('geometria.html', lado_t=lado_t, perime_t=round(perime_t, 2))
        else:
            flash('Preencha todos os campos para calcular o Perímetro do Triangulo', 'alert-danger')
    return render_template('geometria.html')


@app.route('/area_circulo', methods=['GET', 'POST'])
def area_circulo():
    if request.method == 'POST':
        if request.form['form_raio']:
            raio = float(request.form['form_raio'])
            area_c = 3.14 * pow(raio, 2)
            flash('Área do Circulo Calculado', 'alert-success')
            return render_template('geometria.html', raio=raio, area_c=round(area_c, 2))
        else:
            flash('Preencha todos os campos para calcular a Área do Circulo', 'alert-danger')
    return render_template('geometria.html')


@app.route('/perimetro_circulo', methods=['GET', 'POST'])
def perimetro_circulo():
    if request.method == 'POST':
        if request.form['form_raio']:
            raio = float(request.form['form_raio'])
            perime_c = 2 * 3.14 * raio
            flash('Perímetro do Circulo Calculado', 'alert-success')
            return render_template('geometria.html', raio=raio, perime_c=round(perime_c, 2))
        else:
            flash('Preencha todos os campos para calcular o Perímetro do Circulo', 'alert-danger')
    return render_template('geometria.html')


@app.route('/area_quadrado', methods=['GET', 'POST'])
def area_quadrado():
    if request.method == 'POST':
        if request.form['form_lado_q']:
            lado_q = float(request.form['form_lado_q'])
            area_q = pow(lado_q, 2)
            flash('Área do Quadrado Calculado', 'alert-success')
            return render_template('geometria.html', lado_q=lado_q, area_q=round(area_q, 2))
        else:
            flash('Preencha todos os campos para calcular a Área do Quadrado', 'alert-danger')
    return render_template('geometria.html')


@app.route('/perimetro_quadrado', methods=['GET', 'POST'])
def perimetro_quadrado():
    if request.method == 'POST':
        if request.form['form_lado_q']:
            lado_q = float(request.form['form_lado_q'])
            perime_q = 4 * lado_q
            flash('Perímetro do Quadrado Calculado', 'alert-success')
            return render_template('geometria.html', lado_q=lado_q, perime_q=round(perime_q, 2))
        else:
            flash('Preencha todos os campos para calcular o Perímetro do Quadrado', 'alert-danger')
    return render_template('geometria.html')


@app.route('/area_hexagono', methods=['GET', 'POST'])
def area_hexagono():
    if request.method == 'POST':
        if request.form['form_lado_h']:
            lado_h = float(request.form['form_lado_h'])
            area_h = (3 * pow(lado_h, 2) * 3 ** 0.5) / 2 # A = (3√3 * L²) / 2
            flash('Área do Hexagono Calculado', 'alert-success')
            return render_template('geometria.html', lado_h=lado_h, area_h=round(area_h, 2))
        else:
            flash('Preencha todos os campos para calcular a Área do Hexagono', 'alert-danger')
    return render_template('geometria.html')


@app.route('/perimetro_hexagano', methods=['GET', 'POST'])
def perimetro_hexagano():
    if request.method == 'POST':
        if request.form['form_lado_h']:
            lado_h = float(request.form['form_lado_h'])
            perime_h = 6 * lado_h
            flash('Perímetro do Hexagono Calculado', 'alert-success')
            return render_template('geometria.html', lado_h=lado_h, perime_h=round(perime_h, 2))
        else:
            flash('Preencha todos os campos para calcular o Perímetro do Hexagono','alert-danger')
    return render_template('geometria.html')

@app.route('/funcionario')
def funcionario():
    return render_template('funcionarios.html')

# TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)
