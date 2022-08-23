import requests

def system_ping(artifactory, access_token):
    response = requests.get('https://'+artifactory+'/artifactory/api/system/ping', headers={'Authorization': 'Bearer '+access_token})
    if (response.status_code != 200):
        print("Error pinging system")
        print(response.content.decode('utf-8'))
        exit(1)
    return response.content
