import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="trabalho"
)

cursor = banco.cursor()

print("Conectado ao MySQL!")

