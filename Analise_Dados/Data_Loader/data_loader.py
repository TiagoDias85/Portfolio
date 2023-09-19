import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Solicitar o nome do arquivo SQLite
    db_name = input("Digite o nome do arquivo SQLite para abrir: ")

    # Conectar ao banco de dados
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Listar tabelas disponíveis no banco de dados
    tables = get_tables(cursor)
    print("Tabelas disponíveis:", tables)

    # Solicitar o tipo de tabela
    table_name = input("Digite o nome da tabela que deseja puxar: ")

    # Listar colunas da tabela escolhida
    columns = get_columns(cursor, table_name)
    print("Colunas disponíveis:", columns)

    # Solicitar a coluna que deseja puxar
    column_name = input("Digite o nome da coluna que deseja puxar: ")

    # Realizar consulta no banco de dados
    data = fetch_data(cursor, table_name, column_name)

    # Opções de análise de dados
    analysis_options = [
        "1. Média",
        "2. Mediana",
        "3. Desvio Padrão",
        "4. Histograma",
      
    ]

    # Listar opções de análise
    for option in analysis_options:
        print(option)

    # Solicitar opção de análise
    analysis_choice = int(input("Escolha o número da análise que deseja realizar: "))

    # Executar a análise escolhida
    if analysis_choice == 1:
        calculate_mean(data)
    elif analysis_choice == 2:
        calculate_median(data)
    elif analysis_choice == 3:
        calculate_std_dev(data)
    elif analysis_choice == 4:
        plot_histogram(data)
    # Adicione mais opções de análise aqui

    conn.close()

def get_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    return tables

def get_columns(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = [column[1] for column in cursor.fetchall()]
    return columns

def fetch_data(cursor, table_name, column_name):
    cursor.execute(f"SELECT {column_name} FROM {table_name};")
    data = [row[0] for row in cursor.fetchall()]
    return data

def calculate_mean(data):
    mean = sum(data) / len(data)
    print("Média:", mean)

def calculate_median(data):
    median = sorted(data)[len(data) // 2]
    print("Mediana:", median)

def calculate_std_dev(data):
    std_dev = pd.Series(data).std()
    print("Desvio Padrão:", std_dev)

def plot_histogram(data):
    plt.hist(data, bins=10, edgecolor='black')
    plt.xlabel("Valores")
    plt.ylabel("Frequência")
    plt.title("Histograma")
    plt.show()

if __name__ == "__main__":
    main()
