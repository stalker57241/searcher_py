import os
from dotenv import load_dotenv

from flask import Flask
from elasticsearch import Elasticsearch

from pathlib import Path

from searcher.posts_grabber import grab_posts
from searcher.config import *

BASE_FOLDER: Path = Path(".").absolute()
DATA_FOLDER: Path = BASE_FOLDER / "data"
POSTS_FILE: Path = DATA_FOLDER / "posts.csv"

posts: list[dict] = grab_posts(POSTS_FILE)

load_dotenv()

elastic = Elasticsearch("http://elasticsearch:9200")
# elastic.info()
app: Flask = Flask(__name__, template_folder= BASE_FOLDER / "templates", static_folder=BASE_FOLDER / "static")

import searcher.index
