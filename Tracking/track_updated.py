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
print(get_long_lat())

loc_dict=get_long_lat()
longitude=loc_dict['longitude']
latitude=loc_dict['latitude']

import webbrowser
def open_gmaps():
    return (webbrowser.open(f"https://www.google.com/maps/place/12%C2%B052'16.5%22N+80%C2%B013'26.0%22E/@{latitude},{longitude},17z/data=!3m1!4b1!4m6!3m5!1s0x0:0x5c79646cc337bb51!7e2!8m2!3d12.8712379!4d80.2238744"))
open_gmaps()
