from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/id/<int:id>', methods=['GET'])
def get(id: int):
    return {"result": bool(id >= 5000)}


@app.route('/id', methods=['POST'])
def post():
    req = request.json
    return {'name': req['name']}


@app.route('/')
def test():
    return 'server is open'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
