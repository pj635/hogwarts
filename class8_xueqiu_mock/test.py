import json

def recrusion(data, m = 2):
    if isinstance(data, dict):
        for k, v in data.items():
            data[k] = recrusion(v, m)

    elif isinstance(data, float):
        data *= 2

    elif isinstance(data, list):
        for i in data:
            recrusion(i, m)

    else:
        data = data
    return data


with open("mapLocal.json", encoding="utf-8", mode='r') as f:
    data = json.load(f)
    data = recrusion(data, 2)
with open("mapLocal.json", encoding="utf-8", mode='w') as f:
    json.dump(data, f)
    body = json.dumps(data)
