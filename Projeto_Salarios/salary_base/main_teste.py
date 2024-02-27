from employee import Employee
from junior_developer import JuniorDeveloper as jun_dev
from mid_level_developer import MidLevelDeveloper as mid
from senior_developer import SeniorDeveloper
from lead_developer import LeadDeveloper
import openpyxl

lista_jun_devs = [jun_dev("Tiago Dias", 1800, 10), mid("Gobblert", 1900, 12)]

while True:
    nome = input("Digite o nome do desenvolvedor (ou 'continuar' para imprimir salários): ")

    if nome.lower() == "continuar":
        break

    try:
        salario = float(input("Digite o salário: "))
        horas_trabalhadas = float(input("Digite o total de horas Extra: "))

        # Cria o objeto JuniorDeveloper com os dados fornecidos
        novo_jun_dev = jun_dev(nome, salario, horas_trabalhadas)

        # Adiciona o objeto à lista
        lista_jun_devs.append(novo_jun_dev)
    except ValueError:
        print("Formato Inválido!")

# Imprime salários
for jun_dev in lista_jun_devs:
    calculo_salario_total = jun_dev.calculate_pay()
    print(f"Salário total para {jun_dev.name}: R${calculo_salario_total:.2f}")

# Cria uma nova planilha xlsx
workbook = openpyxl.Workbook()
sheet = workbook.active

# Adiciona cabeçalhos
sheet.append(["Nome", "Salário", "Horas Trabalhadas"])

# Preenche os dados da planilha
for jun_dev in lista_jun_devs:
    sheet.append([jun_dev.name, jun_dev.salary])

# Salva a planilha xlsx
workbook.save("employee_data.xlsx")

print("Planilha Excel criada com sucesso!")
