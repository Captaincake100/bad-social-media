from flask import Flask, render_template, request, redirect, url_for
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template('#index.html', x = 'good')

@app.route('/<usr>')
def usr(usr):
  return render_template('user.html', usr = usr)
  
@app.route('/login', methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
    user = request.form['nm']
    return redirect(url_for('usr', usr=user))
  else:
    return render_template('login.html')
print("test")
app.run(host='0.0.0.0', port=8080)