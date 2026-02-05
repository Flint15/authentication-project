from flask import Flask, request, jsonify
from flask_cors import CORS
from database import insert_data, retrive_data
import bcrypt

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
  return 'love'

@app.route('/love/<name>')
def love(name):
  return f'I love you {name}'

@app.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  name = data.get('name')
  gmail = data.get('gmail')
  password = data.get('password')

  hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

  response: str = insert_data(name, gmail, hashed_password)

  return jsonify({
    'status': 'ok',
    'response': response,
    'data': {
      'name': name,
      'gmail': gmail
    }
  })

def verify_password(input_password: str, stored_hash: bytes) -> bool:
  return bcrypt.checkpw(input_password.encode(), stored_hash)

@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  gmail = data.get('gmail')
  password = data.get('password')

  user = retrive_data(gmail)
  if user is None:
    return jsonify({
      'status': 'not ok',
      'response': None
    }), 401

  stored_password: bytes = user['password']
  verification: bool = verify_password(password, stored_password)

  if verification:
    return jsonify({
      'status': 'ok',
      'response': 'User was found',
      'data': {
        'name': user['name'],
        'gmail': user['gmail']
      }
    })

  return jsonify({
    'status': 'not ok',
    'response': 'User with that gmail does not exist'
  }), 401

if __name__ == '__main__':
  app.run(port=5000, debug=True)