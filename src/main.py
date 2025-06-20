from config import SECTOR, SOURCE_URL_EN
from iterators import iterate_pages
from scraping_utils import get_page_count
from url_utils import get_sector_url

sector_url = get_sector_url(SOURCE_URL_EN, SECTOR)

page_count = get_page_count(sector_url)

iterate_pages(page_count, sector_url)

# from email_scraping import extract_emails_from_website

# print(extract_emails_from_website("https://www.burgondie.info"))
