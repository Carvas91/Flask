import requests

url = 'http://127.0.0.1:5000/index'

response = requests.get(url)


if __name__ == "__main__":
    if response.status_code == 200:
    # Print the response data (JSON format)
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

