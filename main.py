import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI(title='openCV Visualization')

@app.get('/')
async def index():
    return 'Hello World'


if __name__ == "__main__":
    uvicorn.run(app, debug=True)