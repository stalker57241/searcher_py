import csv
from . import POSTS_FILE

def grab_posts() -> list[dict]:
    data = []
    with open(POSTS_FILE, "r") as f:
        data = csv.DictReader(f)
    print(data)