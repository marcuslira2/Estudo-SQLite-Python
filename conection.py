# Estudos de Banco de dados com Python
import sqlite3 as conector

try:

    # Abrindo conexão e aquisição de cursor
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()
