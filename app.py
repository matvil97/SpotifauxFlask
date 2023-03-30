from flask import Flask, render_template
import sqlite3
from pathlib import Path
#import requests

app = Flask("Spotifaux")

if not Path('database/spotifaux.db').exists():
    conn = sqlite3.connect('database/spotifaux.db')
    sql = Path('tables.sql').read_text()
    conn.executescript(sql)

# définir la constante pour la colonne "username"
USR_USERNAME = "USR_USERNAME"

@app.route('/')
def users():
    # se connecter à la base de données 
    conn = sqlite3.connect('database/spotifaux.db')

    # récupérer les utilisateurs dans la table USER_USR
    cursor = conn.execute('SELECT * FROM USER_USR')
    users = cursor.fetchall()

    # obtenir les noms de colonnes de la requête SQL
    column_names = [description[0] for description in cursor.description]

    # fermer la connexion à la base de données
    conn.close()

    # afficher les utilisateurs dans une page HTML
    return render_template('index.html', users=users, column_names=column_names)