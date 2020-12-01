import requests
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
#Content type: formato contenido del mensaje
#Accept: Formato en el q voy a recibir la respuesta
headers={
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
respuesta=requests.post(url,auth=('devnetuser','Cisco123!'),headers=headers)
token=respuesta.text


import json
token=json.loads(token)
type(token)
print(token["Token"])