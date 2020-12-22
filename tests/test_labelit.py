from pathlib import Path

import pytest

from labelit import labelit #pylint:disable=import-error

#pylint:disable=[missing-function-docstring]

def test_import_data(sample):
    data = labelit.import_data(sample['workbook'], sample['sheet'])
    assert data == sample['data']

def test_generate_html(sample):
    html = labelit.generate_html(sample['data'])
    assert sample['html'] == html

test_input = [
    pytest.param(True, id="with html printout"),
    pytest.param(False, id="without html printout")
]

@pytest.mark.parametrize("output_html", test_input)
def test_output_labels(sample, tmp_path, output_html):
    output_name_pdf = tmp_path / 'labels.pdf'
    output_name_html = tmp_path / 'labels.html'
    labelit.output_labels(sample['html'], str(output_name_pdf), output_html)
    assert output_name_pdf.exists()

    if output_html:
        with open(output_name_html) as file:
            test_html = file.read()
        assert test_html == sample['html']
    else:
        assert not Path(output_name_html).exists()

# 'main' function is tested in 'test_cli.py'
