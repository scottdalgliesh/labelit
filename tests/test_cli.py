#pylint:disable=[missing-function-docstring, redefined-outer-name, unused-argument]

from os import chdir
from pathlib import Path
from shutil import copy

from click.testing import CliRunner
import pytest

from labelit.cli import cli  # pylint:disable=import-error

sample_path = Path('tests/sample_data')

test_input = [
    pytest.param('', 'input_data.xlsx', 'labels.pdf', id='no options'),
    pytest.param('-i sample_data.xlsx', 'sample_data.xlsx', 'labels.pdf', id='-i'),
    pytest.param('-i input_data_sheet2.xlsx -s Sheet2', 'input_data_sheet2.xlsx',
                 'labels.pdf', id='-s'),
    pytest.param('-o output.pdf', 'input_data.xlsx', 'output.pdf', id='-o'),
    pytest.param('--output-html', 'input_data.xlsx',
                 'labels.pdf', id='--output-html')
]

@pytest.fixture
def reset_cwd():
    initial_cwd = Path.cwd()
    yield
    chdir(initial_cwd)

@pytest.mark.parametrize('options,input_file_name,output_file_name', test_input)
def test_cli(sample, tmp_path, reset_cwd, options, input_file_name, output_file_name):
    copy(sample_path / input_file_name, tmp_path)
    options_list = options.split()
    chdir(tmp_path)
    runner = CliRunner()
    runner.invoke(cli, options_list)
    assert Path(output_file_name).exists()
    html_output = Path(output_file_name.rstrip('.pdf') + '.html')
    if "--output-html" in options_list:
        assert html_output.exists()
        with open(html_output) as file:
            html = file.read()
        assert html == sample['html']
    else:
        assert not html_output.exists()
