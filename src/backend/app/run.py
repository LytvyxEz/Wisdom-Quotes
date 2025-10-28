from uvicorn import run


if __name__ == '__main__':
    # init_db()
    run(app='main:app', host='localhost', port=8080, reload=True)