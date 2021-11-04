import sqlite3 as conector

try:

    # Abrindo conexão e aquisição de cursor
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()

    # Executando comando SELECT...CREATE
    inserir = """INSERT INTO  pessoa(cpf,nome,nascimento, oculos) 
                    VALUES(12345678911,'joão','2000-01-31',1);"""

    cursor.execute(inserir)
    # Efetivando o comando no BD

    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()
