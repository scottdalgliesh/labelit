from datetime import datetime
from pathlib import Path
from typing import List, Tuple

from jinja2 import Template
import openpyxl
import pdfkit

#type aliases
Label = List[Tuple[str, str, datetime]]

#static file directories
root = Path(__file__).parent.parent
html = root / 'labelit' / 'template.html'
css = root / 'labelit' / 'style.css'

def import_data(book_name: str, sheet_name: str) -> Label:
    """Import label data from excel workbook (assume first row are labels)"""
    book = openpyxl.load_workbook(book_name, data_only=True)
    sheet = book.get_sheet_by_name(sheet_name)
    rows = sheet.max_row
    return [(sheet[f'A{x}'].value, sheet[f'B{x}'].value, sheet[f'C{x}'].value)
            for x in range(2, rows+1)]

def generate_html(labels: Label) -> str:
    """Sort data and generate html for labels"""
    labels.sort(key= lambda x: (x[2], x[0]))
    with open(html) as file:
        template = Template(file.read())
    return template.render({'labels':labels, 'css':css})

def output_labels(label_html: str, output_name: str, output_html: bool) -> None:
    """Output labels as a PDF, and optionally as html"""
    options = {'enable-local-file-access': None, 'print-media-type': None}
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdfkit.from_string(label_html, output_name, configuration=config, options=options)
    print(f'\nFile generated: {output_name}')

    if output_html:
        html_name = output_name.rstrip('.pdf') + '.html'
        with open(html_name, 'w') as file:
            file.write(label_html)
        print(f'File generated: {html_name}')

def main(input_workbook: str, input_sheet: str, output_pdf: str, output_html: bool) -> None:
    """Generate sorted labels from excel data"""
    label_data = import_data(input_workbook, input_sheet)
    label_html = generate_html(label_data)
    output_labels(label_html, output_pdf, output_html)
