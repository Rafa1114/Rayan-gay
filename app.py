from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Amora_321",
        database="trabalho"
    )


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
    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM objetos")
    objetos = cursor.fetchall()

    cursor.close()
    banco.close()

    return render_template("paginaconsulta.html", objetos=objetos)


@app.route("/paginadeentrada")
def paginadeentrada():
    return render_template("paginadeentrada.html")


@app.route("/paginadesaida")
def paginadesaida():
    return render_template("paginadesaida.html")


@app.route("/paginadonovoitem")
def paginadonovoitem():
    return render_template("paginadonovoitem.html")
@app.route("/adicionaritem", methods=["POST"])
def adicionaritem():

    nome = request.form["nome"]
    descricao = request.form["descricao"]
    qtd = request.form["qtd"]
    preco = request.form["preco"]
    imagem = request.form["imagem"]

    banco = conectar()
    cursor = banco.cursor()

    sql = """
    INSERT INTO objetos (nome, descricao, qtd, preco, imagem)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, descricao, qtd, preco, imagem))

    banco.commit()

    cursor.close()
    banco.close()

    from flask import redirect, url_for, flash
    flash("Item adicionado com sucesso!")
return redirect(url_for("paginadonovoitem"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)