import requests
from bs4 import BeautifulSoup
from config import HEADERS, SOURCE_URL
from csv_utils import initialize_email_csv_df, initialize_link_csv_df
from directors import direct_company_page_url
from url_utils import get_sector_url_with_page


def iterate_companies(soup):  # iterate companies in the page
    spans = soup.find_all("span", class_="line-clamp-2 md:line-clamp-1 break-anywhere")
    for span in spans:
        company_name = span.text.strip()

        parent_a = span.find_parent("a")
        if parent_a and parent_a.has_attr("href"):
            company_page_url = SOURCE_URL + parent_a["href"]
            direct_company_page_url(company_page_url, company_name)

        else:
            continue  # could not find the company page url


def iterate_pages(page_count, sector_url):

    # initialzation of csv files
    initialize_email_csv_df()
    initialize_link_csv_df()

    for i in range(1, page_count):
        print(f"\n--- Page {i} ---")
        sector_url_with_page = get_sector_url_with_page(sector_url, i)
        response = requests.get(sector_url_with_page, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        iterate_companies(soup)
