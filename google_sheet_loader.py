import gspread
import pandas as pd


def load_google_sheet(spreadsheet_key: str, worksheet_name: str, credentials_path: str) -> pd.DataFrame:
    """Load a Google Sheet worksheet into a DataFrame using gspread.

    Parameters
    ----------
    spreadsheet_key : str
        The unique key of the spreadsheet.
    worksheet_name : str
        Name of the worksheet within the spreadsheet.
    credentials_path : str
        Path to the service account credentials JSON file.

    Returns
    -------
    pandas.DataFrame
        Data extracted from the worksheet with columns taken from the first row.
    """
    gc = gspread.service_account(filename=credentials_path)
    sh = gc.open_by_key(spreadsheet_key)
    worksheet = sh.worksheet(worksheet_name)
    values = worksheet.get_all_values()
    if not values:
        return pd.DataFrame()
    return pd.DataFrame(values[1:], columns=values[0])
