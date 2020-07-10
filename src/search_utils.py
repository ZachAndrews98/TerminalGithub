""" Handles Github searches. """


import repo_utils
import gen_utils
import user_utils


def search_repo(git_auth):
    """ Search github for repositories and then load a selected repo. """
    search = gen_utils.get_input(prompt="Search: ")
    results = git_auth.search_repositories(search).get_page(0)
    repos = list()
    [repos.append(result.full_name) for result in results]
    repo = repo_utils.select_repo(repos, git_auth)
    repo_utils.load_repo(repo)


def search_user(git_auth):
    """ Search github for users and then load a selected user. """
    search = gen_utils.get_input(prompt="Search: ")
    results = git_auth.search_users(search).get_page(0)
    users = list()
    [users.append(result.login) for result in results]
    if len(users) > 1:
        user = user_utils.select_user(users, git_auth)
        user_utils.get_user_info(user)
    else:
        user_utils.get_user_info(results[0])
