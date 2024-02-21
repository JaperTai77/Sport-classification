from fastapi import FastAPI, Depends, File, UploadFile
import contextlib
from model import ClassificationModel
import cv2
import numpy as np

model = ClassificationModel()

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    model.load_model()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home():
    return {'Home': 'Home'}

@app.post("/image-classification")
async def post_image_classification(image: UploadFile = File(...)) -> dict:
    im = image.file.read()
    loaded_image = cv2.imdecode(np.fromstring(im, np.uint8), cv2.IMREAD_COLOR)
    labels = model.predict(loaded_image)
    return {f'Prediction on image {i+1}': label for i,label in enumerate(labels)} 