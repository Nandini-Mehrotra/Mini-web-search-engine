from database import get_all_pages
from text_utils import clean_and_tokenize


def get_suggestions(prefix):
    pages = get_all_pages()
    words_set = set()

    for page in pages:
        page_id, url, title, content = page

        words = clean_and_tokenize(title + " " + content)

        for word in words:
            if word.startswith(prefix.lower()):
                words_set.add(word)

    return list(words_set)[:8]