import requests

def repo_update(artifactory, access_token, repo_key, json):
    response = requests.post('https://'+artifactory+'/artifactory/api/repositories/'+repo_key, headers={'Authorization': 'Bearer '+access_token, 'Content-Type': 'application/json'}, data=json)
    if (response.status_code != 200):
        print("Error updating " + repo_key)
        print(response.content.decode('utf-8'))
        exit(1)
    return response.content

