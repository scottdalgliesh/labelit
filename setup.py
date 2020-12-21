from setuptools import setup, find_packages

setup(
    name='labelit',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'jinja2',
        'pdfkit',
        'openpyxl'
    ],
    entry_points='''
        [console_scripts]
        labelit=labelit.cli:cli
    ''',
)
