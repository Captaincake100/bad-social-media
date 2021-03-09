from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template('#index.html', x = 'good')

@app.route('/usr/<username>')
def usr(username):
  return username
  
app.run(host='0.0.0.0', port=8080)