import os
from dotenv import load_dotenv

load_dotenv()
SSID = os.getenv('SSID')
PSW = os.getenv('SSID_PSW')

def try_connection():
    os.system(f'nmcli device wifi con "{SSID}" password "{PSW}"')


try_connection()