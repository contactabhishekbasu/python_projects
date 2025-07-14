import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from unittest.mock import Mock, patch

import google_sheet_loader


def test_load_google_sheet_uses_first_row_as_columns():
    data = [
        ['col1', 'col2', 'col3'],
        ['a', 'b', 'c'],
        ['d', 'e', 'f']
    ]
    worksheet_mock = Mock()
    worksheet_mock.get_all_values.return_value = data

    sheet_mock = Mock()
    sheet_mock.worksheet.return_value = worksheet_mock

    gc_mock = Mock()
    gc_mock.open_by_key.return_value = sheet_mock

    with patch('google_sheet_loader.gspread.service_account', return_value=gc_mock):
        df = google_sheet_loader.load_google_sheet('key', 'sheet1', 'creds.json')

    assert list(df.columns) == data[0]
    assert df.iloc[0].tolist() == data[1]
