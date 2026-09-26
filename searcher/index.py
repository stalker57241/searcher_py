from . import app, posts, elastic, BASE_FOLDER
from .config import SEARCH_INDEX_NAME

from datetime import datetime
from flask import render_template, request

@app.get("/")
def index():
    return render_template("index.html")

def parse_array(text: str) -> list[str]:
    if isinstance(text, list):
        return text
    text = text.removeprefix("[").removesuffix("]")
    elements = text.replace("\'", "").split(",")
    return elements

@app.get("/search")
def search():
    global posts
    query_text = request.args.get("query") or request.form.get("query")
    app.logger.info("query: " + query_text)
    search_result = [x["_source"] for x in elastic.search(
        index=SEARCH_INDEX_NAME,
        query={
            "match": {
                "text": query_text
            }
        }
    )["hits"]["hits"]]
    # app.logger.info(search_result)
    # idx = 0
    # for result in search_result:
    #     app.logger.info(repr(result))
        # idx += 1

    posts_ = [posts[result['id']] for result in search_result]
    # app.logger.info(posts_)
    posts_.sort(key=lambda p: datetime.strptime(p["created_date"], "%Y-%m-%d %H:%M:%S"))
    for postidx in range(len(posts_)):
        posts_[postidx]["rubrics"] = parse_array(posts_[postidx]["rubrics"])
    # search_result.sort(key=lambda p: datetime.strptime(p['date'], "%"))
    # sorted(search_result, lambda elem, next: elem['date'] < next['date'])
    return render_template("query.html", question=query_text, posts=posts_[:min(20, len(posts_))] )

@app.delete("/delete/<int:idx>")
def delete(idx: int):
    elastic.delete(index=SEARCH_INDEX_NAME, id=idx)
    resp = app.make_response(200)
    return resp

@app.get("/openapi.json")
def openapi_spec():
    return app.send_static_file("openapi.json")
