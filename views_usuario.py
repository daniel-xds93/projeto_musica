from flask import render_template, request, redirect, session, flash, url_for
from musica import  app, db
from definicoes import FormularioUsuario, FormularioCadastroUsuario
from flask_bcrypt import generate_password_hash, check_password_hash

@app.route('/login')
def login():

    form = FormularioUsuario()

    return render_template('login.html', form = form)

@app.route('/autenticar', methods=['POST',])
def autenticar():

    from models import Usuario

    form = FormularioUsuario(request.form)

    usuario = Usuario.query.filter_by(login_usuario=form.usuario.data).first()

    senha = check_password_hash(usuario.senha_usuario, form.senha.data)

    if usuario and senha:

        session['usuario_logado'] = usuario.login_usuario
        
        flash(f"Usuário {usuario.login_usuario} logado com sucesso!")

        return redirect(url_for('listarMusicas'))

    else:

        flash("Usuário ou Senha inválida!")

        return redirect(url_for('login'))
    
@app.route('/cadastraUsuario')
def cadastra_usuario():

    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))

    form = FormularioCadastroUsuario()

    return render_template('cadastra_usuario.html', 
                           titulo = 'Cadastro de Usuario', form = form)

@app.route('/addUsuario', methods=['POST',])
def adicionar_usuario():

    formRecebido = FormularioCadastroUsuario(request.form)

    if not formRecebido.validate_on_submit():
        return redirect(url_for('cadastra_usuario'))
    
    nome = formRecebido.nome.data
    usuario = formRecebido.usuario.data
    senha = generate_password_hash(formRecebido.senha.data).decode('utf-8')

    from models import Usuario

    usuario_existe = Usuario.query.filter_by(login_usuario=usuario).first()

    if usuario_existe:
        flash('Usuario já cadastrado')
        return redirect(url_for('cadastra_usuario'))
    
    novo_usuario = Usuario(nome_usuario = nome, login_usuario = usuario,
                            senha_usuario = senha)
    
    db.session.add(novo_usuario)
    db.session.commit()

    flash('Usuário cadastrado com sucesso!')

    return redirect(url_for('listarMusicas'))


@app.route('/sair')
def sair():
    session['usuario_logado'] = None

    return redirect('/login')