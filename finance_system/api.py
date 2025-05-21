from flask import Flask, jsonify
from app.api.report_routes import report_api
import sqlite3
import os

app = Flask(__name__)
app.register_blueprint(report_api)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, 'database', 'finance.db')

# Utilitário para executar SELECTs
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # Permite acessar os dados como dicionário
    cur = conn.cursor()
    cur.execute(query, args)
    results = cur.fetchall()
    conn.close()
    return [dict(row) for row in results] if not one else dict(results[0]) if results else {}

# Rota de status
@app.route('/')
def index():
    return jsonify({'mensagem': 'API Financeira está rodando com sucesso 🚀'})

# Rota de lucro por empresa
@app.route('/empresas/lucro')
def empresas_lucro():
    query = """
    SELECT 
        e.nome_fantasia,
        IFNULL(SUM(r.valor), 0) - IFNULL(SUM(d.valor), 0) AS lucro
    FROM empresas e
    LEFT JOIN receitas r ON r.id_empresa = e.id_empresa
    LEFT JOIN despesas d ON d.id_empresa = e.id_empresa
    GROUP BY e.id_empresa
    ORDER BY lucro DESC;
    """
    data = query_db(query)
    return jsonify(data)

# Rota dos top clientes por receita
@app.route('/clientes/top')
def top_clientes():
    query = """
    SELECT 
        c.nome, 
        SUM(r.valor) AS total_receita
    FROM clientes c
    JOIN receitas r ON r.id_cliente = c.id_cliente
    GROUP BY c.id_cliente
    ORDER BY total_receita DESC
    LIMIT 10;
    """
    data = query_db(query)
    return jsonify(data)

# Rota de status dos orçamentos
@app.route('/orcamentos/status')
def orcamentos_status():
    query = """
    SELECT 
        e.nome_fantasia, 
        o.ano, 
        o.mes, 
        o.tipo, 
        o.valor_estimado,
        SUM(CASE 
            WHEN o.tipo = 'receita' THEN IFNULL(r.valor, 0) 
            WHEN o.tipo = 'despesa' THEN IFNULL(d.valor, 0) 
            ELSE 0 
        END) AS realizado
    FROM orcamentos o
    LEFT JOIN empresas e ON e.id_empresa = o.id_empresa
    LEFT JOIN receitas r ON r.id_empresa = o.id_empresa 
        AND strftime('%Y-%m', r.data) = printf('%04d-%02d', o.ano, o.mes)
    LEFT JOIN despesas d ON d.id_empresa = o.id_empresa 
        AND strftime('%Y-%m', d.data) = printf('%04d-%02d', o.ano, o.mes)
    GROUP BY o.id_orcamento;
    """
    data = query_db(query)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
