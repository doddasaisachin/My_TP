In the above code, we have two functions – get_ip() and get_location()

get_ip() function
As per the API documentation of ipify, we need to make a GET request on
https://api.ipify.org?format=json 
to get a JSON response that looks like this:
{
  "ip": "117.214.109.137"
}

get_location() function
As per the API documentation of ipapi, we need to make a GET request on 
https://ipapi.co/{ip}/{format}/ 
to get location information for a particular IP address.

This function internally calls the get_ip() function to 
get the IP address and then makes a GET request on the URL with the IP address.
 This API returns a JSON response that looks like this:


{
    "ip": "117.214.109.137",
    "version": "IPv4",
    "city": "Gaya",
    "region": "Bihar",
    "region_code": "BR",
    "country": "IN",
    "country_name": "India",
    "country_code": "IN",
    "country_code_iso3": "IND",
    "country_capital": "New Delhi",
    "country_tld": ".in",
    "continent_code": "AS",
    "in_eu": false,
    "postal": "823002",
    "latitude": 24.7935,
    "longitude": 85.012,
    "timezone": "Asia/Kolkata",
    "utc_offset": "+0530",
    "country_calling_code": "+91",
    "currency": "INR",
    "currency_name": "Rupee",
    "languages": "en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc",
    "country_area": 3287590,
    "country_population": 1352617328,
    "asn": "AS9829",
    "org": "National Internet Backbone"
}