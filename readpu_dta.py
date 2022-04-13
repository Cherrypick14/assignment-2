import json
import requests

lnk_url = 'https://kidadl.com/articles/space-puns-that-are-out-of-this-world'

def dta_read(lnk_url):
    feedback= requests.get(lnk_url).text
    res_content= json.load(feedback)
    return res_content

