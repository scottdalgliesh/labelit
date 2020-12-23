import click

from .labelit import main

@click.command()
@click.option('-i', '--input_workbook',
              default='input_data.xlsx',
              type=click.Path(exists=True, dir_okay=False),
              show_default=True,
              help='workbook name (with ".xlsx" extension) for input data import')
@click.option('-s', '--input_sheet',
              default='Sheet1',
              type=click.STRING,
              show_default=True,
              help='worksheet name for input data import')
@click.option('-o', '--output_pdf',
              default='labels.pdf',
              type=click.STRING,
              show_default=True,
              help='file name (with ".pdf" extension) for ouput')
@click.option('--output-html/--no-output-html',
              default=False,
              show_default=True,
              help='enable output of generated html for inspection')
def cli(input_workbook: str, input_sheet: str, output_pdf: str, output_html: bool) -> None:
    """Generate labels from excel input data"""
    try:
        main(input_workbook, input_sheet, output_pdf, output_html)
    except TypeError as type_error:
        print(f'ERROR - NO LABELS GENERATED\n{type_error}')

#pylint:disable=no-value-for-parameter
if __name__ == '__main__':
    cli()
