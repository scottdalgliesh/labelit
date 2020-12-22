from datetime import datetime
from pathlib import Path

import pytest

#pylint:disable=[missing-function-docstring]

root = Path(__file__).parent #absolute path required since cli tests change cwd

@pytest.fixture
def sample():
    workbook = root / 'sample_data/sample_data.xlsx'
    # workbook = 'tests/sample_data/sample_data.xlsx'
    sheet = 'Sheet1'
    data = [
        ('High Octane', '1111-1111-1111', datetime(year=2020, month=12, day=18)),
        ('World Wide', '2222-2222-2222', datetime(year=2020, month=12, day=18)),
        ('Bean', '3333-3333-3333', datetime(year=2020, month=12, day=18)),
        ('Cali', '4444-4444-4444', datetime(year=2020, month=12, day=18)),
        ('High Octane', '1111-1111-1111', datetime(year=2020, month=12, day=17)),
        ('World Wide', '2222-2222-2222', datetime(year=2020, month=12, day=17)),
        ('Bean', '3333-3333-3333', datetime(year=2020, month=12, day=17)),
        ('Cali', '4444-4444-4444', datetime(year=2020, month=12, day=17))
        ]
    with open(root / 'sample_data/sample_output.html') as file:
        html = file.read()
    return {'workbook': workbook, 'sheet': sheet, 'data': data, 'html': html}
