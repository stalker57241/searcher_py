import csv

def grab_posts(file: Path) -> list[dict]:
    data = []
    with open(file, "r") as f:
        _data = csv.DictReader(f)
        idx = 0
        for elem in _data:
            elem["id"] = idx
            idx += 1
            data.append(elem)
    # print(data)
    return data
