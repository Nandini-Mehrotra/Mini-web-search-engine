from flask import Flask, render_template, request, jsonify
from database import save_search_query, get_search_history
from search_engine import search_with_ranking
from autocomplete import get_suggestions
from crawler import crawl_url_from_admin
from database import get_total_pages, get_total_searches, get_recent_pages
from flask import redirect, url_for
from database import delete_search_query, clear_search_history

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form["query"]
        save_search_query(query)
        results = search_with_ranking(query)

    history = get_search_history()

    return render_template(
        "index.html",
        results=results,
        query=query,
        history=history
    )


@app.route("/suggest")
def suggest():
    prefix = request.args.get("q", "")

    if not prefix:
        return jsonify([])

    suggestions = get_suggestions(prefix)

    return jsonify(suggestions)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    message = ""

    if request.method == "POST":
        url = request.form["url"]
        crawl_url_from_admin(url)
        message = "URL crawled and saved successfully!"

    return render_template("admin.html", message=message)

@app.route("/dashboard")
def dashboard():
    total_pages = get_total_pages()
    total_searches = get_total_searches()
    recent_pages = get_recent_pages()
    history = get_search_history()

    return render_template(
        "dashboard.html",
        total_pages=total_pages,
        total_searches=total_searches,
        recent_pages=recent_pages,
        history=history
    )

@app.route("/delete-history", methods=["POST"])
def delete_history():
    query = request.form["query"]
    delete_search_query(query)
    return redirect(url_for("home"))


@app.route("/clear-history", methods=["POST"])
def clear_history():
    clear_search_history()
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)