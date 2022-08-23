from argparse import ArgumentParser, FileType
from core.auth.auth import generate_access_token
from core.repo.create import repo_create
from core.repo.delete import repo_delete
from core.repo.update import repo_update
from core.repo.list import repo_list
from core.system.ping import system_ping
from core.system.version import system_version
from core.system.storage import system_storage
from core.user.create import user_create
from core.user.list import user_list
from core.user.delete import user_delete



def main(parent_parser, system_parser, user_parser, repo_parser):
    args = parent_parser.parse_args()
    access_token = generate_access_token(args.username, args.password, args.artifactory)


    if ("system" in args):
        if ("system_ping" in args):
            result = system_ping(args.artifactory, access_token)
            print(result.decode('utf-8'))
        elif ("system_version" in args):
            result = system_version(args.artifactory, access_token)
            print(result.decode('utf-8'))
        elif ("system_storage" in args):
            result = system_storage(args.artifactory, access_token)
            print(result.decode('utf-8'))
        else:
            system_parser.print_help()
    elif ("user" in args):
        if ("create_user" in args):
            result = user_create(args.artifactory, access_token, args.name, args.json.read())
            print(result.decode('utf-8'))
        elif ("user_list" in args):
            result = user_list(args.artifactory, access_token)
            print(result.decode('utf-8'))
        elif ("delete_user" in args):
            result = user_delete(args.artifactory, access_token, args.name)
            print(result.decode('utf-8'))
        else:
            user_parser.print_help()
    elif ("repo" in args):
        if ("create_repo" in args):
            result = repo_create(args.artifactory, access_token, args.repo_key, args.json.read())
            print(result.decode('utf-8'))
        elif ("update_repo" in args):
            result = repo_update(args.artifactory, access_token, args.repo_key, args.json.read())
            print(result.decode('utf-8'))
        elif ("repo_list" in args):
            result = repo_list(args.artifactory, access_token)
            print(result.decode('utf-8'))
        elif ("delete_repo" in args):
            result = repo_delete(args.artifactory, access_token, args.repo_key)
            print(result.decode('utf-8'))
        else:
            repo_parser.print_help()




if __name__ == '__main__':
    parent_parser = ArgumentParser(description='A CLI tool to interact with Jfrog api')
    parent_parser.add_argument('-u', '--username', type=str, help="Jfrog user name", required=True)
    parent_parser.add_argument('-p', '--password', type=str, help="Jfrog user name password", required=True)
    parent_parser.add_argument('-a', '--artifactory', type=str, help="Jfrog artifactory url", required=True)

    main_parser = parent_parser.add_subparsers(title='main')

    ##########

    system_parser = main_parser.add_parser('system', help='Interact with Jfrog system api')
    system_parser.add_argument('system', action='store_true')
    system_subparsers = system_parser.add_subparsers()
    system_ping_parser = system_subparsers.add_parser('ping')
    system_ping_parser.add_argument('system_ping', action="store_true")
    system_version_parser = system_subparsers.add_parser('version')
    system_version_parser.add_argument('system_version', action="store_true")
    system_storage_parser = system_subparsers.add_parser('storage')
    system_storage_parser.add_argument('system_storage', action="store_true")


    ##########

    user_parser = main_parser.add_parser('user', help='interact with Jfrog user api')
    user_parser.add_argument('user', action='store_true')
    user_subparsers = user_parser.add_subparsers()

    user_create_parser = user_subparsers.add_parser('create')
    user_create_parser.add_argument('-n', '--name', help="name", required=True)
    user_create_parser.add_argument('-j', '--json', type=FileType('r'), help="User json file location", required=True)
    user_create_parser.add_argument('create_user', action='store_true')

    user_list_parser = user_subparsers.add_parser('list')
    user_list_parser.add_argument('user_list', action='store_true')

    user_delete_parser = user_subparsers.add_parser('delete')
    user_delete_parser.add_argument('-n', '--name', help="name", required=True)
    user_delete_parser.add_argument('delete_user', action='store_true')


    ##########

    repo_parser = main_parser.add_parser('repo', help='interact with Jfrog repo api')
    repo_parser.add_argument('repo', action='store_true')
    repo_subparsers = repo_parser.add_subparsers()

    repo_create_parser = repo_subparsers.add_parser('create')
    repo_create_parser.add_argument('create_repo', action='store_true')
    repo_create_parser.add_argument('-k', '--repo-key', help="Repo key", required=True)
    repo_create_parser.add_argument('-j', '--json', type=FileType('r'), help="Repo json file location", required=True)

    repo_update_parser = repo_subparsers.add_parser('update')
    repo_update_parser.add_argument('update_repo', action='store_true')
    repo_update_parser.add_argument('-k', '--repo-key', help="Repo key", required=True)
    repo_update_parser.add_argument('-j', '--json', type=FileType('r'), help="Repo json file location", required=True)

    repo_list_parser = repo_subparsers.add_parser('list')
    repo_list_parser.add_argument('repo_list', action='store_true')

    repo_delete_parser = repo_subparsers.add_parser('delete')
    repo_delete_parser.add_argument('-k', '--repo-key', help="Repo name", required=True)
    repo_delete_parser.add_argument('delete_repo', action='store_true')

    ##########
    main(parent_parser, system_parser, user_parser, repo_parser)
