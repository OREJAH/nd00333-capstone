import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
             "age": 40,
            "anaemia": 0,
            "creatinine_phosphokinase": 478,
            "diabetes": 1,
            "ejection_fraction": 30,
            "high_blood_pressure": 0,
            "platelets": 303000,
            "serum_creatinine": 0.9,
            "serum_sodium": 136,
            "sex": 1,
            "smoking": 0,
            "time": "148"
          },
          {
            "age": 86,
            "anaemia": 0,
            "creatinine_phosphokinase": 582,
            "diabetes": 0,
            "ejection_fraction": 38,
            "high_blood_pressure": 0,
            "platelets": 263358,
            "serum_creatinine": 1.83,
            "serum_sodium": 134,
            "sex": 0,
            "smoking": 0,
            "time": "95"
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
