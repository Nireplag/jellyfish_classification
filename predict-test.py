import requests


url = 'http://localhost:9696/predict' # localhost test


image_data = {
    "url": '',
    "path": './dataset/valid/barrel_jellyfish/09.jpg'
}

response = requests.post(url, json=image_data).json()
print(response) # expected response is Barrel_jellyfish


image_data = {
    "url": 'https://github.com/Nireplag/jellyfish_classification/raw/main/44.jpg',
    "path": ''
}


response = requests.post(url, json=image_data).json()
print(response) # expect response is Moon_jellyfish