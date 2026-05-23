from flask import Flask, render_template, request
from database import search_pages, save_search_query

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form["query"]
        save_search_query(query)
        results = search_pages(query)

    return render_template("index.html", results=results, query=query)


if __name__ == "__main__":
    app.run(debug=True)