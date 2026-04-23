from flask import Flask
from .namer import hemlo_actually
from pta_shared.utils.jenkins import get_build

app = Flask("fp-studio")


@app.get("/")
def hello():
    b = get_build("hemlo")
    print(b)
    return hemlo_actually("pepe")
