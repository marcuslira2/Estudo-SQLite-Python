# Estudos de Banco de dados com Python
import sqlite3 as conector

try:

    #Abrindo conexão e aquisição de cursor
    conexao = conector.connect('meu_banco.db')
    cursor = conexao.cursor()
    comando = """CREATE TABLE pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculus BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    ); """

    cursor.execute(comando)
    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()
