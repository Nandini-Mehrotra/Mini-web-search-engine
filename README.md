# TechSearch - Full Stack Mini Search Engine

TechSearch is a full-stack mini search engine that crawls selected websites, stores webpage content, builds a searchable index, and returns ranked search results with snippets.

## Features

- Web crawler using Python
- SQLite database for storing crawled pages
- Inverted index for faster search
- Ranking system based on title match and word frequency
- Search result snippets
- Autocomplete suggestions
- Search history
- Admin panel to crawl new URLs
- Dashboard analytics
- Clean frontend using HTML, CSS, and JavaScript

## Tech Stack

- Python
- Flask
- SQLite
- BeautifulSoup
- Requests
- HTML
- CSS
- JavaScript
- Git & GitHub

## CS Concepts Used

- DBMS: SQLite database, tables, queries
- Computer Networks: HTTP requests, URLs, response codes
- DSA: inverted index, dictionaries, ranking
- OS: multithreading can be added for faster crawling
- NLP: tokenization, stopword removal, text cleaning
- Full Stack Development: frontend, backend, database integration

## How It Works

1. Admin enters a website URL.
2. Crawler visits the webpage.
3. It extracts title, text content, and links.
4. Extracted data is saved in SQLite.
5. User searches a keyword.
6. The query is cleaned and matched using an inverted index.
7. Results are ranked and displayed with snippets.

## Pages

- `/` - Search page
- `/admin` - Add URL and crawl webpage
- `/dashboard` - View analytics

## Run Locally

```bash
git clone YOUR_REPO_LINK
cd mini-web-search-engine
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py