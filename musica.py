from flask import Flask, render_template, request, redirect, session, flash, url_for

class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero


musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai banca', 'Mc Ryan SP', 'Funk')
musica03 = Musica('Camisa 10', 'Turma do Pagode', 'Pagode')

lista = [musica01, musica02, musica03]

class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

usuario01 = Usuario("Daniel Xavier", "daniel.xds93", "admin")
usuario02 = Usuario("João Zinho", "joao.zinho", "1234")
usuario03 = Usuario("Vilma Nunes", "vilmanunes104", "nunes")

usuarios = {
    usuario01.login : usuario01,
    usuario02.login : usuario02,
    usuario03.login : usuario03
}

app = Flask(__name__)

app.secret_key = 'aprendendodoiniciocomdaniel'

@app.route('/')
def listarMusicas():

    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))

    return render_template('lista_musicas.html', 
                           titulo = 'Musicas cadastradas',
                           musicas = lista)

@app.route('/cadastrar')
def cadastrar_musica():

    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))

    return render_template('cadastra_musica.html', 
                           titulo = "Cadastrar música")

@app.route('/adicionar', methods=['POST',])
def adicionar_musica():
    nome = request.form['txtNome']
    cantorBanda = request.form['txtCantor']
    genero = request.form['txtGenero']

    novaMusica = Musica(nome, cantorBanda, genero)

    lista.append(novaMusica)

    return redirect(url_for('listarMusicas'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['txtLogin'] in usuarios:

        usuarioEncontrado = usuarios[request.form['txtLogin']]

        if request.form['txtSenha'] == usuarioEncontrado.senha:

            session['usuario_logado'] = request.form['txtLogin']
        
            flash("Usuário logado com sucesso!")

            return redirect(url_for('listarMusicas'))
    else:

        flash("Usuário ou Senha inválida!")

        return redirect(url_for('login'))

@app.route('/sair')
def sair():
    session['usuario_logado'] = None

    return redirect('/login')



app.run(debug=True)