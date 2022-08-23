import requests

def user_delete(artifactory, access_token, user_name):
    response = requests.delete('http://'+artifactory+'/artifactory/api/security/users/'+user_name, headers={'Authorization': 'Bearer '+access_token})
    if (response.status_code != 200):
        print("Error Deleting "+user_name)
        print(response.content.decode('utf-8'))
        exit(1)
    return response.content

