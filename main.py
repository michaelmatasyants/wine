from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import date
import collections
from pathlib import Path
import argparse
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas


def get_name_of_year(year: int) -> str:
    if year % 100 in (11, 12, 13, 14):
        return f"{year} лет"
    elif year % 10 in (2, 3, 4):
        return f"{year} года"
    elif year % 10 == 1:
        return f"{year} год"
    return f"{year} лет"


def get_wines_from_excel(file_path: Path, sheet_name='Лист1') -> dict:
    '''Fetches a table from an excel file and returns dict with drinks
       sorted by category'''
    excel_df = pandas.read_excel(file_path, sheet_name, na_values=['NaN'],
                                 keep_default_na=False)
    headers = excel_df.columns.ravel()
    category_header = headers[0]
    categories = sorted(excel_df[category_header].unique().tolist())
    all_wines = [dict(zip(headers, list(rows)))
                 for _, rows in excel_df.iterrows()]
    wines_by_category = collections.defaultdict(list)
    for category in categories:
        for wine in all_wines:
            if wine[category_header] == category:
                wines_by_category[category].append(wine)
    return wines_by_category


def main():
    '''Main function'''
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    wine_parser = argparse.ArgumentParser(
        description='''Program makes it easy to add (remove) drinks to the wine
                    store website page.
                    To make changes on website, you only need to edit wine.xlsx
                    file or create a similar file and pass the file path.
                    The script will do everything itself for you.
                    '''
    )
    wine_parser.add_argument('-f', '--file_path',
                             type=Path,
                             default=Path('wine.xlsx'),
                             help='excel file path with drinks')
    args = wine_parser.parse_args()
    template = env.get_template('template.html')
    rendered_page = template.render(
        since_foundation_years=get_name_of_year(year=date.today().year - 1920),
        all_wines=get_wines_from_excel(file_path=args.file_path),
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
