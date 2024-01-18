from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Adicione uma chave secreta para usar o flash

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

        sql_query = 'SELECT * FROM Clientes WHERE LOWER(Nome) LIKE ?'
        cursor.execute(sql_query, (f'%{nome_pesquisa.lower()}%',))
        clientes = cursor.fetchall()

    return render_template('resultados_pesquisa.html', clientes=clientes)

# Rota para mostrar detalhes do cliente
@app.route('/detalhes_cliente/<int:cliente_id>')
def detalhes_cliente(cliente_id):
    with conectar_bd() as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM Clientes WHERE ID = ?', (cliente_id,))
        cliente = cursor.fetchone()

        cursor.execute('SELECT * FROM DadosPessoais WHERE ClienteID = ?', (cliente_id,))
        dados_pessoais = cursor.fetchone()

        cursor.execute('SELECT * FROM HistoricoCompras WHERE ClienteID = ?', (cliente_id,))
        compras = cursor.fetchall()

    return render_template('detalhes_cliente.html', cliente=cliente, dados_pessoais=dados_pessoais, compras=compras)

# Rota para adicionar compra
@app.route('/adicionar_compra/<int:cliente_id>', methods=['GET', 'POST'])
def adicionar_compra(cliente_id):
    if request.method == 'POST':
        produto = request.form['produto']
        valor = request.form['valor']
        data_compra = request.form['data_compra']

        with conectar_bd() as conn:
            cursor = conn.cursor()

            cursor.execute('INSERT INTO HistoricoCompras (ClienteID, Produto, Valor, DataCompra) VALUES (?, ?, ?, ?)',
                           (cliente_id, produto, valor, data_compra))
            
            conn.commit()
            
            flash('Compra adicionada com sucesso!', 'success')

    return render_template('adicionar_compra.html', cliente_id=cliente_id)

# Rota para remover cliente
@app.route('/remover_cliente/<int:cliente_id>', methods=['GET', 'POST'])
def remover_cliente(cliente_id):
    if request.method == 'POST':
        with conectar_bd() as conn:
            cursor = conn.cursor()

            # Remova o cliente e seus dados pessoais
            cursor.execute('DELETE FROM Clientes WHERE ID = ?', (cliente_id,))
            cursor.execute('DELETE FROM DadosPessoais WHERE ClienteID = ?', (cliente_id,))

            conn.commit()

            flash('Cliente removido com sucesso!', 'success')

            return redirect(url_for('index'))

    return render_template('remover_cliente.html', cliente_id=cliente_id)

if __name__ == "__main__":
    app.run(debug=True)
