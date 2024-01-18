import requests


url = 'http://localhost:9696/predict' # localhost test


image_data = {
    "url": '',
    "path": './dataset/valid/barrel_jellyfish/09.jpg'
}


response = requests.post(url, json=image_data).json()
print(response) # expect output 0