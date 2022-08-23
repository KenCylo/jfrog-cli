import requests
import json

def system_storage(artifactory, access_token):
    response = requests.get('https://'+artifactory+'/artifactory/api/storageinfo', headers={'Authorization': 'Bearer '+access_token})
    if (response.status_code != 200):
        print("Error pinging system")
        print(response.content.decode('utf-8'))
        exit(1)
    return bytearray(json.dumps(json.loads(response.content), indent=4), "utf-8")
