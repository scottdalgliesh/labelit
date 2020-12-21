from pathlib import Path

from jinja2 import Template
import openpyxl
import pdfkit

#file directories
root = Path(__file__).parent.parent
html = root / 'labelit' / 'template.html'
css = root / 'labelit' / 'style.css'
out_html = root / 'output' / 'output.html'
out_pdf = root / 'output' / 'output.pdf'
excel = root / 'labelit' / 'sample_data.xlsx'

#import data from excel
wb = openpyxl.load_workbook(excel, data_only=True)
ws = wb.get_sheet_by_name('Sheet1')
rows = ws.max_row
bulls = [(ws[f'A{x}'].value, ws[f'B{x}'].value, ws[f'C{x}'].value) for x in range(2, rows+1)]

#sort by date then name
bulls.sort(key= lambda x: (x[2], x[0]))

#read html template
with open(html) as file:
    template = Template(file.read())
doc = template.render({'bulls':bulls, 'css':css})

#output complete html document
with open(out_html, 'w') as file:
    file.write(doc)

# output complete pdf
options = {'enable-local-file-access': None, 'print-media-type': None}
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
pdfkit.from_string(doc, out_pdf, configuration=config, options=options)
