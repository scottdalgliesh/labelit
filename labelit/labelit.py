from datetime import date

from jinja2 import Template
import pdfkit

from .sample_data import bulls

#sort by date then name
bulls = [(x[0], x[1], date.fromisoformat(x[2])) for x in bulls]
bulls.sort(key= lambda x: (x[2], x[0]))

#read html template
with open(r'labelit\template.html') as file:
    template = Template(file.read())
doc = template.render({'bulls':bulls})

#output complete html document
with open(r'output\output.html', 'w') as file:
    file.write(doc)

# output complete pdf
options = {'enable-local-file-access': None, 'print-media-type': None}
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
pdfkit.from_string(doc,r'output\output.pdf', configuration=config, options=options)
