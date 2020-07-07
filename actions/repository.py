from bullet_utils import utils

from actions import issues


def select_repo(USER):
    visibility = utils.option_select(
        prompt="Visibility:",
        choices=[
            "all",
            "public",
            "private"
        ]
    )
    utils.cls()
    repos = list()
    repos.append("RETURN (not a repo)")
    for repo in USER.get_repos(affiliation="owner", visibility=visibility):
        repos.append(repo.name)
    repo = utils.option_select(prompt="Select Repo", choices=repos)
    utils.cls()
    if repo == "RETURN (not a repo)":
        return "RETURN"
    return USER.get_repo(repo)


def load_repo(REPO):
    while True:
        print("\nRepository:", REPO.name)
        option = utils.option_select(
            choices=[
                "Info",
                "Issues",
                "Commits",
                "Delete",
                "Return"
            ]
        )
        utils.cls()
        if option == "Info":
            load_repo_info(REPO)
        elif option == "Issues":
            option = utils.option_select(
                prompt="Options:",
                choices=[
                    "Load",
                    "Create"
                ]
            )
            utils.cls()
            if option == "Load":
                issues.load_issue(issues.select_issue(REPO))
            elif option == "Create":
                issues.create_issue()
        elif option == "Commits":
            load_repo_commits(REPO)
        elif option == "Delete":
            if delete_repo(REPO):
                utils.cls()
                return
        elif option == "Return":
            return
        # utils.cls()


def load_repo_info(REPO):
    print(REPO.name)
    print("Clone URL:", REPO.clone_url)
    print("SSH Url", REPO.ssh_url)
    print("Number of Issues:", len(list(REPO.get_issues(state="all"))))
    print("Branches:", list_repo_branches(REPO))



def list_repo_branches(REPO):
    branches = list()
    [branches.append(branch.name) for branch in REPO.get_branches()]
    return ', '.join(branches)



def load_repo_commits(REPO):
    pass


def delete_repo(REPO):
    print("Are you sure you would like to delete this repository (" + REPO.name + ")")
    print("This cannot be undone")
    choice = utils.get_YesNo(prompt="Delete: ")
    if choice == True:
        REPO.delete()
        return True
    elif choice == False:
        return False


def create_repo(USER):
    USER.create_repo(utils.get_input(prompt="Repository Name: "))
