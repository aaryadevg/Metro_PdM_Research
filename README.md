# Failure Prediction for APU's on a Metro System

## Abstract

Predictive maintenance is crucial for ensuring the reliable operation of metro transportation systems, enhancing passenger safety, and minimizing service disruptions. This research focuses on the challenging task of predicting failures on the Air Processing Unit (APU) in a metro system at least two hours in advance. The APU is a critical component responsible for compressing and storing air for various metro functions, such as suspension.

The study includes a comprehensive comparison of machine learning and deep learning models, such as Support Vector Machines (SVM), Decision Trees, and Long Short-Term Memory (LSTM) networks. Evaluation is performed on the MetroPT Dataset published by Veloso et al. in 2022 [Dataset](https://doi.org/10.1038/s41597-022-01877-3).

Considering performance metrics like accuracy, precision, recall, and F1-Score for classification. This provides valuable insights into the applicability of these models in predicting impending failures.

In addition, a practical demonstration of a web API is introduced to showcase how the model would be deployed in a real-world scenario. This API serves as evidence of the feasibility of deploying predictive maintenance models in production settings.

It is important to note that while the research offers valuable insights into model performance and deployment readiness, it does not propose a final production model. This limitation is due to the complex domain knowledge required for selecting an optimal model, and to keep the paper more general since the requirements of various transportation companies may differ. Nevertheless, the findings contribute to ongoing efforts to enhance metro system reliability and safety through proactive failure prediction.

## Table of Contents

- [Failure Prediction for APU&#39;s on a Metro System](#failure-prediction-for-apus-on-a-metro-system)
  - [Abstract](#abstract)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
    - [Model Service Dependencies](#model-service-dependencies)
    - [Admin Service Dependencies](#admin-service-dependencies)
    - [Frontend Dependencies](#frontend-dependencies)
    - [Displaying SQL Table Data](#displaying-sql-table-data)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contact](#contact)
  - [Timeline](#timeline)

## Getting Started

To get started with the research paper repository, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/aaryadevg/Metro_PdM_Research.git
   cd Metro_PdM_Research
   ```
2. Launch the application

```bash
  python start.py
```

Now you can explore the research paper repository and, if interested, run the API demo by launching both services in separate terminals.

## Prerequisites

Before running the code or replicating the experiments, make sure you have the following prerequisites installed:

- Python 3.x
- [PyTorch](https://pytorch.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [PyTorch Lightning](https://www.pytorchlightning.ai/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [imbalanced-learn](https://imbalanced-learn.org/stable/)
- [Tensorboard](https://www.tensorflow.org/tensorboard)

### Model Service Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- PyTorch (already included in the main prerequisites)

### Admin Service Dependencies

- [Flask](https://flask.palletsprojects.com/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

### Frontend Dependencies

- [Bootstrap](https://getbootstrap.com/)

### Displaying SQL Table Data

- [Grid.js](https://gridjs.io/) - Used for displaying SQL table data in HTML

## Usage

To replicate the results of the research paper, follow these steps:

1. Run the Jupyter notebook for model training and evaluation:

   ```bash
   cd ML
   jupyter notebook Modeling.ipynb
   ```

   Execute all the cells in the `Modeling.ipynb` notebook to train and evaluate the machine learning models.
2. Run the Jupyter notebook for testing with resampled data:

   ```bash
   cd ML_Testingv2
   jupyter notebook Resampled.ipynb
   ```

   Execute all the cells in the `Resampled.ipynb` notebook to perform testing with resampled data.
3. Run the LSTM notebook for additional analysis:

   ```bash
   jupyter notebook LSTM2.ipynb
   ```

   Execute all the cells in the `LSTM2.ipynb` notebook for further analysis using Long Short-Term Memory networks.

You need to download and install Jupyter notebooks or use the Jupyter VS Code extension

- [Jupyter](https://jupyter.org/install)
- [VS Code extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

## Contact

Feel free to reach out to me for any questions or request for collaboration to me via aaryadevg@gmail.com

## Timeline

- [X] Find Papers on LSTM for PdM
- [X] Finish Review
- [X] Select algorithms to compare
- [X] Write about the Dataset and Perform EDA
- [X] Make Presentation for DOT internal
- [X] Balance dataset
- [X] Implement Algorithms (SVM, Decision Tree, Random Forest, Neural Net, LSTM)
- [X] Test on Dataset (Evaluation)
- [X] Select an Approach for API (Chose a Micro service architecture)
- [X] Build API
- [X] Build Admin app
  - [X] Display data in table
  - [X] Search
  - [X] Sort
  - [X] Form to Mark Failure
  - [ ] Docker?
  - [X] Dashboard
- [ ] Try RUL Approach
- [ ] Evaluate RUL
- [X] Finish Off Paper
- [X] Finish Log Book
