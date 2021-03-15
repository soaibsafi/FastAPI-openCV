from io import BytesIO
import os

import cv2
import numpy as np
import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse


ALLOWED_EXTENSION = {'jpg', 'png', 'jpeg'}
UPLOAD_FOLDER = 'static/uploads'
DOWNLOAD_FOLDER = 'static/downloads'

app = FastAPI(title='openCV Visualization')

@app.get('/')
async def index():
    return 'Hello World'

@app.post('/gaussian-blur')
async def _gaussian_blur(file: UploadFile = File(...)):
    file_extension = file.filename.split('.')[-1] in ALLOWED_EXTENSION
    if not file_extension:
        return 'File type is invalid.'
    image = await file.read()
    nparr = np.fromstring(image, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    image = cv2.GaussianBlur(image, (5,5), 0, 0)
    res, img_png = cv2.imencode('.png', image)
    #encoded_img = base64.b64encode(img_png)

    cv2.imwrite(f"{UPLOAD_FOLDER}/{file.filename}", image)

    return StreamingResponse(BytesIO(img_png.tobytes()), media_type="image/png")



if __name__ == "__main__":
    uvicorn.run(app, debug=True)