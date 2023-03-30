from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    session,
)
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path
import sqlite3

app = Flask("Spotifaux")

# If databse doesn't exist, create it by reading the script tables.sql

if not Path("database/spotifaux.db").exists():
    conn = sqlite3.connect("database/spotifaux.db")
    conn.execute('PRAGMA encoding="UTF-8"')
    sql = Path("tables.sql").read_text(encoding="utf-8")
    conn.executescript(sql)


# Configure the application session to use a secret key
app.secret_key = "super_secret_key"


# Root - Index with Titles data

@app.route("/")
def titles():
    if "ID_USR" in session:
        # connect to the database
        conn = sqlite3.connect("database/spotifaux.db")

        # get data from the TITLE_TTL table
        cursor = conn.execute("SELECT * FROM TITLE_TTL")
        titles = cursor.fetchall()

        # close the connection to the database
        conn.close()

        # send the result of the SQL query as data name 'titles'
        return render_template("index.html", titles=titles)
    else:
        return redirect("/login")


# Root - Login form processing


@app.route("/login", methods=["GET", "POST"])
def login_post():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database/spotifaux.db")
        cursor = conn.execute(
            "SELECT * FROM USER_USR WHERE USR_MAIL = ?", (email,))
        user = cursor.fetchone()

       # flash(user[3])
        
        if user[3] == password:
            # the user is authenticated
            # redirect to the home page
            session["ID_USR"] = user[0]
            session["USR_USERNAME"] = user[1]
            session["USR_MAIL"] = email
            return redirect("/")
        else:
            # the user is not authenticated
            # redirect to the login page
            flash("Incorrect e-mail or password! Please try again.")
            return redirect("/login")
    return render_template("login.html")


# Root - Log out feature

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


@app.route('/liked')
#@login_required
def liked_titles():
    # Se connecter à la base de données
    conn = sqlite3.connect('database/spotifaux.db')
    
    # Récupérer les titres likés de l'utilisateur connecté
    cursor = conn.execute('SELECT LUS.*, TTL.TTL_NAME,TTL.TTL_ARTIST FROM LIKE_USER_LUS LUS JOIN TITLE_TTL TTL ON LUS.ID_TTL = TTL.ID_TTL WHERE ID_USR = ?', (session['ID_USR'],))
    liked_titles = cursor.fetchall()
    
    # Fermer la connexion à la base de données
    conn.close()

    # Afficher la page HTML
    return render_template('liked.html', liked_titles=liked_titles)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Récupérer les données du formulaire soumises par l'utilisateur
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Vérifier que les deux mots de passe entrés correspondent
        if password != confirm_password:
            flash('Les mots de passe ne correspondent pas.')
            return redirect('/signup')

        # Se connecter à la base de données
        conn = sqlite3.connect('database/spotifaux.db')

        # Insérer le nouvel utilisateur dans la table USER_USR
        conn.execute('INSERT INTO USER_USR (USR_USERNAME, USR_MAIL, USR_PASSWORD) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()

        # Fermer la connexion à la base de données
        conn.close()

        # Rediriger l'utilisateur vers la page de connexion
        flash('Vous êtes maintenant inscrit ! Veuillez vous connecter.')
        return redirect('/login')

    # Si la méthode HTTP est GET, afficher la page HTML du formulaire d'inscription
    return render_template('signup.html')

