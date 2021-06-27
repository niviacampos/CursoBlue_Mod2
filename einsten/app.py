from flask import Flask, render_template


app = Flask(__name__)


@app.route("/<status>")
def index(status=None):
    nome = "Betão"
    sobrenome = "Einsten"
    idade = 42

    if status == "doido":
        doido = False
    else:
        doido = True
        
    imagem_serio = "/static/einsten_normal.jpeg"
    imagem_doido = "https://www.hypeness.com.br/1/2017/08/EinsteinL3.jpg"

    return render_template('index.html', nome=nome, sobrenome=sobrenome, idade=idade, doido=doido, imagem_serio=imagem_serio, imagem_doido=imagem_doido)


if (__name__ == "__main__"):
    app.run(debug=True)