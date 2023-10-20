from fastapi import FastAPI
from model import load_model, ModelMeta, ModelPrediction
import torch
import numpy as np
import joblib

app = FastAPI()
model, meta_data = load_model(".\wights_raw.pickle")

class_mapping = {0: "Normal", 1: "Pre-Failure", 2: "Failure"}
scaler = joblib.load(".\scaler.pkl")


@app.get("/Model")
async def get_model() -> ModelMeta:
    """
    ## Get Model Metadata

    Returns the metadata for the PyTorch classification model.

    ## Returns:
    - Model_Meta.

    ## Example Usage:

    ### sh (Bash or also Powershell)
    ```
    $ curl -X GET "http://127.0.0.1:8000/Model"
    ```

    ### Python (Requires Request)

    ```
    import requests

    response = requests.get("http://127.0.0.1:8000/Model")
    if response.status_code == 200:
        model_metadata = response.json()
        print(model_metadata)
    else:
        print(f"Error: {response.status_code} - Unable to retrieve model metadata.")
    ```
    """
    return meta_data


@app.post("/Model")
async def predict(data: list[float]) -> ModelPrediction:
    """
    ## Predict using PyTorch Classification Model

    Predicts the class and provides confidence scores for a single input data point.
    
    **NOTE:** A Single data point consists of a List of 16 Numbers (float)
    
    Just for testing this is a value from the data:
    
    ` [-0.01200103759765625, 9.7578125, 9.7578125, -0.0279998779296875, 1.576171875, 63.34375, 19.046875, 3.955078125, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]`

    ## Args:
    - data (list[float]): The input data as a list of floats.

    ## Returns:
    - ModelPrediction: A prediction result that includes the predicted class, label, raw output, class probabilities, and confidence score.

    ## Example Usage:
    - Using 'requests' module in Python:

    ```python
    import requests

    input_data = [-0.01200103759765625, 9.7578125, 9.7578125, -0.0279998779296875, 1.576171875, 63.34375, 19.046875, 3.955078125, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    response = requests.post("http://your-server:port/predict", json={"data": input_data})

    if response.status_code == 200:
        prediction_result = response.json()
        print(prediction_result)
    else:
        print(f"Error: {response.status_code} - Unable to make a prediction.")
    ```
    """
    data_t = np.array(data, dtype=np.float32)
    data_t = scaler.transform(data_t.reshape(-1, 16))
    
    data_t = torch.tensor(data_t, dtype=torch.float32)
    
    preds = model(data_t).detach().cpu().numpy()[0]
    epred = np.exp(preds)
    probs = epred / epred.sum()
    pclass = np.argmax(probs)
    conf = np.max(probs)

    lbl = class_mapping[int(pclass)]
    
    return ModelPrediction(
        predicted_class=lbl,
        predicted_label=int(pclass),
        raw_out=preds.tolist(),
        probabilities=probs.tolist(),
        confidence=conf,
    )

#print(predict([-0.01200103759765625, 9.7578125, 9.7578125, -0.0279998779296875, 1.576171875, 63.34375, 19.046875, 3.955078125, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]))