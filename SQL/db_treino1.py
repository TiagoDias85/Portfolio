import sqlite3
from faker import Faker
from sqlite3 import dbapi2 as sqlite
sqlite.enable_callback_tracebacks(True)

# Criar um banco de dados SQLite e uma tabela Clientes
conn = sqlite3.connect('treino-1.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        ID INTEGER PRIMARY KEY,
        Nome TEXT,
        Idade INTEGER,
        Email TEXT UNIQUE
    )
''')

# Adicionar dados aleatórios à tabela Clientes
fake = Faker()
for _ in range(100):
    nome = fake.name()
    idade = fake.random_int(min=18, max=80)
    email = fake.email()
    cursor.execute('INSERT INTO Clientes (Nome, Idade, Email) VALUES (?, ?, ?)', (nome, idade, email))

# Criar tabela DadosPessoais
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DadosPessoais (
        ClienteID INTEGER PRIMARY KEY,
        Endereco TEXT,
        Telefone TEXT,
        FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
    )
''')

# Adicionar dados aleatórios à tabela DadosPessoais
for cliente_id in range(1, 101):
    endereco = fake.address()
    telefone = fake.phone_number()
    cursor.execute('INSERT OR REPLACE INTO DadosPessoais (ClienteID, Endereco, Telefone) VALUES (?, ?, ?)',
                   (cliente_id, endereco, telefone))

# Criar tabela HistoricoCompras
cursor.execute('''
    CREATE TABLE IF NOT EXISTS HistoricoCompras (
        CompraID INTEGER PRIMARY KEY,
        ClienteID INTEGER,
        Produto TEXT,
        Valor DECIMAL(10, 2),
        DataCompra TEXT,  -- Vamos armazenar a data como uma string
        FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
    )
''')

# Adicionar dados aleatórios à tabela HistoricoCompras
for cliente_id in range(1, 101):
    produto = fake.word()
    valor = fake.random_int(min=10, max=100)
    data_compra = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
    cursor.execute('INSERT INTO HistoricoCompras (ClienteID, Produto, Valor, DataCompra) VALUES (?, ?, ?, ?)',
                   (cliente_id, produto, valor, data_compra))

# Commit para salvar as alterações no banco de dados
conn.commit()

# Fechando a conexão com o banco de dados
conn.close()
