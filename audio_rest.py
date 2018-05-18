from __future__ import division
import numpy as np
import sys
import traceback
from skimage.draw import line
from scipy import misc
from scipy.spatial import distance
from collections import Counter
import base64
import requests
import json
import web
import uuid
import time
import signal
import os

import six.moves.urllib_parse

DEBUG = True

class GracefulKiller:
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum, frame):
        print 'exit rest server!!!'

def is_audio_good(audio):
    return True

def process_audio(id, audio, debug= DEBUG) :
    res={}
    res['id']=id

    # empty traces due to scgink data
    if not is_audio_good(audio):
       res['info']="wrong audio data"
       res['status']='error'
       return res
    audio_file_path = 'input.au'
    #convert to other format


    predictor = Predictor(audio)
    #call backend service
    res_decision = predictor.predict()

    if debug :
        print "_________________________________________________"
        print res_decision
        print "_________________________________________________"
    res['status']="succuss"
    res['info']=''
    res['decision']=res_decision
    return res


urls = (
     '/api/audio/', 'HeartBeatHanler',
     '/RecoServices/image/ADDRESS/USA', 'HeartBeatHanler',
)

app = web.application(urls, globals())

def size(b64string):
    return (len(b64string) * 3) / 4 - b64string.count('=', -2)


class HeartBeatHanler:

    def POST(self):
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Methods', '*')

        data = json.loads(web.data())
        encodedImgdata = data["encodedAudio"]

        data_type = data['type']
        print 'data_type: ', data_type

        import StringIO

        output = StringIO.StringIO()
        output.write(base64.b64decode(encodedImgdata))
        img= misc.imread(output)

        request_id = str(uuid.uuid4())
        request_audio_name = "data/"+request_id + ".au"
        #save audio

        #process audio

        result={"data":
                   {
                      "RestServer": "ali-id",
                      "quality": "good",
                      "process_t": "1467059712633",
                      "heart_rate_max": "100",
                      "heart_rate_min": "72",
                      "CAD_score": 75
                   }
               }
        return json.dumps(result)

    def OPTIONS(self):
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Headers', 'Content-Type')
        web.header('Access-Control-Allow-Methods', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        return


class Predictor(object):
    def __init__(self, audio):
        self.audio = audio

    def predict(self):
        return True

if __name__ == "__main__":
    app.run()
