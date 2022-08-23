import requests

def repo_delete(artifactory, access_token, repo_key):
    response = requests.delete('https://'+artifactory+'/artifactory/api/repositories/'+repo_key, headers={'Authorization': 'Bearer '+access_token})
    if (response.status_code != 200):
        print("Error Deleting "+repo_key)
        print(response.content.decode('utf-8'))
        exit(1)
    return response.content

