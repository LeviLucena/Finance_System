from create_tables import create_tables
from load_data import load_all_data

def main():
    create_tables()
    load_all_data()
    print("Banco criado e dados carregados com sucesso.")

if __name__ == "__main__":
    main()
