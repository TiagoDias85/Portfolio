#   BRAINSTORM: CRIAR UM PROGRAMA ONDE PELO IMC DA PESSOA O PROGRAMA ENCAMINHA OS DADOS PARA O PROFISSIONAL IDEAL, SENDO:
# PERSONAL TRAINER (1,2,3), PSICÓLOGA,NUTRICIONISTA (1,2,3),

# COLETAR OS DADOS DA PESSOA E CRIAR UM BANCO DE DADOS
# INPUTS, FLOATS, XML
# CALCULAR O IMC, COLETAR DADOS FÍSICOS
# ENCAMINHAR PARA CADA PROFISSIONAL ABRINDO UM HOST COM SOCKET

import xml.etree.ElementTree as ET

# Coletar os dados do usuário
while True:
    nome_user = input("Insira seu nome de usuário: ")

    # Criar o elemento raiz do XML ou carregar o arquivo XML existente
    try:
        tree = ET.parse("dados.xml")
        root = tree.getroot()
    except FileNotFoundError:
        root = ET.Element("Pessoas")
        tree = ET.ElementTree(root)

    # Verificar se o usuário já existe no XML
    usuarios = root.findall(".//Pessoa[Nome='{}']".format(nome_user))
    if len(usuarios) > 0:
        print("Erro: Usuário já existente. Tente novamente.")
    else:
        break

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
idade = float(input("Insira sua idade: "))

# Calcular o IMC
imc = peso / (altura * altura)
print(imc)
print()

if imc <= 18.5:
    print("Você está abaixo do peso ideal, informações repassadas aos nossos profissionais!")
elif imc >= 18.5 and imc <= 24.9:
    print("Você está com o peso ideal, informações repassadas aos nossos profissionais!")
elif imc >= 25 and imc <= 29.9:
    print("Você está com sobrepeso, informações repassadas aos nossos profissionais!")
elif imc >= 30 and imc <= 34.9:
    print("Você está com obesidade grau I, informações repassadas aos nossos profissionais!")
elif imc >= 35 and imc <= 39.9:
    print("Você está com obesidade grau II, informações repassadas aos nossos profissionais!")
elif imc >= 40:
    print("Você está com obesidade grau III (obesidade mórbida), informações repassadas aos nossos profissionais!")

# Criar um novo elemento para a pessoa e adicionar ao elemento raiz
pessoa = ET.SubElement(root, "Pessoa")
ET.SubElement(pessoa, "Nome").text = nome_user
ET.SubElement(pessoa, "Peso").text = str(peso)
ET.SubElement(pessoa, "Altura").text = str(altura)
ET.SubElement(pessoa, "Idade").text = str(idade)
ET.SubElement(pessoa, "IMC").text = str(imc)

# Salvar o XML atualizado em um arquivo
tree.write("dados.xml")
