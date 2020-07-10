""" Handles interactions with repositories. """

import os

from github import GithubException

import issue_utils
import gen_utils


def load_user_repos(user):
    """ Return a list of repositories that the user owns. """
    visibility = gen_utils.option_select(
        prompt="Visibility:",
        choices=[
            "all",
            "public",
            "private"
        ]
    )
    gen_utils.cls()
    repos = list()
    repos.append("RETURN")
    for repo in user.get_repos(affiliation="owner", visibility=visibility):
        repos.append(repo.name)
    return repos


def select_repo(repos, user):
    """ Return a user selected repository. """
    repo = gen_utils.option_select(prompt="Select Repo", choices=repos)
    gen_utils.cls()
    if repo == "RETURN":
        return "RETURN"
    return user.get_repo(repo)


def load_repo(repo):
    """
        Load a selected repository and allow for different
        repository specific actions.
    """
    while True:
        print("\nRepository:", repo.name)
        option = gen_utils.option_select(
            choices=[
                "Info",
                "Clone",
                "Files",
                "Issues",
                "Commits",
                "Delete",
                "Return"
            ]
        )
        gen_utils.cls()
        if option == "Info":
            load_repo_info(repo)
        elif option == "Issues":
            load_repo_issues(repo)
        elif option == "Clone":
            load_repo_clone(repo)
        elif option == "Files":
            print(list_repo_files(repo))
        elif option == "Commits":
            print(list_repo_commits(repo))
        elif option == "Delete":
            if delete_repo(repo):
                gen_utils.cls()
                return True
        elif option == "Return":
            return "RETURN"


def load_repo_info(repo):
    """ Display repository information. """
    print(repo.name)
    print("Clone URL:", repo.clone_url)
    print("SSH Url", repo.ssh_url)
    print("Number of Issues:", len(list(repo.get_issues(state="all"))))
    print("Branches:", list_repo_branches(repo))


def load_repo_issues(repo):
    """ Handle repo issues. """
    option = gen_utils.option_select(
        prompt="Options:",
        choices=[
            "RETURN",
            "Load",
            "Create"
        ]
    )
    gen_utils.cls()
    if option == "Load":
        issue = issue_utils.select_issue(repo)
        if issue == "None":
            print("No Issues")
        if issue not in ("RETURN", "None"):
            issue_utils.load_issue(issue)
    elif option == "Create":
        issue_utils.create_issue(repo)
    return "RETURN"


def load_repo_clone(repo):
    """ Handle cloning repo """
    path = gen_utils.get_input(
        prompt="Location for repository:"
    )
    method = gen_utils.option_select(
        prompt="Clone method:",
        choices=[
            "SSH",
            "HTTPS"
        ]
    )
    if method == "SSH":
        url = repo.ssh_url
    else:
        url = repo.clone_url
    clone_repo(url, path=path)


def list_repo_branches(repo):
    """ Return a list of branches in the repository. """
    branches = list()
    try:
        [branches.append(branch.name) for branch in repo.get_branches()]
        return ', '.join(branches)
    except GithubException:
        return "None"


def list_repo_commits(repo):
    """ Return a list of commits to the repository. """
    commits = list()
    try:
        [
            commits.append(commit.commit.message)
            for commit in repo.get_commits()
        ]
        return '\n'.join(commits)
    except GithubException:
        return "None"


def list_repo_files(repo):
    """
        Return a list of files within the repository
        (only in root of repo currently).
    """
    try:
        contents = repo.get_contents("/")
        if len(contents) != 0:
            processed = list()
            for content in contents:
                if content.type == "file":
                    processed.append(content.name)
                elif content.type == "dir":
                    processed.append(content.name + "/")
            return '\n'.join(processed)
    except GithubException:
        pass
    return "None"


def delete_repo(repo):
    """ Delete the current repository (have to be the owner of the repo). """
    print(
        "Are you sure you would like to delete this repository (" +
        repo.name + ")"
    )
    print("This cannot be undone")
    choice = gen_utils.get_yes_no(prompt="Delete: ")
    if choice:
        try:
            repo.delete()
            return True
        except GithubException:
            return False
    return False


def create_repo(user):
    """ Create a new repository with a specified name. """
    user.create_repo(gen_utils.get_input(prompt="Repository Name: "))


def clone_repo(url, path="."):
    """ Clone the selected repository to the specified location. """
    if not os.path.exists(os.getenv('HOME') + "/" + path):
        os.mkdir(os.getenv('HOME') + "/" + path)
    command = "git clone " + url + " " + os.getenv('HOME') + "/" + path
    os.system(command)
