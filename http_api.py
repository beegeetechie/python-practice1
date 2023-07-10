import requests
response = requests.get("http://api.open-notify.org/astros.json")
json_results = response.json()
print(json_results)
print("Below are the persons list in the space:")
for names in json_results.get('people'):
  print(names['name'])
   #print(names.get('name'))