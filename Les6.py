HTTPbin
import requests as r
r.delete("https://www.httpbin.org/delete").json()
r.patch("https://www.httpbin.org/patch").json()
r.put("https://www.httpbin.org/put").json()
r.post("https://www.httpbin.org/post").json()
HEAD
OPTIONS

