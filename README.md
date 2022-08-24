# JFrog CLI

## Installation
`
pip3 install -r requirements.txt
`

## How to use
`
python3 main.py --help
`
- The output
```
usage: main.py [-h] -u USERNAME -p PASSWORD -a ARTIFACTORY {system,user,repo} ...

A CLI tool to interact with Jfrog api

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Jfrog user name
  -p PASSWORD, --password PASSWORD
                        Jfrog user name password
  -a ARTIFACTORY, --artifactory ARTIFACTORY
                        Jfrog artifactory url

main:
  {system,user,repo}
    system              Interact with Jfrog system api
    user                interact with Jfrog user api
    repo                interact with Jfrog repo api
```


## Seek Help
You can just use any command with `--help` or `-h` and it will print the help page


## Resources Used
1. Jfrog artifactory documentation https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API 
2. Python argument parser docs https://docs.python.org/3.6/library/argparse.html#action
3. Python requests module docs https://requests.readthedocs.io/en/latest/
