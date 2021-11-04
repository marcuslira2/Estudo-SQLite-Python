import sqlite3 as conector
from modelo import Pessoa

try:

    # Abrindo conexão e aquisição de cursor
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()

    #Criando um objeto do tipo Pessoa
    pessoa = Pessoa(10000000008,'marcus','1996-10-06',False)

    # Executando um comando com query e parameter
    inserir = """INSERT INTO  pessoa(cpf,nome,nascimento, oculos) VALUES(?,?,?,?);"""

    cursor.execute(inserir,(pessoa.cpf,pessoa.nome,pessoa.data_nascimento,pessoa.usa_oculos))
    # Efetivando o comando no BD

    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()
