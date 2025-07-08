import requests
import json

def send_http_request(endpoint, method="POST", payload=None, headers=None):
    method = method.upper()
    headers = headers or {"Content-Type": "application/json"}
    if payload != None:
        payload = json.dumps(payload)
    try:
        response = requests.request(
            method,
            endpoint,
            json=payload if method != "GET" else None,
            headers=headers
        )
        response.raise_for_status()
        print("Response:", response.status_code)
        print("Response content:", response.json())
    except requests.exceptions.HTTPError as e:
        print("HTTP-Error:", e)
    except requests.exceptions.RequestException as e:
        print("Connection failure:", e)
    except ValueError:
        print("Response is not a valid JSON.")
        print("Raw data:", response.text)

if __name__ == "__main__":
    api_url = "http://127.0.0.1:5000/users"
    method = "POST"
    data = {
        "username": "Spiro",
        "email": "Spiro@test.de",
        "is_blocked": 0
    }

    send_http_request(api_url, method=method, payload=data)
