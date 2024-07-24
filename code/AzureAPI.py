import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from PIL import Image
from config import get_endpoint_key

endpoint, key = get_endpoint_key()

def CaptionModel(
    image_file = None,
    endpoint = endpoint,
    key = key
):
    if image_file is None:
        return {"Caption": "no image"}
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )
    #with open(image_file, mode="rb") as image_data:
    result = client.analyze(
        image_data=image_file,
        visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ, VisualFeatures.OBJECTS],
        gender_neutral_caption=True,
        language='en'
    )
    if result.caption is not None:
        message = f"'{result.caption.text}'"
        confidence = f"{result.caption.confidence:.4f}"
        objects = result.objects.as_dict()
    return {"Caption": message, "Confidence": confidence, "Object": objects['values']}
