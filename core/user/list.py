import requests

def user_list(artifactory, access_token):

    response = requests.get('https://'+artifactory+'/artifactory/api/security/users', headers={'Authorization': 'Bearer '+access_token})
    if (response.status_code != 200):
        print("Error Getting users")
        print(response.content.decode('utf-8'))
        exit(1)
    return response.content
