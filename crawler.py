import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from database import save_page


def clean_text(text):
    return " ".join(text.split())


def crawl_page(url):
    try:
        print(f"Crawling: {url}")

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print("Failed to fetch page:", response.status_code)
            return

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title"

        for tag in soup(["script", "style"]):
            tag.decompose()

        content = soup.get_text(separator=" ")
        content = clean_text(content)

        save_page(url, title, content)

        print("Saved:", title)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    seed_urls = [
        "https://en.wikipedia.org/wiki/Search_engine",
        "https://www.geeksforgeeks.org/python-programming-language/",
        "https://www.w3schools.com/python/",
        "https://en.wikipedia.org/wiki/Web_crawler"
    ]

    for url in seed_urls:
        crawl_page(url)