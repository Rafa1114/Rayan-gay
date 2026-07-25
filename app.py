from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/paginaconsulta")
def paginaconsulta():
    return render_template("paginaconsulta.html")

@app.route("/paginadeentrada")
def paginadeentrada():
    return render_template("paginadeentrada.html")

@app.route("/paginadesaida")
def paginadesaida():
    return render_template("paginadesaida.html")

@app.route("/paginadonovoitem")
def paginadonovoitem():
    return render_template("paginadonovoitem.html")

@app.route("/usuarios") 
def paginadeusuarios():
    return render_template("paginadeusuarios.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)