from flask import Flask, flash, render_template, url_for, request, redirect
from sqlalchemy.exc import SQLAlchemyError
from database import db_session, Funcionarios
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from api_routes import routes

app = Flask(__name__)
# Mover para .env
app.config['SECRET_KEY'] = 'FLAMINGO'

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(funci_id):
    funcio = select(Funcionarios).where(Funcionarios.id == int(funci_id))
    result = db_session.execute(funcio).scalar_one_or_none()
    return result


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/gatos')
def listar_gatos():
    l_gatos = routes.get_gatos()
    print('antes:', l_gatos)
    for i in l_gatos:
        i["temperament"] = i["temperament"].split(',')
        i["imagem"] = routes.get_image()["url"]

    return render_template('gatos.html',l_gatos=l_gatos)


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
            flash('Preencha todos os campos para fazer a Soma', 'alert-alert-danger')
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
            flash('Preencha todos os campos para fazer a Subtração', 'alert-alert-danger')
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
            flash('Preencha todos os campos para fazer a Multiplicação', 'alert-alert-danger')
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
            flash('Preencha todos os campos para fazer a Divisão', 'alert-alert-danger')
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
            flash('Preencha todos os campos para calcular o Área do Triangulo', 'alert-alert-danger')
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
            flash('Preencha todos os campos para calcular o Perímetro do Triangulo', 'alert-alert-danger')
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
            flash('Preencha todos os campos para calcular a Área do Circulo', 'alert-alert-danger')
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
            flash('Preencha todos os campos para calcular o Perímetro do Circulo', 'alert-alert-danger')
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
            flash('Preencha todos os campos para calcular a Área do Quadrado', 'alert-alert-danger')
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
            flash('Preencha todos os campos para calcular o Perímetro do Quadrado', 'alert-alert-danger')
    return render_template('geometria.html')


@app.route('/area_hexagono', methods=['GET', 'POST'])
def area_hexagono():
    if request.method == 'POST':
        if request.form['form_lado_h']:
            lado_h = float(request.form['form_lado_h'])
            area_h = (3 * pow(lado_h, 2) * 3 ** 0.5) / 2  # A = (3√3 * L²) / 2
            flash('Área do Hexagono Calculado', 'alert-success')
            return render_template('geometria.html', lado_h=lado_h, area_h=round(area_h, 2))
        else:
            flash('Preencha todos os campos para calcular a Área do Hexagono', 'alert-alert-danger')
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
            flash('Preencha todos os campos para calcular o Perímetro do Hexagono', 'alert-alert-danger')
    return render_template('geometria.html')


@app.route('/funcionario')
@login_required
def funcionario():
    sql_funcio = select(Funcionarios)
    funcio_exe = db_session.execute(sql_funcio).scalars().all()
    print(f'aaa: {funcio_exe}')
    return render_template('funcionarios.html',funcio_exe=funcio_exe)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')
        if not email:
            flash('Porfavor insira o email', 'alert-danger')
            return render_template('login.html')
        if not senha:
            flash('Porfavor insira o senha', 'alert-danger')
            return render_template('login.html')
        email_sql = select(Funcionarios).where(Funcionarios.email == email)
        result = db_session.execute(email_sql).scalar_one_or_none()
        print('asd', result)
        if result:
            if result.check_password(senha):
                login_user(result)
                flash('Logado com sucesso!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Senha Incorreta', 'error')
                return redirect(url_for('login'))
        else:
            flash(f'Email não Encontrado', 'alert-danger')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))

