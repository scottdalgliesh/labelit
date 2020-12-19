from jinja2 import Template
import pdfkit

from .sample_data import bulls

#alphabetical sort
bulls.sort()

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
pdfkit.from_string(doc,'output\output.pdf', configuration=config, options=options)
