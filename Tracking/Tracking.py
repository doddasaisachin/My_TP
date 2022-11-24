import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    return response
def get_long_lat():
    ip_address=get_ip()
    response=requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    lon={
        'longitude': response.get('longitude'),
        'latitude' : response.get('latitude')
    }
    return lon

print(get_ip())
print(get_location())
print(get_long_lat())

loc_dict=get_long_lat()
longitude=loc_dict['longitude']
latitude=loc_dict['latitude']

import webbrowser
def open_gmaps():
    return (webbrowser.open(f"https://www.google.com/maps/place/12%C2%B053'40.5%22N+80%C2%B013'39.9%22E/@{latitude},{longitude},17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x4ac1389715ceefca!8m2!3d12.8945695!4d80.2277538"))
open_gmaps()
