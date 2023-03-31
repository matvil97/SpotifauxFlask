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

app = Flask("Spotifaux", static_folder='templates', static_url_path='/templates')

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
        cursor = conn.execute(
            "SELECT TTL.*, CASE WHEN LUS.ID_TTL IS NOT NULL THEN 1 ELSE 0 END AS TTL_LIKED FROM TITLE_TTL TTL LEFT JOIN (SELECT ID_TTL FROM LIKE_USER_LUS WHERE ID_USR = ?) LUS ON TTL.ID_TTL = LUS.ID_TTL;",
            (session["ID_USR"],),
        )
        titles = cursor.fetchall()

        # close the connection to the database
        conn.close()

        # send the result of the SQL query as data name 'titles'
        return render_template("index.html", titles=titles)
    else:
        # redirect to the login page
        return redirect("/login")


# Root - Login form processing


@app.route("/login", methods=["GET", "POST"])
def login_post():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # connect to the database
        conn = sqlite3.connect("database/spotifaux.db")
        # get the data of user by mail send from form
        cursor = conn.execute("SELECT * FROM USER_USR WHERE USR_MAIL = ?", (email,))
        user = cursor.fetchone()

        # if the password send is the same as the result of the query
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
            flash("E-mail ou mot de passe incorrect. Veuillez réessayer")
            return redirect("/login")
    # return the template html page login
    return render_template("login.html")


# Root - Log out feature


@app.route("/logout")
def logout():
    session.clear()
    # redirect to the home page
    return redirect("/")


# Root - Like feature


@app.route("/like/<int:id>")
def like(id):
    # connect to the database
    conn = sqlite3.connect("database/spotifaux.db")

    # insert data into LIKE_USER_LUS table
    cursor = conn.execute(
        "INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (?, ?);",
        (session["ID_USR"], id),
    )
    conn.commit()

    # close the connection to the database
    conn.close()
    return redirect(request.referrer)


# Root - Unlike feature


@app.route("/unlike/<int:id>")
def unlike(id):
    # connect to the database
    conn = sqlite3.connect("database/spotifaux.db")

    # insert data into LIKE_USER_LUS table
    cursor = conn.execute(
        "DELETE FROM LIKE_USER_LUS WHERE ID_USR = ? AND ID_TTL = ?;",
        (session["ID_USR"], id),
    )
    conn.commit()

    # close the connection to the database
    conn.close()
    return redirect(request.referrer)


# Root - Liked title page


@app.route("/liked")
def liked_titles():
    # connect to the database
    conn = sqlite3.connect("database/spotifaux.db")

    # get data from the LIKE_USER_LUS table
    cursor = conn.execute(
        "SELECT LUS.*, TTL.* FROM LIKE_USER_LUS LUS JOIN TITLE_TTL TTL ON LUS.ID_TTL = TTL.ID_TTL WHERE ID_USR = ?",
        (session["ID_USR"],),
    )
    liked_titles = cursor.fetchall()

    # close the connection to the database
    conn.close()

    # send the result of the SQL query as data name 'liked_titles'
    return render_template("liked.html", liked_titles=liked_titles)


# Root - Sign up feature


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # get form data
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # check if the password and the confirm_password are identic
        if password != confirm_password:
            flash("Les mots de passe ne correspondent pas.")
            return redirect("/signup")

        # connect to the database
        conn = sqlite3.connect("database/spotifaux.db")

        # insert new user in USER_USR table
        conn.execute(
            "INSERT INTO USER_USR (USR_USERNAME, USR_MAIL, USR_PASSWORD) VALUES (?, ?, ?)",
            (username, email, password),
        )
        conn.commit()

        # close the connection to the database
        conn.close()

        # redirect to the login page
        flash("Vous êtes maintenant inscrit ! Veuillez vous connecter.")
        return redirect("/login")

    # return the template html page sign up
    return render_template("signup.html")

# Page + Function to add a new music 
@app.route('/add_title', methods=['GET', 'POST'])

def add_title_route():
    if request.method == 'POST':

        # asks for all the information of the music to add
        title_name = request.form['title_name']
        title_artist = request.form['title_artist']
        title_duration = request.form['title_duration']
        title_type = request.form['title_type']
        title_img = request.form['title_img']
        add_title(title_name, title_artist, title_duration, title_type, title_img)
        return redirect("/")
    else:
        return render_template('add_title.html')

def add_title(title_name, title_artist, title_duration, title_type, title_img):

    # connect to the database
    conn = sqlite3.connect('database/spotifaux.db')

    # add the new music in the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES (?, ?, ?, ?, ?)", (title_name, title_artist, title_duration, title_type, title_img))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    app.run(debug=True)