from database import get_all_pages
from text_utils import clean_and_tokenize


def build_inverted_index():
    pages = get_all_pages()
    inverted_index = {}

    for page in pages:
        page_id, url, title, content = page

        words = clean_and_tokenize(title + " " + content)

        for word in words:
            if word not in inverted_index:
                inverted_index[word] = {}

            if page_id not in inverted_index[word]:
                inverted_index[word][page_id] = {
                    "url": url,
                    "title": title,
                    "content": content,
                    "frequency": 0
                }

            inverted_index[word][page_id]["frequency"] += 1

    return inverted_index


if __name__ == "__main__":
    index = build_inverted_index()

    for word, pages in list(index.items())[:20]:
        print(word, "=>", list(pages.keys()))