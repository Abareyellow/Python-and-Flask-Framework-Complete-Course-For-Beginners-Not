from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def index(name):
    return 'Hello %s' % name

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
  # app.run(debug=True)
