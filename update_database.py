import sqlite3 as conector

try:

    # Abrindo conexão e aquisição de cursor
    conexao = conector.connect('./meu_banco.db')
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # Definindo os comandos
    alterar01 = '''UPDATE Pessoa SET oculos = 1; '''
    cursor.execute(alterar01)

    alterar02 = ''' UPDATE Pessoa  SET oculos = ? WHERE cpf = 10000000009;'''
    cursor.execute(alterar02, (False,))

    alterar03 = '''UPDATE Pessoa SET oculos = :usa_oculos WHERE cpf = :cpf;'''
    cursor.execute(alterar03, {"usa_oculos": False, "cpf": 10000000009})


except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()
