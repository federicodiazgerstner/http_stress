from flask import Flask, render_template
import time
app = Flask(__name__)

def countdown(n):
    while n>0:
        n-= 1
    return 
@app.route('/')
def hello_world():
    return 'Index Page'

@app.route('/script')
def script():
    start = time.time()
    countdown(1000000) #cuenta regresiva de 1.000.000
    end = time.time()
    print(end - start)
    return render_template('index.html')

