import json


def recrusion(data, mul):
    if isinstance(data, dict):
        for k, v in data.items():
            data[k] = recrusion(v, mul)

    elif isinstance(data, float):
        data *= mul

    elif isinstance(data, list):
        for i in data:
            recrusion(i, mul)

    else:
        data = data
    return data

def test():
    with open("mapLocal.json", encoding = "utf-8") as f:
        data = json.load(f)
        recrusion(data)
        print(data)

