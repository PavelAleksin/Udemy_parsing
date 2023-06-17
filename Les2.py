# Requests
import requests
url = 'https://quotes.toscrape.com/'

resp = requests.get(url)
# print(resp)
# resp.status_code
# resp.content
# print(resp.content.decode('utf-8'))
# resp.text
# resp.headers
# type(resp)
# resp.headers
#resp.headers['content-type']
# resp = requests.get(url,headers={'user-agent':'Mozilla/5.0'})
resp = requests.get('https://httpbin.org/headers')
# resp
# resp.json()
dict(resp.request.headers)