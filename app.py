from flask import Flask, render_template
import sqlite3
from pathlib import Path
#import requests

app = Flask("Spotifaux")

if not Path('database/spotifaux.db').exists():
    conn = sqlite3.connect('database/spotifaux.db')
    sql = Path('tables.sql').read_text()
    conn.executescript(sql)

@app.route('/')
def users():
    # se connecter à la base de données
    conn = sqlite3.connect('database/spotifaux.db')

    # récupérer les utilisateurs dans la table USER_USR
    cursor = conn.execute('SELECT * FROM USER_USR')
    users = cursor.fetchall()

    # fermer la connexion à la base de données
    conn.close()

    # afficher les utilisateurs dans une page HTML
    return render_template('users.html', users=users)

@app.route('/albums/<artist_id>')
def albums(artist_id):
    # Code pour récupérer les albums de l'artiste sélectionné
    return render_template('albums.html', album_list=album_list)


