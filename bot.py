import requests
import time

url = "https://galaxy.mobstudio.ru/"

while True:
    try:
        r = requests.get(url)
        print("Galaxy site active:", r.status_code)
    except:
        print("Connection error")

    time.sleep(60)
