# Estudos de Banco de dados com Python
import sqlite3 as conector

try:

    # Abrindo conexão e aquisição de cursor
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()
    comando01 = """CREATE TABLE pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    ); """
    comando02 = """CREATE TABLE veiculo(
                    placa CHARACTERE(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    motor REAL NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY(placa),
                    FOREIGN KEY (proprietario) REFERENCES pessoa(cpf),
                    FOREIGN KEY (marca) REFERENCES marca(id)
                    );"""
    cursor.execute(comando01)
    cursor.execute(comando02)
    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()
