import requests
import pandas as pd


df = pd.read_feather(r"C:\Users\DELL\PGDS\Project\Metro_PdM_Research\Data\Classification.feather")
df = df.drop(columns=["timestamp", "Target"])

# test_data = df.iloc[1].astype("float32").to_list()

# r = requests.post("http://127.0.0.1:8000/Model", json=test_data)
# print(r.status_code)
# print(r.json())

for i in range(10):
    test_data = df.iloc[i].to_dict()
    r = requests.post("http://127.0.0.1:5000/sensor_data", json=test_data)

    print("="*20)
    print(r.status_code)
    print(r.text)
    print(test_data)
    print("="*20)
