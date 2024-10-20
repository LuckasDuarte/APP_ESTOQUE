import sqlite3
import pandas as pd
import random

# Conectar ao banco de dados (ou criar um novo se não existir)
conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

# Ler o arquivo Excel
produtos_df = pd.read_excel('Produtos.xls')

# Verifique se o DataFrame não está vazio e se tem pelo menos 200 linhas
if produtos_df.empty or len(produtos_df) < 200:
    raise ValueError("O arquivo deve conter pelo menos 200 produtos.")

# Selecionar aleatoriamente 200 itens sem repetição
produtos_aleatorios = produtos_df.sample(n=200, random_state=1)

# Inserir os produtos na tabela ESTOQUE
for _, row in produtos_aleatorios.iterrows():
    quantidade = random.randint(1, 100)  # Gera uma quantidade aleatória entre 1 e 100
    cursor.execute('''
        INSERT INTO ESTOQUE (COD, DESCRICAO, QUANTIDADE, PERECIVEL, VALIDADE, CUSTO) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        row['COD_MEGA'],
        row['DESCRICAO'],
        quantidade,  # Insere a quantidade aleatória
        row['PERECIVEL'],
        None,  # VALIDADE pode ser None se não houver dados no Excel
        row['CUSTO']
    ))

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()

print("200 itens inseridos na tabela ESTOQUE com sucesso!")
