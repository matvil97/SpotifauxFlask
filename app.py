from flask import Flask, render_template, request, flash, redirect, url_for, Response, session
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path
import sqlite3

app = Flask("Spotifaux")

if not Path('database/spotifaux.db').exists():
    conn = sqlite3.connect('database/spotifaux.db')
    conn.execute('PRAGMA encoding="UTF-8"')
    sql = Path('tables.sql').read_text(encoding='utf-8')
    conn.executescript(sql)


# Configurer la session de l'application pour qu'elle utilise un secret key
app.secret_key = 'super_secret_key'


@app.route('/')
def titles():
    if 'ID_USR' in session:
        # se connecter à la base de données
        conn = sqlite3.connect('database/spotifaux.db')

        # récupérer les utilisateurs dans la table TITLE_TTL
        cursor = conn.execute('SELECT * FROM TITLE_TTL')
        titles = cursor.fetchall()

        # fermer la connexion à la base de données
        conn.close()

        # afficher les utilisateurs dans une page HTML
        return render_template('index.html', titles=titles)
    else:
        return redirect('/login')

# Route pour traiter le formulaire de login


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database/spotifaux.db')
        cursor = conn.execute(
            'SELECT * FROM USER_USR WHERE USR_MAIL = ?', (email,))
        user = cursor.fetchone()

        if user[3] == password:
            # l'utilisateur est authentifié
            # rediriger vers la page d'accueil
            session['ID_USR'] = user[0]
            session['USR_USERNAME'] = user[1]
            session['USR_MAIL'] = email
            return redirect('/')
        else:
            # l'utilisateur n'est pas authentifié
            # rediriger vers la page de connexion
            flash("E-mail ou mot de passe incorrect ! Veuillez réessayer.")
            return redirect('/login')
    return render_template('login.html')


@app.route('/logout')
# @login_required
def logout():
    session.clear()
    return redirect('/')


@app.route('/test')
def test_db():
    conn = sqlite3.connect('database/spotifaux.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER_USR")
    data = cursor.fetchall()
    conn.close()
    return str(data)


if __name__ == '__main__':
    app.run(debug=True)
