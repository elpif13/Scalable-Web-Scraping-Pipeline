import pandas as pd
from config import CSV_DIR, EMAIL_CSV_FILENAME, LINK_CSV_FILENAME


def initialize_email_csv_df():
    df = pd.DataFrame(columns=["Name", "Country", "Email"])
    df.to_csv(CSV_DIR + EMAIL_CSV_FILENAME, index=False)


def append_to_email_csv_df(company_name, country=None, email=None):
    new_row = pd.DataFrame(
        [[company_name, country, email]], columns=["Name", "Country", "Email"]
    )
    new_row.to_csv(CSV_DIR + EMAIL_CSV_FILENAME, mode="a", header=False, index=False)


def initialize_link_csv_df():
    df = pd.DataFrame(columns=["Name", "Link"])
    df.to_csv(CSV_DIR + LINK_CSV_FILENAME, index=False)


def append_to_link_csv_df(company_name, link=None):
    new_row = pd.DataFrame([[company_name, link]], columns=["Name", "Link"])
    new_row.to_csv(CSV_DIR + LINK_CSV_FILENAME, mode="a", header=False, index=False)
