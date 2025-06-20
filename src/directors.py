import requests
from bs4 import BeautifulSoup
from config import HEADERS
from csv_utils import append_to_email_csv_df, append_to_link_csv_df
from email_scraping import extract_emails_from_website
from filters import is_producer
from scraping_utils import get_country_of_company, get_website_of_company


def direct_company_website(
    website_of_company, company_name, country_of_company
):  # original website of the company

    company_email, error = extract_emails_from_website(website_of_company)
    if error:
        return
    append_to_email_csv_df(company_name, country_of_company, company_email)
    append_to_link_csv_df(company_name, website_of_company)


def direct_company_page_url(
    company_page_url, company_name
):  # company page url in the europages
    response_company_page = requests.get(company_page_url, headers=HEADERS)
    soup_company_page = BeautifulSoup(response_company_page.text, "html.parser")

    is_producer_flag = is_producer(soup_company_page)

    if is_producer_flag:
        website_of_company = get_website_of_company(soup_company_page)
        country_of_company = get_country_of_company(soup_company_page)
        if (
            website_of_company is not None
        ):  # some of the companies do not have website in europages.co
            direct_company_website(website_of_company, company_name, country_of_company)
            print(website_of_company, country_of_company)
