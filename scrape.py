import json
from pprint import pprint
import requests


with open('dresses.json') as f:
    raw_data = json.load(f)

dresses = raw_data['products']

for index, dress in enumerate(dresses):
    image_url = dress['images'][0]['src']
    print(image_url)
    img_data = requests.get(image_url).content
    img_name = './dresses/img_%s.jpg'%(index)

    with open(img_name, 'wb') as handler:
        handler.write(img_data)
# pprint(data)