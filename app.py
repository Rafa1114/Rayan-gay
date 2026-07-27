from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
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

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute(
        "INSERT INTO objetos (nome, descricao, qtd, preco) VALUES (%s, %s, %s, %s)",
        (nome, descricao, qtd, preco)
    )

    cursor.execute(
        "INSERT INTO historico (nome, tipo, quantidade) VALUES (%s, %s, %s)",
        (nome, "Entrada", qtd)
    )

    banco.commit()

    cursor.close()
    banco.close()

    return redirect("/paginadonovoitem")

@app.route("/excluir_todos")
def excluir_todos():

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("DELETE FROM objetos")

    banco.commit()

    cursor.close()
    banco.close()

    return redirect("/paginaconsulta")

@app.route("/excluir/<id>")
def excluir(id):

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("SELECT nome, qtd FROM objetos WHERE id = %s", (id,))
    objeto = cursor.fetchone()

    cursor.execute(
        "INSERT INTO historico (nome, tipo, quantidade) VALUES (%s, %s, %s)",
        (objeto[0], "Saída", objeto[1])
    )

    cursor.execute("DELETE FROM objetos WHERE id = %s", (id,))

    banco.commit()

    cursor.close()
    banco.close()

    return redirect("/paginaconsulta")

# historico
@app.route("/historico")
def historico():

    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM historico")

    historico = cursor.fetchall()

    cursor.close()
    banco.close()

    return render_template("historico.html", historico=historico)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)