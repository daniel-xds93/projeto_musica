from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def hello():
    return "<h3>Bem vindo a minha primeira aplicação flask</h3>"

app.run()