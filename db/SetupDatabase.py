import sqlite3

try:
    # Conectar ao banco de dados
    conn = sqlite3.connect('database/database.db')

    # Criar um cursor
    cursor = conn.cursor()

    # Criar uma tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUTOS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo INTEGER NOT NULL,
            descricao TEXT NOT NULL,
            fornecedor TEXT NOT NULL,
            custo FLOAT NOT NULL
        )
    ''')

    # Inserir dados
    # cursor.execute('''
    #     INSERT INTO USERS (user, nome, senha, nivel, acesso)
    #     VALUES (?, ?, ?, ?, ?)
    # ''', ("lucas.batista", "Lucas Duarte Batista", "mega123", 1 ,"10/09/2024"))

    # cursor.execute('''
    #     INSERT INTO usuarios (nome, idade)
    #     VALUES (?, ?)
    # ''', ('Maria Oliveira', 25))

    # Salvar as mudanças
    # conn.commit()

except sqlite3.Error as e:
    print(f"Erro ao operar com o banco de dados: {e}")

finally:
    # Fechar a conexão
    if conn:
        conn.close()
