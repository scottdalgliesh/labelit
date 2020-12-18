from jinja2 import Template

# list of bulls & codes
bulls = [
    ('High Octane', '1111-1111-1111','2020-12-18'),
    ('World Wide', '2222-2222-2222','2020-12-18'),
    ('Bean', '3333-3333-3333','2020-12-18'),
    ('Cali', '4444-4444-4444','2020-12-18'),
    ('Delta', '5555-5555-5555','2020-12-18'),
    ('Stinker', '6666-6666-6666','2020-12-18'),
    ('Grumpy', '7777-7777-7777','2020-12-18'),
    ('Farty', '8888-8888-8888','2020-12-18'),
]

#alphabetical sort
bulls.sort()

#read html template
with open(r'labelit\template.html') as file:
    template = Template(file.read())
doc = template.render({'bulls':bulls})

#output complete html document
with open(r'labelit\output.html', 'w') as file:
    file.write(doc)

#TODO: convert HTML document to printable pdf
#TODO: auto-import from AX