import sqlite3 as conector

try:

    # Abrindo conexão e aquisição de cursor
    conexao = conector.connect('./meu_banco.db')
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    deletar = '''DELETE FROM pessoa WHERE cpf =10000000009;'''
    cursor.execute(deletar)

    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()
