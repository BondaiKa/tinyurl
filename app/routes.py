from flask import render_template, redirect
from app import app, redis
from flask import request


def create_short_link():
    context = {'full_link': None, 'short_link': None}

    if request.method == 'POST':
        full_link = request.form['full_link']
        context['full_link'] = full_link
        redis.set('abc', full_link)

    return render_template('main.html', context=context)


def get_short_link(short_link):
    full_link = redis.get(short_link)
    return redirect(full_link, code=302)


app.add_url_rule('/', view_func=create_short_link, methods=['GET', 'POST'])
app.add_url_rule('/<string:short_link>/', view_func=get_short_link, methods=['GET'])
