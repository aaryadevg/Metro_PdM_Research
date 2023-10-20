import torch
from pydantic import BaseModel
import os
from datetime import datetime

class ModelPrediction(BaseModel):
    """
    ModelPrediction is a data model representing the prediction result for a single input.

    ## Attributes:
    - predicted_label (int): The predicted label or class for the input.
    - predicted_class (str): The predicted class name.
    - raw_out (list[float]): The raw output values.
    - probabilities (list[float]): The class probabilities calculated using the Softmax function.
    - confidence (float): The highest probability among the class probabilities.
    """
    predicted_label: int
    predicted_class: str
    raw_out: list[float]
    probabilities: list[float]
    confidence: float


class ModelMeta(BaseModel):
    """
    ## About
    Model_Meta is a Pydantic data model to store metadata related to the classification model used by this API.

    ## Attributes:
    - `name` The name of the model.
    - `created_date`: The date and time when the model was created, in ISO 8601 format.
    - `n_params`: The number of parameters in the model.
    - `features`: The number of features used by the model for classification.
    """
    name: str
    created_date: datetime
    n_params: int
    features: int


class NN_Classifier(torch.nn.Module):
    def __init__(self, n_inputs=16) -> None:
        super().__init__()
        self.model = torch.nn.Sequential(
            torch.nn.Linear(n_inputs, 256),
            torch.nn.Tanh(),
            torch.nn.Linear(256, 64),
            torch.nn.Tanh(),
            torch.nn.Linear(64, 64),
            torch.nn.Tanh(),
            torch.nn.Linear(64, 3),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)


def _calc_param(model: torch.nn.Module) -> int:
    return sum(map(lambda x: x.numel(), model.parameters()))


def load_model(path: str) -> tuple[torch.nn.Module, ModelMeta]:
    location = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    state = torch.load(path, map_location=location)

    model = NN_Classifier()
    model.load_state_dict(state)
    model.eval()

    meta = ModelMeta(
        name=type(model).__name__,
        created_date=datetime.fromtimestamp(os.path.getctime(path)),
        n_params=_calc_param(model),
        features=16,
    )  # Features is hard coded right now

    return (model, meta)
