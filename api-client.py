import requests
from requests.exceptions import Timeout, ConnectionError
from requests.exceptions import HTTPError

url_get = "https://api.github.com/users/torvalds"
url_post = "https://httpbin.org/post"
payload = {"name": "Margeirr", "status": "learning"}

def make_request(url, method="GET", payload=None):
    try:
        if method == "GET":
            response = requests.get(url, timeout=5)
        elif method == "POST":
            response = requests.post(url, json=payload, timeout=5)
        else:
            return None, "Неизвестный метод"
        response.raise_for_status()
    except Timeout:
        return None, "Таймаут"
    except ConnectionError:
        return None, "Нет связи"
    except HTTPError as e:
        return None, f"Ошибка HTTP: {e.response.status_code}"
    return response.json(), None

def main(url, method="GET", payload=None):
    data, error = make_request(url, method=method, payload=payload)
    if error:
        print(error)
        return
    print(type(data))
    print(data)

if __name__ == "__main__":
    main(url_get)
    main(url_post, method="POST", payload=payload)


