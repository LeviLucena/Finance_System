from flask import Blueprint, jsonify
import sqlite3
import os

report_api = Blueprint('report_api', __name__)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "database", "finance.db"))


def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv


@report_api.route("/empresas/lucro", methods=["GET"])
def empresas_lucro():
    query = """
        SELECT 
            e.id_empresa,
            e.nome_fantasia,
            IFNULL(SUM(r.valor), 0) AS total_receita,
            IFNULL(SUM(d.valor), 0) AS total_despesa,
            IFNULL(SUM(r.valor), 0) - IFNULL(SUM(d.valor), 0) AS lucro
        FROM empresas e
        LEFT JOIN receitas r ON e.id_empresa = r.id_empresa
        LEFT JOIN despesas d ON e.id_empresa = d.id_empresa
        GROUP BY e.id_empresa
        ORDER BY lucro DESC
    """
    data = query_db(query)
    return jsonify([dict(row) for row in data])


@report_api.route("/clientes/top", methods=["GET"])
def clientes_top():
    query = """
        SELECT 
            c.id_cliente,
            c.nome,
            c.email,
            SUM(r.valor) AS total_receita
        FROM clientes c
        JOIN receitas r ON c.id_cliente = r.id_cliente
        GROUP BY c.id_cliente
        ORDER BY total_receita DESC
        LIMIT 10
    """
    data = query_db(query)
    return jsonify([dict(row) for row in data])


@report_api.route("/orcamentos/status", methods=["GET"])
def orcamentos_status():
    query = """
        SELECT 
            o.id_empresa,
            e.nome_fantasia,
            o.ano,
            o.mes,
            o.tipo,
            SUM(o.valor_estimado) AS valor_orcado,
            CASE 
                WHEN o.tipo = 'Receita' THEN (
                    SELECT SUM(valor) FROM receitas 
                    WHERE receitas.id_empresa = o.id_empresa 
                    AND strftime('%Y', data) = CAST(o.ano AS TEXT) 
                    AND strftime('%m', data) = printf('%02d', o.mes)
                )
                WHEN o.tipo = 'Despesa' THEN (
                    SELECT SUM(valor) FROM despesas 
                    WHERE despesas.id_empresa = o.id_empresa 
                    AND strftime('%Y', data) = CAST(o.ano AS TEXT) 
                    AND strftime('%m', data) = printf('%02d', o.mes)
                )
            END AS valor_realizado
        FROM orcamentos o
        JOIN empresas e ON o.id_empresa = e.id_empresa
        GROUP BY o.id_empresa, o.ano, o.mes, o.tipo
        ORDER BY o.ano DESC, o.mes DESC
    """
    data = query_db(query)
    return jsonify([dict(row) for row in data])
