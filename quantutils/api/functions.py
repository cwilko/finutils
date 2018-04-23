import json
import pandas
import requests
import base64

class Functions:
    
    def __init__(self, credentials_file):
        credentials = json.load(open(credentials_file))
        self.credentials = credentials

    def call_function(self, name, args, debug=False):        
    	b64token = base64.b64encode(self.credentials["api_key"])
        headers = {'Content-type': 'application/json', 'Authorization':"".join(["Basic ", b64token])}
        url = "".join([self.credentials["endpoint"],name,"?blocking=true"])
        resp = requests.post(url=url, data=json.dumps(args), headers=headers) 

        if debug: 
            print(resp.text)

        return pandas.read_json(json.dumps(json.loads(resp.text)["response"]["result"]), orient='split')