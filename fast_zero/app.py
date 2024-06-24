from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return 'Eu quero um boy, bora frescar'
