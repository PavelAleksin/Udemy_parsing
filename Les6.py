HTTPbin
import requests as r
r.delete("https://www.httpbin.org/delete").json()
r.patch("https://www.httpbin.org/patch").json()
r.put("https://www.httpbin.org/put").json()
r.post("https://www.httpbin.org/post").json()
HEAD
OPTIONS

import requests as r
resp = r.post("https://www.httpbin.org/post",data={'key1':'value1'})
resp.json()
resp = r.post("https://www.httpbin.org/post",data={
                                                'key1':'value1',
                                                'key2':'avalue with'
                                                })
resp.request.body
resp = r.post("https://www.httpbin.org/post",data='some text')
resp.request.body
resp = r.post("https://www.httpbin.org/post",json={
                                                'key1':'value1',
                                                'key2':'avalue with'
                                                })

resp.json()
resp.request.body
JSON -> JavaScript Object Notation
