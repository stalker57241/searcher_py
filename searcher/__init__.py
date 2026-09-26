from flask import Flask

BASE_FOLDER = ".."
DATA_FOLDER = f"{BASE_FOLDER}/data"
POSTS_FILE = f"{DATA_FOLDER}/posts.csv"

app = Flask(__name__, template_folder=f"{BASE_FOLDER}/templates", static_folder=f"{BASE_FOLDER}/static")

import searcher.index
