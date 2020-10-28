from flask import Flask

app = Flask(__name__)
@app.route('/')
def index ():
    return 'Aplicação Web com Python e Flask! Por ERIC OLIVEIRA DATA SCIENTIST'
      
app.run(host='0.0.0.0',port=81)