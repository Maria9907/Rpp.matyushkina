from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Конфигурация подключения к БД
DB_CONFIG = {
    'dbname': 'currencies_db',   
    'user': 'postgres',         
    'password': 'postgres',    
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    """Устанавливает соединение с PostgreSQL."""
    return psycopg2.connect(**DB_CONFIG)
    

@app.route('/load', methods=['POST'])
def load_currency():
    """Добавление новой валюты"""
    data = request.get_json()
    currency_name = data.get('currency_name')
    rate = data.get('rate')

    conn = get_db_connection()
    cur = conn.cursor()

    # Проверка, существует ли уже такая валюта
    cur.execute('SELECT id FROM currencies WHERE currency_name = %s', (currency_name,))
    if cur.fetchone():
        cur.close()
        conn.close()
        return jsonify({'error': 'Валюта уже существует'}), 409

    cur.execute(
        'INSERT INTO currencies (currency_name, rate) VALUES (%s, %s)',
        (currency_name, rate)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Валюта успешно добавлена'}), 200

@app.route('/update_currency', methods=['POST'])
def update_currency():
    """Обновление курса существующей валюты."""
    data = request.get_json()
    currency_name = data.get('currency_name')
    new_rate = data.get('rate')

    conn = get_db_connection()
    cur = conn.cursor()

    # Проверка существования валюты
    cur.execute('SELECT id FROM currencies WHERE currency_name = %s', (currency_name,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        return jsonify({'error': 'Валюта не найдена'}), 404

    # Обновление курса
    cur.execute(
        'UPDATE currencies SET rate = %s WHERE currency_name = %s', (new_rate, currency_name)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Курс обновлён'}), 200

@app.route('/delete', methods=['POST'])
def delete_currency():
    """Удаление валюты по названию."""
    data = request.get_json()
    currency_name = data.get('currency_name')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id FROM currencies WHERE currency_name = %s', (currency_name,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        return jsonify({'error': 'Валюта не найдена'}), 404

    cur.execute('DELETE FROM currencies WHERE currency_name = %s', (currency_name,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Валюта удалена'}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)