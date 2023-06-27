from http.server import HTTPServer, SimpleHTTPRequestHandler

from datetime import date
from jinja2 import Environment, FileSystemLoader, select_autoescape


def name_of_year(year: int) -> str:
    if year % 100 in (11, 12, 13, 14):
        return f"{year} лет"
    elif year % 10 in (2, 3, 4):
        return f"{year} года"
    elif year % 10 == 1:
        return f"{year} год"
    return f"{year} лет"


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    since_foundation_years=name_of_year(year=date.today().year - 1920),
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
