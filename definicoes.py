import os
from musica import app

def recupera_imagem(id):
    for nome_imagem in os.listdir(app.config['UPLOAD_PASTA']):
        if nome_imagem == f'album{id}':
            return nome_imagem
        
    return 'default.png'