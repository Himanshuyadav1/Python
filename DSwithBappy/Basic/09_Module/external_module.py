# We can install external module using pip
# https://pypi.org/
# pip install fastapi
# pip uninstall fastapi
# pip install uvicorn
# pip uninstall uvicorn
# pip list for getting list of installed module

# will run on not http://0.0.0.0:8080/ on http://0.0.0.0:8080
from fastapi import FastAPI
from uvicorn import run as app_run

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8080)