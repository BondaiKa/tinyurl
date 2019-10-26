from flask import render_template, redirect, url_for, abort
from app import app, redis
from flask import request
from .compression import CompressionLink
import re

comp = CompressionLink()

regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


def create_short_link():
    full_link, short_link = None, None

    if request.method == 'POST' and re.match(regex, request.form['full_link']):
        full_link = request.form['full_link']
        redis.incr('linked_id')
        counter = int(redis.get('linked_id'))
        short_link = comp.compress_url(counter)
        redis.set(short_link, full_link, nx=True)
        short_link = request.url + short_link

    return render_template('main.html', context={'full_link': full_link, 'short_link': short_link})


def get_short_link(short_link):
    full_link = redis.get(short_link)
    if full_link is None:
        abort(404)
    return redirect(full_link, code=302)


app.add_url_rule('/', view_func=create_short_link, methods=['GET', 'POST'])
app.add_url_rule('/<string:short_link>/', view_func=get_short_link, methods=['GET'])
