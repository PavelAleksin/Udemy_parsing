authentication
authorization
import requests as r
API_KEY = 'YOUR KEY'
headers= {
    'Authorization':f'Bearer{API_KEY}',
    'Content-Type': 'application/json'
}
url = 'https://api.exchange.coinbase.com/fills'
r.get(url,headers=headers)
basic auth -> username,password
url = 'https://www.httpbin.org/basic-auth/user1/pass2'
auth=('user1','pass2')
resp = r.get(url, auth=auth)