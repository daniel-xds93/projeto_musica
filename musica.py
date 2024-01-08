from flask import Flask, render_template, request, redirect

class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero


musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai banca', 'Mc Ryan SP', 'Funk')
musica03 = Musica('Camisa 10', 'Turma do Pagode', 'Pagode')

lista = [musica01, musica02, musica03]

app = Flask(__name__)

@app.route('/')
def listarMusicas():

    return render_template('lista_musicas.html', 
                           titulo = 'Aprendendo do início com Daniel',
                           musicas = lista)

@app.route('/cadastrar')
def cadastrar_musica():
    return render_template('cadastra_musica.html')

@app.route('/adicionar', methods=['POST',])
def adicionar_musica():
    nome = request.form['txtNome']
    cantorBanda = request.form['txtCantor']
    genero = request.form['txtGenero']

    novaMusica = Musica(nome, cantorBanda, genero)

    lista.append(novaMusica)

    return redirect('/')


app.run(debug=True)