from employee import Employee 
from junior_developer import JuniorDeveloper as jun_dev
from mid_level_developer import MidLevelDeveloper 
from senior_developer import SeniorDeveloper 
from lead_developer import LeadDeveloper 

lista_jun_devs = [jun_dev("Tiago Dias", 1800, 10)]

while True:
    nome = input("Digite o nome do desenvolvedor (ou 'continuar' para Imprimir salários): ")
    
    if nome.lower() == "continuar":
        break
    
    try:
        salario = float(input("Digite o salário: "))
        horas_trabalhadas = float(input("Digite o total de horas trabalhadas: "))
    
        # Crie o objeto JuniorDeveloper com os dados fornecidos
        novo_jun_dev = jun_dev(nome, salario, horas_trabalhadas)
    
        # Adicione o objeto à lista
        lista_jun_devs.append(novo_jun_dev)
    except:
        print("Formato Inválido!")

for jun_dev in lista_jun_devs:
    calculo_salario_total = jun_dev.calculate_pay()
    print(f"Salário total para {jun_dev.name}: R${calculo_salario_total:.2f}")
