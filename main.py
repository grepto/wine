from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from wines import get_wines

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

found_year = 1920
now_year = datetime.datetime.now().year

render_page = template.render(
    years_count=now_year - found_year,
    wines=get_wines(),
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(render_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
