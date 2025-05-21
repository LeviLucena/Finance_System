import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # pasta finance_system
DB = os.path.join(BASE_DIR, 'database', 'finance.db')
print("Criando banco em:", DB)

def create_tables():
    print(">>> Entrou na função create_tables()")
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT,
        cpf TEXT
    );

    CREATE TABLE IF NOT EXISTS empresas (
        id_empresa INTEGER PRIMARY KEY,
        nome_fantasia TEXT,
        cnpj TEXT,
        data_fundacao DATE
    );

    CREATE TABLE IF NOT EXISTS receitas (
        id_receita INTEGER PRIMARY KEY,
        id_empresa INTEGER,
        id_cliente INTEGER,
        categoria TEXT,
        valor REAL,
        data DATE,
        descricao TEXT,
        FOREIGN KEY(id_empresa) REFERENCES empresas(id_empresa),
        FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
    );

    CREATE TABLE IF NOT EXISTS despesas (
        id_despesa INTEGER PRIMARY KEY,
        id_empresa INTEGER,
        id_cliente INTEGER,
        categoria TEXT,
        valor REAL,
        data DATE,
        descricao TEXT,
        FOREIGN KEY(id_empresa) REFERENCES empresas(id_empresa),
        FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
    );

    CREATE TABLE IF NOT EXISTS orcamentos (
        id_orcamento INTEGER PRIMARY KEY,
        id_empresa INTEGER,
        ano INTEGER,
        mes INTEGER,
        tipo TEXT,
        valor_estimado REAL,
        FOREIGN KEY(id_empresa) REFERENCES empresas(id_empresa)
    );

    CREATE TABLE IF NOT EXISTS transferencias (
        id_transferencia INTEGER PRIMARY KEY,
        id_empresa_origem INTEGER,
        id_empresa_destino INTEGER,
        tipo TEXT,
        valor REAL,
        data DATE,
        descricao TEXT,
        FOREIGN KEY(id_empresa_origem) REFERENCES empresas(id_empresa),
        FOREIGN KEY(id_empresa_destino) REFERENCES empresas(id_empresa)
    );
    """)

    conn.commit()

    # Verificar tabelas criadas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tabelas criadas:", [t[0] for t in tables])

    conn.close()

# ✅ Aqui fora da função!
if __name__ == "__main__":
    create_tables()
