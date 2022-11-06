from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hi, welcome to module app install"