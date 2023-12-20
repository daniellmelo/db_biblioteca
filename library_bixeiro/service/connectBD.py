import mysql.connector
import sys

# Configuração do banco de dados

def getDB():
    try:
        db_conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='bumbersplash',
            database='projetoBD',
        )
        return db_conexao
    
    except mysql.connector.Error as erro:
        print(f'Erro connection com o BANCO DE DADOS: {erro}')
        sys.exit(1)
