import json
from jinja2 import Environment, FileSystemLoader

with open ("restaurants.json", "r") as d:
    restaurants=json.load(d)

    fileLoader = FileSystemLoader("templates")
    env = Environment(loader=fileLoader)

    rendered = env.get_template("dynamic_abrilq.html").render(restaurants = restaurants)

    fileName = "index.html"

    with open(f"./site/{fileName}", "w") as f:
        f.write(rendered)


