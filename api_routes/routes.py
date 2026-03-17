import requests

base_url = "https://api.thecatapi.com/v1"


def get_gatos():
    url_gato = f"{base_url}/breeds"

    headers = {
        "x-api-key": "live_ekGJ2mas5u6NMrrdDBsGvZnimhixlJlHUKPctOJ0giGkXqwB2Hci4NPSLaVJ0yVW"
    }

    result = requests.get(url_gato, headers=headers)
    return result.json()

def get_image():
    url_image = f"https://api.thecatapi.com/v1/images/search"

    result = requests.get(url_image)

    return result.json()[0]
