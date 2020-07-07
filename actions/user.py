
def get_user_info(USER):
    print("Name:", USER.name)
    print("Email:", USER.email)
    print("Bio:", USER.bio)
    print("Company:", USER.company)
    print("Organizations:", list_user_organizations(USER))
    print("Repositories:", list_user_repos(USER))


def list_user_organizations(USER):
    organizations = list()
    [organizations.append(org.login) for org in USER.get_orgs()]
    return ', '.join(organizations)


def list_user_repos(USER):
    repos = list()
    [repos.append(repo.name) for repo in USER.get_repos(affiliation="owner")]
    return ', '.join(repos)
