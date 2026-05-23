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


def get_search_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT query, searched_at
        FROM search_history
        ORDER BY searched_at DESC
        LIMIT 10
    """)

    history = cursor.fetchall()

    conn.close()
    return history


create_tables()