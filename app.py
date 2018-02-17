import random
import time

from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)
random.seed()

chars = list('abcdefghijkmnpqrstuvwxyz0123456789')

def random_string(length=10):
    return ''.join(random.choices(chars, k=length))


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/health')
def health():
    return jsonify({'status': 'OK'})


@app.route('/shorter')
def shorter():
    time.sleep(0.3)
    s = random_string()
    return jsonify({'results': s})


@app.route('/longer')
def longer():
    time.sleep(1.5)
    s = random_string(20)
    return jsonify({'results': s})
