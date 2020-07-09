""" Handles displaying user information. """


from github import GithubException

from src import gen_utils


def get_user_info(user):
    """ Display user information """
    print("Name:", user.name)
    print("Email:", user.email)
    print("Bio:", user.bio)
    print("Company:", user.company)
    print("Organizations:", list_user_organizations(user))
    print("Repositories:", list_user_repos(user))


def list_user_organizations(user):
    """ Returns a list of organizations a user is a member of. """
    organizations = list()
    [organizations.append(org.login) for org in user.get_orgs()]
    return ', '.join(organizations)


def list_user_repos(user):
    """ Return a list of repositories the user (or other) is an owner of. """
    repos = list()
    try:
        [
            repos.append(repo.name)
            for repo in user.get_repos(affiliation="owner")
        ]
    except GithubException:
        [repos.append(repo.name) for repo in user.get_repos(type="owner")]
    return ', '.join(repos)


def select_user(users, git_auth):
    """ Return a user with a specified login from a list of NamedUsers. """
    user = gen_utils.option_select(
        prompt="Select User:",
        choices=users
    )
    return git_auth.get_user(user)
