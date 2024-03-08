import csv
import random
from datetime import datetime, timedelta

# Definir os produtos disponíveis e clientes
produtos = ['Produto_A', 'Produto_B', 'Produto_C']
clientes = []

# Gerando 100 Clientes Fictícios 

for i in range(1, 101):
    novo_cliente = f'Cliente_{i}'
    clientes.append(novo_cliente)

# Definir o número de registros de vendas
num_de_vendas = 500

# Definir a faixa de datas para as vendas (últimos 6 meses)
start_date = datetime.now() - timedelta(days=180)
end_date = datetime.now()

# Gerar registros de vendas aleatórios
registro_vendas = []
for _ in range(num_de_vendas):
    data = start_date + timedelta(days=random.randint(0, 180))
    produto = random.choice(produtos)
    preço = random.randint(50, 1000)
    cliente = random.choice(clientes)
    registro_vendas.append([data.strftime('%Y-%m-%d'), produto, preço, cliente])

# Escrever os registros de vendas no arquivo CSV
with open('Registro_Vendas.csv', 'w', newline='') as banco_dados:
    writer = csv.writer(banco_dados)
    writer.writerow(['Data', 'Produto', 'Price', 'Cliente'])
    writer.writerows(registro_vendas)

print("Arquivo CSV 'Registro_Vendas.csv' gerado com sucesso!")
