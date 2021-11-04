import sqlite3 as conector

from modelo import Marca, Veiculo

try:

    # Abrindo conexão e aquisição de cursor
    conexao = conector.connect('./meu_banco.db')
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # Inserir dados na table Marca
    inserir_marca = """INSERT INTO marca (nome,sigla) VALUES (:nome,:sigla);"""

    marca1 = Marca("Marca A", "MA")
    cursor.execute(inserir_marca, vars(marca1))
    marca1.id = cursor.lastrowid

    marca2 = Marca("Marca B", "MB")
    cursor.execute(inserir_marca, vars(marca2))
    marca2.id = cursor.lastrowid

    # Inserir na table veiculo
    inserir_veiculo = """INSERT INTO veiculo VALUES (:placa,:ano,:cor,:motor,:proprietario,:marca);"""

    veiculo1 = Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000009, marca1.id)
    veiculo2 = Veiculo("AAA0002", 2003, "Preto", 1.8, 10000000008, marca2.id)
    veiculo3 = Veiculo("AAA0003", 2006, "Branco", 1.4, 10000000009, marca1.id)
    veiculo4 = Veiculo("AAA0004", 2002, "Vermelho", 2.0, 10000000009, marca2.id)
    veiculo5 = Veiculo("AAA0005", 2009, "Azul", 1.6, 10000000009, marca1.id)

    cursor.execute(inserir_veiculo, vars(veiculo1))
    cursor.execute(inserir_veiculo, vars(veiculo2))
    cursor.execute(inserir_veiculo, vars(veiculo3))
    cursor.execute(inserir_veiculo, vars(veiculo4))
    cursor.execute(inserir_veiculo, vars(veiculo5))

    # Efetivando o comando no BD

    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento de conexão
    if conexao:
        cursor.close()
        conexao.close()
