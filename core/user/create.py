import requests

def user_create(artifactory, access_token, user_name, json):
    response = requests.put("https://"+artifactory+"/artifactory/api/security/users/"+user_name, headers={'Authorization': 'Bearer '+access_token, 'Content-type': 'application/json'}, data=json)
    if (response.status_code != 200 and response.status_code != 201):
        print("Error creating user " + user_name)
        print(response.content.decode('utf-8'))
        exit(1)
    if (len(response.content.strip()) < 2):
        return bytearray(f"Success {user_name} created Success", "utf-8")
    return response.content

