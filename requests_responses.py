#   a program to get the requests and response from a webpage x raw socket response from servver

import requests

c = requests.get('https://www.linkedin.com/in/cheryl-owala-423731191/')
print(c.text)
print("\n===========")

print(c.content)

r = requests.get("https://api.github.com/events", stream= True)
print(r.raw)
print(r.raw.read(15))
  