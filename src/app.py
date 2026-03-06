from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.join("..", "templates"))

@app.route("/login", methods=["GET", "POST"])
def login():

    mensaje = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "":
            mensaje = "El campo de usuario esta vacio"

        elif password == "":
            mensaje = "El campo de password esta vacio"

        elif username == "admin" and password == "123456":
            return "Dashboard"

        else:
            mensaje = "Credenciales incorrectas"

    return render_template("login.html", mensaje=mensaje)



if __name__ == "__main__":
    app.run(debug=True)