from fastapi import FastAPI
import pathlib
from model import load_model, Model_Meta
import torch

model_dir = pathlib.Path("../Model")
app = FastAPI()
model, meta_data = load_model(model_dir / "wights_raw.pickle")


@app.get("/")
async def root() -> Model_Meta:
    """
    ## Get Model Metadata

    Returns the metadata for the PyTorch classification model.

    ## Returns:
    - Model_Meta.

    ## Example Usage:
    
    ### sh (Bash or also Powershell)
    ```
    $ curl -X GET "http://127.0.0.1:8000/"
    ```
    
    ### Python (Requires Request)
    
    ```
    import requests

    response = requests.get("http://127.0.0.1:8000/")
    if response.status_code == 200:
        model_metadata = response.json()
        print(model_metadata)
    else:
        print(f"Error: {response.status_code} - Unable to retrieve model metadata.")
    ```
    """
    return meta_data












