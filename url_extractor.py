import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_and_parse_url(start_url: str) -> list:
    response = requests.get(start_url, verify=False)
    if response.status_code != 200:
        response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # Filter and sort URLs
    filtered_urls = []
    for link in soup.find_all('a'):
        href = link.get('href')
        full_url = urljoin(start_url, href)
        if full_url.startswith(start_url):
            filtered_urls.append(full_url)
    return sorted(set(filtered_urls))
