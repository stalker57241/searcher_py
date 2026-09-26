import sys

from . import app, elastic
from elasticsearch import helpers, BadRequestError
from .posts_grabber import grab_posts
from . import posts
from searcher.config import *

def index_posts():
    for i in range(len(posts)):
        yield {
            "_index": SEARCH_INDEX_NAME,
            "_id": i,
            "_source": {
                "id": i,
                "text": posts[i].get("text", "None")
            }
        }

def update_posts():
    try:
    # if not elastic.indices.exists(index=SEARCH_INDEX_NAME):
        elastic.indices.create(index=SEARCH_INDEX_NAME, mappings=SEARCH_INDEX_MAPPINGS)
    except BadRequestError as err:
        print(err)
    finally:
        helpers.bulk(elastic, index_posts())

if __name__ == "__main__":
    update_posts()
    app.run(host="0.0.0.0", port=5000, debug=sys.argv.count("--debug") > 0)
