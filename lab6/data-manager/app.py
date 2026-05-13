from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Настройки подключения к БД
DB_CONFIG = {
    'dbname': 'currencies_db',   
    'user': 'postgres',          
    'password': 'postgres',      
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/convert', methods=['GET'])
def convert():
    """Конвертирует сумму в рублях по курсу указанной валюты"""
    currency_name = request.args.get('currency')
    amount = request.args.get('amount')

    conn = get_db_connection()
    cur = conn.cursor()

    # Проверяем, существует ли валюта
    cur.execute('SELECT rate FROM currencies WHERE currency_name = %s', (currency_name,))
    row = cur.fetchone()
    if not row:
        cur.close()
        conn.close()
        return jsonify({'error': 'Валюта не найдена'}), 404

    rate = float(row[0])
    converted = amount * rate
    cur.close()
    conn.close()

    return jsonify({
        'currency': currency_name,
        'amount': amount,
        'rate': rate,
        'converted_amount': round(converted, 2)
    }), 200

@app.route('/currencies', methods=['GET'])
def get_currencies():
    """Возвращает список всех валют из таблицы"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT currency_name, rate FROM currencies')
    rows = cur.fetchall()

    currencies_list = [{'currency_name': row[0], 'rate': float(row[1])} for row in rows]

    cur.close()
    conn.close()

    return jsonify({'currencies': currencies_list}), 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)