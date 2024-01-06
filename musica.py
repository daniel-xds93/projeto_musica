from flask import Flask, render_template

class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero


app = Flask(__name__)

@app.route('/musicas')
def listarMusicas():

    musica01 = Musica('Temporal', 'Hungria', 'Rap')
    musica02 = Musica('Papai banca', 'Mc Ryan SP', 'Funk')
    musica03 = Musica('Camisa 10', 'Turma do Pagode', 'Pagode')


    lista = [musica01, musica02, musica03]

    return render_template('lista_musicas.html', 
                           titulo = 'Aprendendo do início com Daniel',
                           musicas = lista)

@app.route('/cadastrar')
def cadastrar_musica():
    return render_template('cadastra_musica.html')


app.run(debug=True)