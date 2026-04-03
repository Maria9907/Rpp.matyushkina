import random
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/number/', methods=['GET'])
def get_number():
    param = int(request.args.get('param'))  
    random_number = random.randint(1, 10)             
    result = random_number * param

    return jsonify({
        "operation": "mul",
        "param": param,
        "random": random_number,
        "result": result
    })

@app.route('/number/', methods=['POST'])
def post_number():
    data = request.get_json()       
    param = data.get('jsonParam')

    random_number = random.randint(1, 10)

    operations = ['sum', 'sub', 'mul', 'div']
    operation = random.choice(operations)

    if operation == 'sum':
        result = random_number + param
    elif operation == 'sub':
        result = random_number - param
    elif operation == 'mul':
        result = random_number * param
    else:
        result = random_number / param

    return jsonify({
        "param": param,
        "random": random_number,
        "result": result,
        "operation": operation
    })

@app.route('/number/', methods=['DELETE'])
def delete_number():
    random_number = random.randint(1, 10)

    operations = ['sum', 'sub', 'mul', 'div']
    operation = random.choice(operations)

    return jsonify({
        "random": random_number,
        "operation": operation
    })


import requests

base_url = "http://127.0.0.1:5000/number/"

def apply_operation(a, b, operation):
    if operation == "sum":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    else:  # div
        return a / b

if __name__ == "__main__":
    import sys
    import time

    # если аргумент server
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        app.run(debug=True)
    else:
        # иначе клиентская часть
        time.sleep(1)
        #GET 
        param_get = random.randint(1, 10)
        resp_get = requests.get(base_url, params={"param": param_get}).json()
        get_num = resp_get["result"]
        get_opr = resp_get["operation"]
        print("GET запрос:")
        print(f"Параметр: {param_get}, Ответ: {resp_get}")

        #POST
        param_post = random.randint(1, 10)
        resp_post = requests.post(base_url, json={"jsonParam": param_post}).json()
        post_num = resp_post["result"]
        post_opr = resp_post["operation"]
        print("POST запрос:")
        print(f"Параметр: {param_post}, Ответ: {resp_post}")

        #DELETE
        resp_del = requests.delete(base_url).json()
        del_num = resp_del["random"]
        del_opr = resp_del["operation"]
        print("DELETE запрос:")
        print(f"Ответ: {resp_del}")

        #выражение
        result = get_num  # сначала GET
        result = apply_operation(result, post_num, get_opr)  # GET операция между GET и POST
        result = apply_operation(result, del_num, post_opr)  # POST операция между результатом и DELETE

        final_result = int(result)

        print("\nСоставленное выражение:")
        print(f"{get_num} {get_opr} {post_num} {post_opr} {del_num}")
        print(f"Не использовалось: {del_opr}")
        print("Результат:", final_result)

        