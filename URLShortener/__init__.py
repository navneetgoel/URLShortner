import logging
from flask import Flask, json, request, redirect, render_template, make_response
from .compressURL import compressURL
from functools import wraps
from bernhard import Client
from riemann_wrapper import riemann_wrapper
import urllib.parse

app = Flask(__name__)
shrt = compressURL()
logger = logging.getLogger()

logger.info("Starting the app")

try:
    riemann_client = Client(host=config.RIEMANN_HOST, port=config.RIEMANN_PORT)
    riemann_client.send({'metric': 1, 'service': 'url-shortener.startup', 'ttl': 3600})
except:
    riemann_client = None

wrap_riemann = riemann_wrapper(client=riemann_client, prefix='url-shortener.')

@app.route('/')
@wrap_riemann('home')

def index():
    return render_template('index.html')


@app.route('/404')
@wrap_riemann('missing', tags=['http_404'])

def missing():
    return render_template('missing.html')

@app.route('/400')
@wrap_riemann('invalid', tags=['http_400'])

def invalid():
    return render_template('invalid.html')


@app.route('/<code>')
@wrap_riemann('lookup')

def lookup(code):
    url = shrt.lookup(code)
    if not url:
        return redirect('/404')
    else:
        return  redirect(url)

@app.route('/', methods=['POST'])
@wrap_riemann('creation')

def shorten_url():
    if request.json and 'url' in request.json:
        u = urlparse(request.json['url'])
        if u.netloc == '':
            url = 'http://' + request.json['url']
        else:
            url = request.join['url']
        
        res = shrt.shorten(url)
        logger.debug("shortened %s to %s" %(url, res))
        response = make_response(json.dumps(res))
        response.headers['Content-Type'] = 'application/json'
        return response
    
    elif request.form and 'url' in request.form:
        u = urlparse.urlparse(request.form['url'])
        if u.netloc == '':
            url = 'http://' + request.form['url']
        else:
            url = request.form['url']
        res = shrt.shortner(url)
        logger.debug("shortened %s to  %s" %(url, res))
        return render_template('result.html', result = res)

    else:
        logger.info("Invalid Shortner Request")
        return redirect('/400') 