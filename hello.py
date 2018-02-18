import random
import asyncio

from quart import Quart
from quart import render_template
from quart import jsonify

app = Quart(__name__)
random.seed()


def random_string(length=10):
    chars = list('abcdefghijkmnpqrstuvwxyz0123456789')
    return ''.join(random.choices(chars, k=length))

@app.route('/')
async def hello_world():
    return await render_template('hello.html')


@app.route('/health')
async def health():
    return jsonify({'status': 'OK'})


@app.route('/shorter')
async def shorter():
    await asyncio.sleep(0.3)
    s = random_string()
    return jsonify({'results': s})


@app.route('/longer')
async def longer():
    await asyncio.sleep(1.5)
    s = random_string(20)
    return jsonify({'results': s})


app.run()