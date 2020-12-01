#token
TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZTlkYmI3NzdjZDQ3ZTAwNGM2N2RkMGUiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVkYzQ0NGQ1MTQ4NWM1MDA0YzBmYjIxMiJdLCJ0ZW5hbnRJZCI6IjVkYzQ0NGQzMTQ4NWM1MDA0YzBmYjIwYiIsImV4cCI6MTYwNjc4NjcwOCwiaWF0IjoxNjA2NzgzMTA4LCJqdGkiOiJkNWRmYWJlNC1kNzk0LTQ4NGEtYTVjZC1kMDUxZjc3NmRmNDYiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.v0I-mpYON1I0AYmvLvXu5a1CVDXL1FENZs5_Sne9BLkfocSn79DgkMqI8lVpNaOCxeZlRLFYRSkG5PG5x-QWulQ_wmoH5a5MtmI0HEaalhznjwz-rG7MRbBk9OV5U1olyf9NEaSxPxKb_nDflDf7e-sinO8G-Qu8pyOTEmaejStyUW013WnpMvM6tNJG9ginBDk7HgyaTL1F2z5-v1uf74UiHZd3uxxIQM5fQIovTRUjjVYp2MDSGJoxbRVzuzqaapKZpG0Kr-h21oBMAeGC1Kn4ZRMnklKAHcshgPBApAIjpjHT0Fe_bmUAf1dGHdJjhKzn4Z1Ephzd0tf1wOcE6g"
#URL
url='https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
#headers
headers={
    "Accept":"application/json",
    "X-Auth-Token": TOKEN
}
#body
import requests

#resp=requests.request("GET")
#resp=requests.get("GET")

resp=requests.request("GET",url, headers=headers,verify=False)
#la repsuesta de un request va a ser el status code
resultado=resp.text
print(str(type(resultado)))
import json
dict=json.loads(resultado)
print(dict)
