import re

STOPWORDS = {
    "the", "is", "a", "an", "and", "or", "of", "to", "in",
    "on", "for", "with", "as", "by", "at", "from", "this",
    "that", "it", "be", "are", "was", "were"
}


def clean_and_tokenize(text):
    text = text.lower()

    words = re.findall(r'\b[a-z]+\b', text)

    filtered_words = []

    for word in words:
        if word not in STOPWORDS:
            filtered_words.append(word)

    return filtered_words