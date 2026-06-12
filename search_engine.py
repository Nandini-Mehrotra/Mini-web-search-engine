from urllib.parse import urlparse
from indexer import build_inverted_index
from text_utils import clean_and_tokenize


def get_source_name(url):
    domain = urlparse(url).netloc

    if "wikipedia" in domain:
        return "Wikipedia"
    elif "w3schools" in domain:
        return "W3Schools"
    elif "geeksforgeeks" in domain:
        return "GeeksforGeeks"
    elif "quotes" in domain:
        return "Quotes"
    elif "books" in domain:
        return "Books"
    else:
        return domain


def calculate_score(query_words, page_data):
    score = 0
    title = page_data["title"].lower()

    for word in query_words:
        frequency = page_data["frequency"]

        if word in title:
            score += 10

        score += frequency

    return score


def create_snippet(content, query_words):
    content_lower = content.lower()

    for word in query_words:
        position = content_lower.find(word)

        if position != -1:
            start = max(position - 80, 0)
            end = min(position + 220, len(content))
            return content[start:end] + "..."

    return content[:300] + "..."


def search_with_ranking(query, selected_source="All"):
    inverted_index = build_inverted_index()
    query_words = clean_and_tokenize(query)

    results_dict = {}

    for word in query_words:
        if word in inverted_index:
            pages = inverted_index[word]

            for page_id, page_data in pages.items():
                source = get_source_name(page_data["url"])

                if selected_source != "All" and source != selected_source:
                    continue

                if page_id not in results_dict:
                    results_dict[page_id] = page_data.copy()
                    results_dict[page_id]["score"] = 0
                    results_dict[page_id]["source"] = source

                results_dict[page_id]["score"] += calculate_score(query_words, page_data)

    final_results = []

    for page_id, data in results_dict.items():
        snippet = create_snippet(data["content"], query_words)

        final_results.append({
            "title": data["title"],
            "url": data["url"],
            "snippet": snippet,
            "score": data["score"],
            "source": data["source"]
        })

    final_results.sort(key=lambda x: x["score"], reverse=True)

    return final_results