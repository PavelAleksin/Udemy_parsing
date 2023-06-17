import requests as r
url = 'https://api.sunrisesunset.io/json'
params = {
    'lat':56.8583600,
    'lng':35.9005700,
    'timezone':'Nort',
    'date': 'today'
}
headers={'user-agent':'Mozila/5.0'}
resp = r.get(url, params=params,headers=headers)
resp.json()