@app.route('/cadastrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form.get('form_nome')
        data_nascimento = request.form.get('form_date_nascimento')
        cpf = request.form.get('form_cpf')
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')
        cargo = request.form.get('form_cargo')
        salario = request.form.get('form_salario')
        if not request.form['form_nome']:
            flash('Preencha o Campo Nome', 'alert-alert-danger')
            print('Preencha o Campo Nome')
            return redirect(url_for('login'))

        if not request.form['form_date_nascimento']:
            flash('Preencha o Campo Data Nascimento', 'alert-alert-danger')
            print('Preencha o Campo Data Nascimento')
            return redirect(url_for('login'))

        if not request.form['form_cpf']:
            flash('Preencha o Campo CPF', 'alert-alert-danger')
            print('Preencha o Campo CPF')
            return redirect(url_for('login'))

        if not request.form['form_email']:
            flash('Preencha o Campo Email', 'alert-alert-danger')
            print('Preencha o Campo Email')
            return redirect(url_for('login'))

        if not request.form['form_senha']:
            flash('Preencha o Campo Senha', 'alert-alert-danger')
            print('Preencha o Campo Senha')
            return redirect(url_for('login'))

        if not request.form['form_cargo']:
            flash('Preencha o Campo Cargo', 'alert-alert-danger')
            print('Preencha o Campo Cargo')
            return redirect(url_for('login'))

        if not request.form['form_salario']:
            flash('Preencha o Campo Salario', 'alert-alert-danger')
            print('Preencha o Campo Salario')
            return redirect(url_for('login'))

        ver_email = select(Funcionarios).where(Funcionarios.email == email)
        exist_email = db_session.execute(ver_email).scalar_one_or_none()
        if exist_email:
            flash(f'Email: {email} já esta cadastrado', 'alert-danger')
            return render_template('login.html')
        try:
            new_user = Funcionarios(nome=nome, data_nascimento=data_nascimento, cpf=cpf,email=email, cargo=cargo, salario=float(salario))
            new_user.set_password(senha)
            db_session.add(new_user)
            db_session.commit()
            flash(f'Usuario: {nome} Cadastrado com sucesso!', 'success')
            print('Cadastrado com sucesso!')
            return redirect(url_for('funcionario'))
        except SQLAlchemyError as e:
            flash(f'Erro na base de dados', 'alert-danger')
            print(f'Erro na base de dados {e}')
            return redirect(url_for('funcionario'))
        except Exception as e:
            flash(f'Error', 'alert-danger')
            print(f'Erro: {e}')
            return redirect(url_for('funcionario'))

@app.route('/editar_funcionario/<int:var_id>', methods=['GET', 'POST'])
def editar_funcionario(var_id):
    edit_funcio = select(Funcionarios).where(Funcionarios.id == var_id)
    result_f = db_session.execute(edit_funcio).scalar_one_or_none()
    if request.method == 'POST':
        novo_name = request.form.get('form_nome')
        novo_data_nascimento = request.form.get('form_date_nascimento')
        novo_cpf = request.form.get('form_cpf')
        novo_email = request.form.get('form_email')
        novo_cargo = request.form.get('form_cargo')
        novo_salario = request.form.get('form_salario')
        if novo_name != '':
            result_f.nome = novo_name
        if novo_data_nascimento != '':
            result_f.data_nascimento = novo_data_nascimento
        if novo_cpf != '':
            result_f.cpf = novo_cpf
        if novo_email != '':
            result_f.email = novo_email
        if novo_cargo != '':
            result_f.cargo = novo_cargo
        if novo_salario != '':
            result_f.salario = novo_salario
        try:
            db_session.commit()
            flash('Funcionario editado com sucesso!', 'success')
            return redirect(url_for('funcionario'))
        except SQLAlchemyError as e:
            print(f'Erro: {e} na base de dados')
            flash(f'Erro na base de dados','alert-danger')
            db_session.rollback()
            return redirect(url_for('funcionario'))
        except Exception as e:
            print(f'Erro: {e}')
            flash(f'Erro: {e}','alert-danger')
    return render_template('funcionarios.html',result_f=result_f)

@app.route('/deletar_funcionario/<int:var_id>', methods=['GET', 'POST'])
def deletar_funcionario(var_id):
    delet_funcio = select(Funcionarios).where(Funcionarios.id == int(var_id))
    result_f = db_session.execute(delet_funcio).scalar_one_or_none()
    if request.method == 'POST':
        try:
            db_session.delete(result_f)
            db_session.commit()
            flash('Funcionario deletado com sucesso!', 'success')
            return redirect(url_for('funcionario'))
        except SQLAlchemyError as e:
            print(f'Erro: {e} na base de dados')
            flash(f'Erro na base de dados','alert-danger')
            db_session.rollback()
            return redirect(url_for('funcionario'))
        except Exception as e:
            print(f'Erro: {e}')
            flash(f'Erro: {e}','alert-danger')
        return render_template('funcionarios.html',result_f=result_f)
    return render_template('funcionarios.html',result_f=result_f)

@app.route('/animais')
def animais():
    return render_template('animais.html')

# TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)
