from flask import Flask, request, jsonify
from flask_cors import CORS
from database import insert_data
import hashlib

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
  return 'love'

@app.route('/love/<name>')
def love(name):
  return f'I love you {name}'

@app.route('/register', methods=['POST'])
def receive_data():
  data = request.get_json()
  name = data.get('name')
  gmail = data.get('gmail')
  password = data.get('password')

  hashed_password = hashlib.sha256(password.encode()).hexdigest()

  response: str = insert_data(name, gmail, hashed_password)

  return jsonify({
    'status': 'ok',
    'response': response,
    'data': {
      'gmail': gmail
    }
  })

if __name__ == '__main__':
  app.run(port=5000, debug=True)