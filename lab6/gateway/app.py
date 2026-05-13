from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Адреса микросервисов
CURRENCY_MANAGER_URL = "http://127.0.0.1:5001"
DATA_MANAGER_URL = "http://127.0.0.1:5002"

@app.route('/')
def index():
    """Главная страница с формой добавления валюты и списком валют."""
    # Получаем список валют через data-manager
    try:
        resp = requests.get(f"{DATA_MANAGER_URL}/currencies")
        currencies_data = resp.json().get('currencies', [])
    except:
        currencies_data = []

    return render_template('index.html', currencies=currencies_data)

@app.route('/load', methods=['POST'])
def load_currency():
    """Прокси на POST /load у currency-manager."""
    data = request.form  # из HTML-формы данные приходят как form
    resp = requests.post(f"{CURRENCY_MANAGER_URL}/load", json={
        'currency_name': data.get('currency_name'),
        'rate': data.get('rate')
    })
    return resp.text, resp.status_code

@app.route('/update_currency', methods=['POST'])
def update_currency():
    """Прокси на POST /update_currency."""
    data = request.form
    resp = requests.post(f"{CURRENCY_MANAGER_URL}/update_currency", json={
        'currency_name': data.get('currency_name'),
        'rate': data.get('rate')
    })
    return resp.text, resp.status_code

@app.route('/delete', methods=['POST'])
def delete_currency():
    """Прокси на POST /delete."""
    data = request.form
    resp = requests.post(f"{CURRENCY_MANAGER_URL}/delete", json={
        'currency_name': data.get('currency_name')
    })
    return resp.text, resp.status_code

@app.route('/convert', methods=['POST'])
def convert():
    """Прокси на GET /convert у data-manager, но принимает данные из формы."""
    if request.method == 'POST':
        # перенаправляем GET-параметрами на /convert?currency=...&amount=...
        currency = request.form.get('currency')
        amount = request.form.get('amount')
        resp = requests.get(f"{DATA_MANAGER_URL}/convert", params={
            'currency': currency,
            'amount': amount
        })
        return resp.text, resp.status_code
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)