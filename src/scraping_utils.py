import time

from bs4 import BeautifulSoup
from selenium import webdriver


def get_page_count(url):  # return how many pages
    driver = webdriver.Chrome()
    driver.get(
        url
    )  # instead of request i use driver because the div that i wanna retrieve is loaded dynamically

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    last_page_tag = soup.find(
        "div", class_="disabled button number", attrs={"data-test": "pagination-number"}
    )  # this gives how many pages are there a.k.a max page number

    if last_page_tag:
        last_page = last_page_tag.text
        if last_page.isdigit:
            return int(last_page)
        else:
            raise ValueError("Variable page number is not an integer.")
    else:
        raise ValueError("Could not find page number.")


# static way of the retrieve page count

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.europages.co.uk/en/products?categories=200618&isPserpFirst=1&q=wine"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# outer_div = soup.find(
#     "div", class_="flex flex-wrap gap-y-2 items-center justify-center py-3 md:py-6"
# )
# print(outer_div.text)  # return "1234...58next" use regex to retrieve 58

# ----------------------------------------


def get_country_of_company(soup_company_page):
    flag_icon = soup_company_page.find("span", class_="vis-flag")

    if flag_icon:
        country_span = flag_icon.find_next_sibling("span")
        if country_span:
            return country_span.text.strip()

    return None


def get_website_of_company(soup_company_page):
    website_tag = soup_company_page.find(
        "a", class_="btn btn--subtle btn--md website-button"
    )
    website = (
        website_tag["href"].strip()
        if website_tag and website_tag.has_attr("href")
        else None
    )
    return website
