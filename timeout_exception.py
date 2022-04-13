#    send a request, deny a resonse and raise an exception on timeout
import requests

def timeout_request():

    try:
        c = requests.get('https://github.com/', timeout= 0.0001)
    #   print(c.text)
    except requests.exceptions as error:
        print(error)

    try:
        c = requests.get('https://github.com/', timeout=1.0)
        print("you're connected!,,,,")
    except requests.exceptions as error:
        print(error)
