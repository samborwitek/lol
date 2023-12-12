import requests


api_key = RGAPI-fa205826-b426-417b-9cb6-2254f44355b5
api_url = 'https://github.com/samborwitek/lol.git'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

# Make a GET request to the API
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")