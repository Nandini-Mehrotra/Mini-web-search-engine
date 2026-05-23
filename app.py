from flask import Flask, render_template, request
from database import save_search_query, get_search_history
from search_engine import search_with_ranking

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


if __name__ == "__main__":
    app.run(debug=True)