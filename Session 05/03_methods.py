from flask import Flask
from flask import request, Response, jsonify

app = Flask(__name__)


@app.route('/request', methods=['GET', 'POST'])
def request_method():
    print(f'Headers: [{(request.headers)}]')
    print(f'Arguments: [{request.args}]')
    if request.method == 'POST':
        # wget --method=POST http://localhost:5000/request
        text = "This is Post Method"
    else:
        text = "This is a GET"

    resp = Response(text, status=200, mimetype='text/plain')
    return resp        


@app.route('/response', methods=['GET', 'POST'])
def response_method():
    print(request.headers)

    json_dict = {'a': 1, 'b': 2, 'c':3}

    resp = Response(jsonify(json_dict), status=200, mimetype='application/json')
    return resp        