from flask import render_template, redirect, url_for, abort
from app import app, redis
from flask import request
from .compression import CompressionLink

comp = CompressionLink()


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html', title='404'), 404


def create_short_link():
    full_link, short_link = None, None
    #TODO: need check valid url
    if request.method == 'POST':
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
