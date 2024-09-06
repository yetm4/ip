from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
def get_ip():
    req = f'https://ipgeolocation.abstractapi.com/v1/?api_key={os.getenv("API_KEY")}'
    ip_data = requests.get(req).json()
    return ip_data

if __name__ == "__main__":
    ip_data = get_ip()
    pprint(ip_data)