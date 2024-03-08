import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from PIL import Image

def CaptionModel(
    image_file = None,
    endpoint = "https://seasiacv3445217.cognitiveservices.azure.com/",
    key = "dc60774c96174c219a59eaec3e5a4ed9"
):
    if image_file is None:
        return {"Caption": "no image"}
    
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    with open(image_file, mode="rb") as image_data:
        result = client.analyze(
            image_data=image_data,
            visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
            gender_neutral_caption=True,
        )
    if result.caption is not None:
        message = f"'{result.caption.text}' (Confidence {result.caption.confidence:.4f})"
    return {"Caption": message}
