import requests

def system_version(artifactory, access_token):
    response = requests.get('https://'+artifactory+'/artifactory/api/system', headers={'Authorization': 'Bearer '+access_token})
    if (response.status_code != 200):
        print("Error getting system info")
        print(response.content.decode('utf-8'))
        exit(1)
    return response.content
