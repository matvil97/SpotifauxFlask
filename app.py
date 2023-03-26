from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        artist_name = request.form['artist_name']
        # Code pour effectuer la recherche d'artistes
        return render_template('index.html', artist_list=artist_list)
    else:
        return render_template('index.html')

@app.route('/albums/<artist_id>')
def albums(artist_id):
    # Code pour récupérer les albums de l'artiste sélectionné
    return render_template('albums.html', album_list=album_list)


