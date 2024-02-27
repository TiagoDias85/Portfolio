from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect('treino-1.db')

# Rota principal, exibe a lista de clientes
@app.route('/')
def index():
    # Consulta todos os clientes
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Clientes')
        clientes = cursor.fetchall()
    return render_template('index.html', clientes=clientes)

# Rota para adicionar um novo cliente
@app.route('/adicionar_cliente', methods=['POST'])
def adicionar_cliente():
    nome = request.form['nome']
    idade = int(request.form['idade'])
    email = request.form['email']

    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Clientes (Nome, Idade, Email) VALUES (?, ?, ?)', (nome, idade, email))
        conn.commit()

    return redirect(url_for('index'))

# Rota para remover um cliente
@app.route('/remover_cliente/<int:cliente_id>')
def remover_cliente(cliente_id):
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Clientes WHERE ID = ?', (cliente_id,))
        conn.commit()

    return redirect(url_for('index'))

# Rota para exibir as vendas de um cliente e permitir a adição e remoção de vendas
@app.route('/cliente/<int:cliente_id>', methods=['GET', 'POST'])
def detalhes_cliente(cliente_id):
    with conectar_bd() as conn:
        cursor = conn.cursor()

        # Consulta informações do cliente
        cursor.execute('SELECT * FROM Clientes WHERE ID = ?', (cliente_id,))
        cliente = cursor.fetchone()

        # Consulta histórico de compras do cliente
        cursor.execute('SELECT * FROM HistoricoCompras WHERE ClienteID = ?', (cliente_id,))
        historico_compras = cursor.fetchall()

        if request.method == 'POST':
            # Adiciona uma nova venda
            produto = request.form['produto']
            valor = float(request.form['valor'])
            data_compra = request.form['data_compra']

            cursor.execute('INSERT INTO HistoricoCompras (ClienteID, Produto, Valor, DataCompra) VALUES (?, ?, ?, ?)',
                           (cliente_id, produto, valor, data_compra))
            conn.commit()

    return render_template('detalhes_cliente.html', cliente=cliente, historico_compras=historico_compras)

# Rota para remover uma venda
@app.route('/remover_venda/<int:venda_id>')
def remover_venda(venda_id):
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM HistoricoCompras WHERE CompraID = ?', (venda_id,))
        conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
