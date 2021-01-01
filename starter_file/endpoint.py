import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
             "age": 90,
            "anaemia": 1,
            "creatinine_phosphokinase": 47,
            "diabetes": 0,
            "ejection_fraction": 40,
            "high_blood_pressure": 1,
            "platelets": 204000,
            "serum_creatinine": 2.1,
            "serum_sodium": 132,
            "sex": 1,
            "smoking": 1,
            "time": "8"
          },
          {
            "age": 45,
            "anaemia": 1,
            "creatinine_phosphokinase": 981,
            "diabetes": 0,
            "ejection_fraction": 30,
            "high_blood_pressure": 0,
            "platelets": 136000,
            "serum_creatinine": 1.1,
            "serum_sodium": 137,
            "sex": 1,
            "smoking": 0,
            "time": "11"
          },
      ]
    }

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
