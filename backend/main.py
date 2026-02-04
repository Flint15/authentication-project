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

@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  gmail = data.get('gmail')
  password = data.get('password')

  response = retrive_data(gmail, password)

  return jsonify({
    'status': 'ok',
    'response': response
  })

if __name__ == '__main__':
  app.run(port=5000, debug=True)