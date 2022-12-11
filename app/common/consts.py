import pathlib


BASE_PATH = pathlib.Path(__file__).resolve().parent.parent
WORKSPACE_PATH = BASE_PATH.parent

HOST = "0.0.0.0"
PORT = 8000

if HOST == "0.0.0.0":
    BASE_URL = "https://www.primers.ml"
else:
    BASE_URL = f"http://{HOST}:{PORT}"