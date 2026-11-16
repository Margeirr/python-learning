import requests
from requests.exceptions import Timeout, ConnectionError
from requests.exceptions import HTTPError
import sys

url = "https://api.github.com/users/torvalds"

def get_api_data(url, params=None):
    try:
        response_get = requests.get(url, params=params, timeout=5)
        response_get.raise_for_status()
    except Timeout:
        return None, "Таймаут"
    except ConnectionError:
        return None, "Нет связи"
    except HTTPError as e:
        return None, f"Ошибка HTTP: {e.response.status_code}"
    return response_get.json(), None

def main():
    data, error = get_api_data(url)
    if error:
        print(error)
        sys.exit()
    name = data.get("name")
    public_repos = data.get("public_repos")
    followers = data.get("followers")
    print(f"У {name} {public_repos} репозиториев и {followers} подписчиков")
    
if __name__ == "__main__":
    main()

