import re
import time
from urllib.parse import urljoin

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def extract_email_from_text(text):
    """
    Extract the first valid-looking email from text.
    Filters out version numbers, static files, and dummy/test addresses.
    """
    matches = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

    invalid_extensions = {
        "png",
        "jpg",
        "jpeg",
        "gif",
        "webp",
        "svg",
        "css",
        "js",
        "woff",
        "ico",
        "ttf",
        "eot",
        "otf",
        "mp4",
        "mp3",
        "pdf",
    }

    dummy_addresses = {
        "name@domain.com",
        "example@example.com",
        "info@example.com",
        "test@test.com",
        "your@email.com",
        "email@domain.com",
    }

    filtered = []
    for email in matches:
        # Strip and lowercase to compare safely
        email_clean = email.strip().lower()

        # 1. Ignore dummy placeholders
        if email_clean in dummy_addresses:
            continue

        # 2. Filter out version-looking patterns
        if re.search(r"@\d+\.\d+(\.\d+)?$", email):
            continue

        # 3. Filter out file extensions
        tld = email.split(".")[-1].lower()
        if tld in invalid_extensions:
            continue

        filtered.append(email)

    return filtered[0] if filtered else None


def extract_email_with_requests(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"[{url}] – HTTP Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[{url}] – Connection Error: {e}")
        return None


def setup_selenium_driver():
    """
    Create a headless Chrome WebDriver instance.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=chrome_options)


def try_closing_popups(driver):
    """
    Click on common popup buttons like cookie consent or age gates.
    """
    popup_texts = ["Accept", "Si, ho l'età", "Close", "I am over 18", "18"]
    for text in popup_texts:
        try:
            xpath = f'//*[contains(text(), "{text}")]'
            elements = driver.find_elements(By.XPATH, xpath)
            for el in elements:
                try:
                    el.click()
                    time.sleep(1)
                except:
                    pass
        except:
            pass


def extract_email_with_selenium(url, driver):
    """
    Load the URL with Selenium and extract the first email if available.
    """
    driver.get(url)
    time.sleep(2)
    try_closing_popups(driver)
    return extract_email_from_text(driver.page_source)


def find_contact_like_elements(driver):
    """
    Find elements that likely lead to contact/about pages.
    Supports links, buttons, divs, etc. with keywords like contact, kontakt, impressum.
    """
    keywords = ["contact", "about", "about us", "kontakt", "impressum", "contacts"]
    results = []

    for word in keywords:
        xpath = f"""//*[self::a or self::button or self::div][contains(
            translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{word}')]"""
        elements = driver.find_elements(By.XPATH, xpath)
        results.extend(elements)

    return results


def extract_emails_from_website(base_url):
    """
    Master function: try requests first, then selenium, then subpages.
    """
    # Step 1: Try with requests
    email = extract_email_with_requests(base_url)
    if email:
        print("[+] Found email via requests:", email)
        return email, None

    # Step 2: Try with selenium (homepage)
    driver = setup_selenium_driver()
    try:
        email = extract_email_with_selenium(base_url, driver)
        if email:
            print("[+] Found email via selenium homepage:", email)
            return email, None

            # Step 3: Try subpages like contact/about/kontakt
        elements = find_contact_like_elements(driver)
        visited = set()
        for el in elements:
            href = el.get_attribute("href")

            if href and not href.startswith("javascript"):
                full_url = urljoin(base_url, href)
                if full_url in visited:
                    continue
                visited.add(full_url)

                try:
                    driver.get(full_url)
                    time.sleep(2)
                    email = extract_email_from_text(driver.page_source)
                    if email:
                        print("[+] Found email via selenium subpage:", email)
                        return email, None
                except Exception as e:
                    print(f"[-] Failed to get {full_url}: {e}")
                    continue

            else:
                # Fallback: try clicking the element if no valid href
                try:
                    el.click()
                    time.sleep(2)
                    email = extract_email_from_text(driver.page_source)
                    if email:
                        print("[+] Found email via selenium click-through:", email)
                        return email, None
                except Exception as e:
                    print(f"[-] Click failed: {e}")
                    continue

    except Exception as e:
        return None, e
    finally:
        driver.quit()

    print("[-] No email found.")
    return None, None
