import re


def get_sector_url(source_url, sector):  # returns sector spesific url
    return source_url + f"/search?q={sector}"


def get_sector_url_with_page(
    sector_url: str, page_number: int
) -> str:  # url with page numbers
    return re.sub(r"/search(\?q=.+)", rf"/search/page/{page_number}\1", sector_url)
