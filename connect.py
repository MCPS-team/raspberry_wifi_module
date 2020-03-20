import os
import requests
from dotenv import load_dotenv

load_dotenv()
SSID = os.getenv('SSID')
PSW = os.getenv('SSID_PSW')

def try_connection():
    return os.system(f'nmcli device wifi con "{SSID}" password "{PSW}"')


try_connection()

payload = {"data": [{
    "bumpID": "xxx",
    "latitude": 52.3547498,
    "longitude": 4.8339211,
    "start_at": "2020-03-18T13:58:56.110Z", 
    "end_at": "2020-03-18T13:58:56.110Z",
    "attached_sensors_data": [{
        "timestamp": 1584610317178,
        "x": 0.166348984,
        "y": 8.52214945,
        "z": 5.461383058,
        "latitude": 52.3547498,
        "longitude": 4.8339211
    }]
},
{
    "bumpID": "xxx",
    "latitude": 52.3547498,
    "longitude": 4.8339211,
    "start_at": "2020-03-18T13:58:56.110Z", 
    "end_at": "2020-03-18T13:58:56.110Z",
    "attached_sensors_data": [{
        "timestamp": 1584610317178,
        "x": 0.166348984,
        "y": 8.52214945,
        "z": 5.461383058,
        "latitude": 52.3547498,
        "longitude": 4.8339211
    }]
}]}


IP = "10.42.0.1"
PORT = "3000"
r = requests.post("http://{}:{}/api/upload/bump-data".format(IP, PORT), json=payload)
if  r.status_code == 200 : 
	print("Data upload has been succesfully!")

VIDEO_PATH = "/home/pi/MPCS2020/video_module/frames" 
fs = list(os.walk(VIDEO_PATH))

#pop the folder root
fs.pop(0)

for directory in fs:
	folder_name = directory[0].split('/')[-1]
	files = []
	[files.append((folder_name, open("{}/{}".format(directory[0], file), 'rb'))) for file in directory[2]] 
	requests.post("http://{}:{}/api/upload/images".format(IP,PORT), files=files)
	print("folder sent..")

