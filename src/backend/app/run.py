from uvicorn import run
from db import init_db


if __name__ == '__main__':
    init_db()
    run(app='main:app', host='localhost', port=8080, reload=True)