import os
from musica import app

def recupera_imagem(id):
    for nome_imagem in os.listdir(app.config['UPLOAD_PASTA']):

        nome = str(nome_imagem)

        nome = nome.split('.')

        if f'album{id}_' in nome[0]:
            return nome_imagem
        
    return 'default.png'