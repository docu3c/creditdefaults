from flask import Flask, render_template, request
import json
import os
import ssl
import requests


app = Flask(__name__)

         

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])

def predict():
    request.method == 'POST'
    data = {
                
                        "input_data": {
                                "columns": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],
                            "index": [0, 1],
                            "data": [
                                    [20000,2,2,1,24,2,2,-1,-1,-2,-2,3913,3102,689,0,0,0,0,689,0,0,0,0],
                                    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8]
                                ]
                        }
            
                        
            }
            
        
        
    def allowSelfSignedHttps(allowed):
        # bypass the server certificate verification on client side
        if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
            ssl._create_default_https_context = ssl._create_unverified_context
    
    allowSelfSignedHttps(True)
    
    body = str.encode(json.dumps(data))
    
    url = "https://new-credit-endpoint-7c592b18.eastus.inference.ml.azure.com/score"
    api_key = 'R3vDlZduHi8rj0Mcf894cJfQ7mI1HfVh'
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer ' + api_key), 'azureml-model-deployment': 'creditdefaults'}
    r = requests.post(url=url, data=body, headers=headers)
    print(r.status_code)
    print(r.content)
    #result = json.loads(body)
    result = json.loads(r.content)
    return render_template('predict.html', prediction = result)
    





if __name__== "_main_":
    app.run()