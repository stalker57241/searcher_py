from . import app, posts, elastic
from .config import SEARCH_INDEX_NAME

from flask import render_template, request

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/search")
def search():
    query_text = request.args.get("query") or request.form.get("query")
    app.logger.info("query: " + query_text)
    p = posts[:20]
    search_result = elastic.search(
        index=SEARCH_INDEX_NAME,
        query={
            "match": {
                "text": query_text
            }
        }
    )["hits"]["hits"]
    app.logger.info(search_result)
    idx = 0
    for result in search_result:
        app.logger.info(f"id: {idx}" + repr(result['_source']))
        idx += 1

    # print(search_result)
    return render_template("results.html", question=query_text, posts=search_result[:min(20, len(search_result))] )