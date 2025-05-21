import sqlite3
import pandas as pd
import os

# Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database', 'finance.db')
DATA_DIR = os.path.join(BASE_DIR, 'data')

print("Criando banco em:", DB_PATH)

# Função para carregar um CSV no banco
def load_csv_to_db(csv_file, table_name, parse_dates=None):
    path = os.path.join(DATA_DIR, csv_file)
    print(f"🔄 Carregando '{table_name}' de {path}...")

    df = pd.read_csv(path, parse_dates=parse_dates, dayfirst=False)

    # Limpeza básica
    df.columns = [col.strip().lower() for col in df.columns]  # nomes em minúsculas
    df = df.where(pd.notnull(df), None)  # substitui NaN por None

    # Correção de tipo de valor monetário
    if 'valor' in df.columns:
        df['valor'] = df['valor'].astype(float)
    if 'valor_estimado' in df.columns:
        df['valor_estimado'] = df['valor_estimado'].astype(float)

    # Conecta ao banco
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()

    print(f"✅ Tabela '{table_name}' populada com {len(df)} registros.")

def main():
    load_csv_to_db('empresas.csv', 'empresas', parse_dates=['data_fundacao'])
    load_csv_to_db('clientes.csv', 'clientes')
    load_csv_to_db('receitas.csv', 'receitas', parse_dates=['data'])
    load_csv_to_db('despesas.csv', 'despesas', parse_dates=['data'])
    load_csv_to_db('orcamentos.csv', 'orcamentos')  # 'ano' e 'mes' são numéricos
    load_csv_to_db('transferencias.csv', 'transferencias', parse_dates=['data'])

if __name__ == "__main__":
    main()
