import requests

url = 'https://jellyfish-classification-2rtrkbrwna-uc.a.run.app/predict' # GCP deploy


image_data = {
    "url": 'https://github.com/Nireplag/jellyfish_classification/raw/main/dataset/valid/barrel_jellyfish/09.jpg',
    "path": ''
}

response = requests.post(url, json=image_data).json()
print(response) # expected response is Barrel_jellyfish


image_data = {
    "url": 'https://github.com/Nireplag/jellyfish_classification/raw/main/dataset/valid/Moon_jellyfish/44.jpg',
    "path": ''
}

response = requests.post(url, json=image_data).json()
print(response) # expect response is Moon_jellyfish