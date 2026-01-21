# Sport Classifier API

Sport Classification is a FastAPI service that takes an uploaded image and returns the top-N predicted sports with probabilities.

The classifier is a TensorFlow model trained to recognize 100 sports classes.

In addition to classification, the API also provides image captioning endpoint powered by Azure AI Vision.

## File Structure

```
Sport-classification/
├── code/
│   ├── api.py                # FastAPI app (routes)
│   ├── main.py               # Uvicorn runner (port 8080)
│   ├── model.py              # TensorFlow classification wrapper
│   ├── AzureAPI.py           # Azure AI Vision caption wrapper
│   ├── class_label.json      # 100 class labels
│   └── sportsEN_V2_0219_2.h5  # Model weights
├── requirements.txt
├── Dockerfile
├── Sports_Classification.ipynb
├── temp.png
└── temp2.png
```

## Demo Images

Sample images are included in this repo:

- `temp.png`
- `temp2.png`

## Environment (Python)
- Install Package
```
pip install -r requirements.txt
```
- Configure Azure AI Vision for `/image_caption`
```
def get_endpoint_key():
  return [your endpoint], [your key]
```
You can create an Azure key/endpoint from: [Azure AI Vision](https://azure.microsoft.com/en-us/products/ai-services/ai-vision).

 - Run locally
This app is run using FastAPI with uvicorn and is written in main.py. Can call the main.py directly.
```
python code/main.py
```

## API Endpoints

### 1) Image Classification

`POST /image-classification`

- **Form field**: `image` (file)
- **Query param**: `numberofpred` (int, default `5`)

Example (curl):

```bash
curl -X POST "http://127.0.0.1:8080/image-classification?numberofpred=5" \
  -F "image=@temp.png"
```

### 2) Image Caption (Azure AI Vision)

`POST /image_caption`

- **Form field**: `image` (file)

Example (curl):

```bash
curl -X POST "http://127.0.0.1:8080/image_caption" \
  -F "image=@temp.png"
```
