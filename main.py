from http.server import HTTPServer, SimpleHTTPRequestHandler

from datetime import date
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas


def name_of_year(year: int) -> str:
    if year % 100 in (11, 12, 13, 14):
        return f"{year} лет"
    elif year % 10 in (2, 3, 4):
        return f"{year} года"
    elif year % 10 == 1:
        return f"{year} год"
    return f"{year} лет"


def get_wines_from_excel(filename='wine.xlsx', sheet_name='Лист1') -> list[dict]:
    excel_df = pandas.read_excel(filename, sheet_name)
    headers = ['name', 'variety', 'price', 'image']
    all_wines = [dict(zip(headers, list(rows))) for _, rows in excel_df.iterrows()]
    return all_wines


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    since_foundation_years=name_of_year(year=date.today().year - 1920),
    wines=get_wines_from_excel(),
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
server.serve_forever()
