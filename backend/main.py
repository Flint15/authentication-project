from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
  return 'love'

@app.route('/love/<name>')
def love(name):
  return f'I love you {name}'

if __name__ == '__main__':
  app.run(port=5000, debug=True)