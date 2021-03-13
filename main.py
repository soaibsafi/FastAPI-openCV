from io import BytesIO
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image

ALLOWED_EXTENSION = {'jpg', 'png', 'jpeg'}

app = FastAPI(title='openCV Visualization')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

def read_image(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

@app.get('/')
async def index():
    return 'Hello World'

@app.post('/opencv')
async def openCV(file: UploadFile = File(...)):
    file_extension = file.filename.split('.')[-1] in ALLOWED_EXTENSION
    if not file_extension:
        return 'Filename is invalid.'
    image = read_image(await file.read())
    return 'File'


if __name__ == "__main__":
    uvicorn.run(app, debug=True)