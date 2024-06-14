import requests

def fetch_earthquake_data():
    url = 'https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch data: {response.status_code}')
