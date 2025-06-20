def is_producer(
    soup_company_page,
):  # boolean check for if the company is producer since the task wants producers
    is_producer = (
        soup_company_page.find("img", attrs={"data-test": "production"}) is not None
    )
    return is_producer


import re


def check_for_blockers(html_text):
    patterns = [
        r"accept\s+(all\s+)?cookies?",  # accept cookies / accept all cookies
        r"we\s+use\s+cookies",
        r"cookie\s+(policy|preferences|settings)",
        r"this\s+site\s+uses\s+cookies",
        r"are\s+you\s+(over\s+)?18",  # are you over 18
        r"you\s+must\s+be\s+18",  # you must be 18
        r"i\s+am\s+(over\s+)?18",  # I am 18 / I am over 18
        r"by\s+continuing\s+to\s+use\s+this\s+site",
    ]

    lower_html = html_text.lower()

    for pattern in patterns:
        matches = re.findall(pattern, lower_html)
        if matches:
            return pattern  # Eşleşen regex pattern'ı döner

    return None
