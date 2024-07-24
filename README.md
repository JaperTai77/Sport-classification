# Sport Classifier API

An API which takes an image as input and output the likelihood of sports it belongs to. There are 100 sports in this model, see code/class_label.json for all classes.

## Environment
- Install Python
download from official web
- Install Package
```
pip install -r requirements.txt
```
- Set up Azure key and endpoint, create a file with path code/config.py. Azure key and enpoint is created on Azure Computer Vision [Azure AI Vision](https://azure.microsoft.com/en-us/products/ai-services/ai-vision).
```
def get_endpoint_key():
  return [your endpoint], [your key]
```

## Run
This app is run using FastAPI with uvicorn and is written in main.py. Can call the main.py directly.
```
python code/main.py
```
Sample image can be found in repo. temp.png & temp2.png
