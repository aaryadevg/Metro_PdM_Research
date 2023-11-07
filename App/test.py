import requests
import pandas as pd


df = pd.read_feather(r"C:\Users\DELL\PGDS\Project\Metro_PdM_Research\Data\Classification.feather")
#df = df.drop(columns=["timestamp", "Target"])

# test_data = df.iloc[1].astype("float32").to_list()

# r = requests.post("http://127.0.0.1:8000/Model", json=test_data)
# print(r.status_code)
# print(r.json())

records = 10

normal = df[df["Target"] == 0].head(records)
pre_fail = df[df["Target"] == 1].head(records)
fail = df[df["Target"] == 2].head(records)

normal = normal.drop(columns=["timestamp", "Target"])
pre_fail = pre_fail.drop(columns=["timestamp", "Target"])
fail = fail.drop(columns=["timestamp", "Target"])

for frame in [normal, pre_fail, fail]:
    for row in range(frame.shape[0]):
        test_data = frame.iloc[row].to_dict()
        r = requests.post("http://127.0.0.1:5000/sensor_data", json=test_data)

        print("="*60)
        print(r.status_code)
        print(r.text)
        print(test_data)
        print("="*60)
