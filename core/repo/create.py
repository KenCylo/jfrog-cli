import requests

def repo_create(artifactory, access_token, repo_key, json):
    response = requests.put('https://'+artifactory+'/artifactory/api/repositories/'+repo_key, headers={'Authorization': 'Bearer '+access_token, 'Content-type': 'application/json'}, data=json)
    if (response.status_code != 200):
        print("Error creating " + repo_key)
        print(response.content.decode('utf-8'))
        exit(1)
    return response.content

