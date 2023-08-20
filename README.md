# indicator_service

### Example ml-fastapi application  for https://www.healthuniverse.com/ hackathon.

Diabet Estimator <br/>
source of dataset :https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

#if you want to run only jupyter notebook you can reach from this link : https://www.kaggle.com/code/sirmax/diabet-indicator/notebook

### how to run software
type in the command line :python3 main.py


### how to run test
open the tests folder and  type in the command line :pytest


### how to use software or service

#### 1.Browser

If you run software open the browser and click this link:http://0.0.0.0:8000

![docs](/img/gui.png )

#### 2.Use with Swagger  Docs

If you run software open the browser and click this link:http://0.0.0.0:8000/docs

![docs](/img/docs.png )

#### 3.Use with Postman
![postman](/img/postman.png )




#### 4. Use with Python Script
<code>

import requests
import json

url = "http://0.0.0.0:8000/predict"

payload = json.dumps({
  "features": [
    1,
    2,
    21,
    1,
    3
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

</code>