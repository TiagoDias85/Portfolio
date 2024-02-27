# Projeto de Gerenciamento de Salários em Python

## Descrição

Este projeto exemplifica a utilização de **classes** em arquivos separados para implementar a **orientação a objetos** em Python. O objetivo principal é calcular os salários de colaboradores de TI, organizados em diferentes hierarquias, e gerar uma planilha Excel (.xlsx) com os resultados.

## Estrutura do Projeto

O projeto é composto por cinco classes principais, cada uma representando uma hierarquia de desenvolvedor:

- **Employee**: Classe base para todos os desenvolvedores.
- **JuniorDeveloper**: Classe para desenvolvedores juniores.
- **MidLevelDeveloper**: Classe para desenvolvedores de nível intermediário.
- **SeniorDeveloper**: Classe para desenvolvedores seniores.
- **LeadDeveloper**: Classe para líderes de equipe.

As instâncias dessas classes são utilizadas para armazenar e calcular salários com base nas horas trabalhadas.

## Utilização

O script principal (`main.py`) demonstra como criar instâncias das classes, coletar dados do usuário e gerar uma planilha Excel. O script utiliza a biblioteca `openpyxl` para manipulação de planilhas.

### Execução do Script

```bash
python main.py

 Execução do Script
Ao executar o script, você será solicitado a inserir informações sobre os desenvolvedores, como nome, salário e horas trabalhadas. Para finalizar a entrada de dados e gerar a planilha, basta inserir continuar quando solicitado pelo nome do desenvolvedor.

Exemplo de Saída
A saída do script inclui a impressão dos salários individuais dos desenvolvedores no console e a criação de uma planilha Excel chamada employee_data.xlsx.

Requisitos
Python 3.x
Biblioteca openpyxl (instalável via pip install openpyxl)
Contribuições
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou adição de novas funcionalidades. Abra uma issue para discussão ou envie um pull request.

Autor
Seu Nome
Seu Email