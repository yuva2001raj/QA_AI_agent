from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse

def is_valid_url(url, base_netloc):
    parsed = urlparse(url)
    return parsed.netloc == base_netloc and parsed.scheme in {"http", "https"}

def crawl_site(base_url, max_pages=30):
    visited = set()
    to_visit = [base_url]
    pages = {}
    base_netloc = urlparse(base_url).netloc

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            main_text = soup.get_text(separator="\n")
            pages[url] = main_text
            visited.add(url)

            for a in soup.find_all("a", href=True):
                next_url = urljoin(url, a["href"])
                if is_valid_url(next_url, base_netloc) and next_url not in visited:
                    to_visit.append(next_url)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    return pages
