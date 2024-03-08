from fastapi import FastAPI, Depends, File, UploadFile
import contextlib
from model import ClassificationModel
from AzureAPI import CaptionModel
import numpy as np
from PIL import Image
import io

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
async def post_image_classification(image: UploadFile=File(...), numberofpred: int=5) -> dict:
    # openCV
    #im = image.file.read()
    #loaded_image = cv2.imdecode(np.fromstring(im, np.uint8), cv2.IMREAD_COLOR)
    contents = image.read()
    loaded_image = Image.open(io.BytesIO(contents))
    loaded_image = np.array(loaded_image.resize((224,224)))
    loaded_image = np.float32(loaded_image/255)
    labels = model.predict(loaded_image, n=numberofpred)
    return {f'Prediction on image {i+1}': label for i,label in enumerate(labels)}

@app.post("/image_caption")
async def post_image_caption(image: UploadFile=File(...)) -> dict:
    contents = image.filename
    message = CaptionModel(contents)
    return message
