from app import app, redis
from .short_link import create_short_link, get_short_link

app.add_url_rule('/', view_func=create_short_link, methods=['GET', 'POST'])
app.add_url_rule('/<string:short_link>/',
                 view_func=get_short_link, methods=['GET'])
