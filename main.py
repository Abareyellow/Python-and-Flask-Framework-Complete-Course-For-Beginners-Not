from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome {}</h1>'.format(name)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    print(request.method)
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp
    else:
        return render_template('setcookie.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug = True)
  # app.run(debug=True)
