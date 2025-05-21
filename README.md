<p align="center">
  <!-- Linguagem principal -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Badge" />
  </a>

  <!-- Framework web -->
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask Badge" />
  </a>

  <!-- CORS -->
  <a href="https://flask-cors.readthedocs.io/en/latest/">
    <img src="https://img.shields.io/badge/-Flask--CORS-00A1E0?style=flat-square&logo=flask&logoColor=white" alt="Flask-CORS Badge" />
  </a>

  <!-- Banco de dados -->
  <a href="https://www.sqlite.org/index.html">
    <img src="https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite Badge" />
  </a>

  <!-- Bibliotecas de dados -->
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas Badge" />
  </a>

  <!-- Visualização -->
  <a href="https://powerbi.microsoft.com/">
    <img src="https://img.shields.io/badge/-Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black" alt="Power BI Badge" />
  </a>

  <!-- Dados -->
  <a href="https://en.wikipedia.org/wiki/Comma-separated_values">
    <img src="https://img.shields.io/badge/-CSV%20Files-FF8800?style=flat-square&logo=files&logoColor=white" alt="CSV Badge" />
  </a>

  <!-- Status -->
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square" alt="Status Badge" />
</p>


![Gemini_Generated_Image_tc0wb6tc0wb6tc0w](https://github.com/user-attachments/assets/a162d751-2eb5-4b20-8a20-64e511b2c687)
## 💰 Sistema de Análise Financeira com API + Power BI

Este projeto é uma solução completa para controle, análise e visualização de dados financeiros empresariais. Ele envolve:

- Banco de dados relacional com dados de clientes, empresas, receitas, despesas, transferências e orçamentos.
- Exposição de dados via API Flask para integração ou consumo externo.
- Visualização com Power BI.

## 🧠 Funcionalidades
🔍 Análise de Dados Financeiros
- Receitas, despesas e lucro por empresa
- Orçamentos: planejado vs. realizado
- Clientes com maior receita gerada
- Visualizações integradas via Power BI

## 🌐 API RESTful com Flask
- Exposição de dados para consumo externo (dashboards, integrações, análises)

## 🖥️ Banco de Dados (SQLite)
As principais tabelas do banco:

- empresas(id_empresa,nome_fantasia,cnpj,data_fundacao)
- clientes(id_cliente,nome,email,cpf)
- receitas(id_receita,id_empresa,id_cliente,categoria,valor,data,descricao)
- despesas(id_despesa,id_empresa,id_cliente,categoria,valor,data,descricao) 
- transferencias(id_transferencia,id_empresa_origem,id_empresa_destino,tipo,valor,data,descricao)
- orcamentos(id_orcamento,id_empresa,ano,mes,tipo,valor_estimado)
- Relacionamentos corretamente definidos (e utilizados no Power BI).

## 📦 Exportação de Dados para BI
Utilize o Script Python no BI para extração de dados do banco SQLite e disponibilização para ferramentas de BI.
```bash
import sqlite3
import pandas as pd

# Configuração do caminho do banco de dados
db_path = r"C:\Users\"informe o caminho"\database\finance.db"

# Para trazer outras tabelas basta repetir o processo e alterar o nome "clientes" para o nome da tabela que pretende exportar.
# Conexão com o banco e extração dos dados
conn = sqlite3.connect(db_path)
query = "SELECT * FROM clientes" 
df = pd.read_sql_query(query, conn)
conn.close()

# Visualização dos dados (opcional)
print(df)
```

## 📊 Power BI Dashboard
Relatório interativo em dashboard.pbix, com:
- Visão geral de desempenho das empresas
- Comparativo orçado x realizado
- Transferências entre empresas: fluxo de capital (quem envia e quem recebe mais)
- Desempenho por cliente: ranking dos maiores clientes por receita gerada

## 📁 Estrutura do Projeto
```bash
finance_system/
├── app/
│   └── api/
│       ├── report_routes.py         # Endpoints da API (lucro, top clientes, orçamentos)
│       └── __init__.py              # Inicialização opcional do módulo Flask
├── data/
│   ├── clientes.csv
│   ├── despesas.csv
│   ├── empresas.csv
│   ├── receitas.csv
│   └── transferencias.csv          # Arquivos CSV com dados brutos
├── database/
│   └── finance.db                   # Banco de dados SQLite
├── exportados/                      # Pasta para arquivos gerados/exportados
├── scripts/
│   ├── create_tables.py             # Criação das tabelas no SQLite
│   ├── load_data.py                 # Carregamento dos dados CSV no banco
│   ├── main.py                      # Execução geral dos scripts
│   └── transform_utils.py           # Funções auxiliares de ETL
├── api.py                           # Inicialização da API Flask
├── check_db.py                      # Verificação da conexão e dados no DB
├── dashboard.pbix                   # Relatório Power BI
├── requirements.txt                 # Dependências Python
└── README.md                        # Documentação

```

## 🔌 API de Relatórios (Flask)
✅ Como executar
1. Crie e carregue o banco de dados:
```bash
python scripts/create_tables.py
python scripts/load_data.py
```

2. Inicie o servidor Flask:
```bash
python api.py
```

3. Acesse em:
📍 http://localhost:5000

## 🌐 Endpoints disponíveis

| Método | Rota                  | Descrição                                                                                     |
|--------|-----------------------|-----------------------------------------------------------------------------------------------|
| GET    | `/empresas/lucro`     | Retorna o lucro por empresa (receitas - despesas)                                             |
| GET    | `/clientes/top`       | Retorna os 10 clientes com maior volume de receita                                            |
| GET    | `/orcamentos/status`  | Compara orçado x realizado por empresa/mês/ano e tipo (receita ou despesa)                    |

## 🔍 Exemplos de Requisição
✅ Empresas com maior lucro:
```bash
GET http://localhost:5000/empresas/lucro
```
✅ Top 10 Clientes:
```bash
GET http://localhost:5000/clientes/top
```
✅ Comparativo orçado x realizado:
```bash
GET http://localhost:5000/orcamentos/status
```

## 📷 Capturas de Tela
| | | |
|-|-|-|
| ![image](https://github.com/user-attachments/assets/abcfab59-2b99-4c36-9621-0cb3f5764f55) | ![image](https://github.com/user-attachments/assets/43a7d218-9825-4c17-96f9-74dff2e8e7fc) | ![image](https://github.com/user-attachments/assets/50f74c0a-45f9-43ab-a771-68919c6a214b) |


## ⚙️ Requisitos
- Python 3.9+
- SQLite
- Power BI Desktop

Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📌 Observações
- Os dados usados são fictícios para fins educacionais.
- Pode ser facilmente adaptado para uso com PostgreSQL, MySQL ou outro SGBD.
- A API pode ser integrada a ferramentas externas ou serviços web.

## 📬 Contato
- Projeto desenvolvido para fins educacionais.
- Dúvidas ou sugestões? Sinta-se à vontade para entrar em contato!
