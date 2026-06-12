import sqlite3

DB_NAME = "search_engine.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE NOT NULL,
            title TEXT,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_page(url, title, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO pages (url, title, content)
        VALUES (?, ?, ?)
    """, (url, title, content))

    conn.commit()
    conn.close()


def get_all_pages():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, url, title, content FROM pages")
    pages = cursor.fetchall()

    conn.close()
    return pages


def save_search_query(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO search_history (query)
        VALUES (?)
    """, (query,))

    conn.commit()
    conn.close()


#  was facing the issue that the repeated search hostory was showing up in the dashboard, so added the group by and order by clause to show only unique search history and sorted by latest search time
def get_search_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT query, MAX(searched_at) as latest_time
        FROM search_history
        GROUP BY query
        ORDER BY latest_time DESC
        LIMIT 10
    """)

    history = cursor.fetchall()

    conn.close()
    return history


def search_pages(query):
    conn = get_connection()
    cursor = conn.cursor()

    search_text = f"%{query}%"

    cursor.execute("""
        SELECT title, url, content
        FROM pages
        WHERE title LIKE ? OR content LIKE ?
    """, (search_text, search_text))

    results = cursor.fetchall()

    conn.close()
    return results

def get_total_pages():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pages")
    total = cursor.fetchone()[0]

    conn.close()
    return total


def get_total_searches():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM search_history")
    total = cursor.fetchone()[0]

    conn.close()
    return total


def get_recent_pages():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, url
        FROM pages
        ORDER BY created_at DESC
        LIMIT 5
    """)

    pages = cursor.fetchall()

    conn.close()
    return pages

def delete_search_query(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM search_history WHERE query = ?", (query,))

    conn.commit()
    conn.close()


def clear_search_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM search_history")

    conn.commit()
    conn.close()

create_tables()