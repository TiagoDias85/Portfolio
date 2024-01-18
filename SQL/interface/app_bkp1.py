from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect('treino-1.db')

# Função para criar as tabelas se não existirem
def criar_tabelas():
    with conectar_bd() as conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                ID INTEGER PRIMARY KEY,
                Nome TEXT,
                Idade INTEGER,
                Email TEXT UNIQUE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS DadosPessoais (
                ClienteID INTEGER PRIMARY KEY,
                Endereco TEXT,
                Telefone TEXT,
                FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS HistoricoCompras (
                CompraID INTEGER PRIMARY KEY,
                ClienteID INTEGER,
                Produto TEXT,
                Valor DECIMAL(10, 2),
                DataCompra TEXT,
                FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
            )
        ''')
        conn.commit()

# Rota principal, exibe a lista de clientes
@app.route('/')
def index():
    # Chama a função para criar as tabelas
    criar_tabelas()

    return render_template('index.html')

# Rota para pesquisar cliente
@app.route('/pesquisar_cliente', methods=['POST'])
def pesquisar_cliente():
    nome_pesquisa = request.form['nome']

    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Clientes WHERE Nome LIKE ?', (f'%{nome_pesquisa}%',))
        clientes = cursor.fetchall()

    return render_template('resultados_pesquisa.html', clientes=clientes)

if __name__ == "__main__":
    app.run(debug=True)
