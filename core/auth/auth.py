import requests
from requests.auth import HTTPBasicAuth

def generate_access_token(user, password, artifactoryurl):
    auth = requests.post(f"https://{artifactoryurl}/artifactory/api/security/token", auth=HTTPBasicAuth(user, password), data={'username': user, 'scope': 'applied-permissions/user', 'expires_in': '0'})
    if (auth.status_code != 200):
        print("Authorization error")
        exit(1)
    return auth.json()['access_token']

