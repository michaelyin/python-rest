import base64
import os
import sys
import requests

# Pass the image data to an encoding function.
def encode_image(imagename):
  with open(imagename, 'rb') as f:
      image_content = f.read()
  f.close()
  return base64.b64encode(image_content)

_url= 'http://39.108.8.106:8080/api/audio'
_url = 'http://localhost:8080/api/audio'
headers = dict()

#headers['accept']='application/json;charset=UTF-8'
headers['Content-Type']='application/json;charset=UTF-8'
params=None

data= dict()
data['type']='JPEG'
data['encodedAudio']=encode_image('/home/michael/git/OCRCloud/WyunOcrClient/src/test/resources/jpgimages/2.jpg')

response = requests.request( 'post', _url, json = data, headers = headers, params = params )

print( "Status code: %d" % ( response.status_code ) )
print( "Message: %s" % ( response.json() ) )
