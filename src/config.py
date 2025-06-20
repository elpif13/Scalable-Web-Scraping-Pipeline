HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.google.com/",
}


# configurations
SOURCE_URL_EN = "https://www.europages.co.uk/en"
SOURCE_URL = "https://www.europages.co.uk"
SECTOR = "wines"
SUPPLIER_TYPE = "Manufacturer/Producer"  # since task wants wine producers

# CSV files
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_DIR = os.path.join(BASE_DIR, "csv-files/")

EMAIL_CSV_FILENAME = f"emails_{SECTOR}.csv"
LINK_CSV_FILENAME = f"links_{SECTOR}.csv"

# HTML constants
