from os import name
from flask import Flask, render_template
import pandas as pd
from IPython.core.display import HTML


app = Flask(__name__)


@app.route("/")
def index():
    pokemons = pd.read_excel("./lista_pokemons.xls")
    pokemons['num'] = pokemons['num'].astype(str)
    caminho_base = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'

    return render_template("index.html", pokemons=pokemons, caminho_base=caminho_base)



if (__name__ == "__main__"):
    app.run(debug=True)