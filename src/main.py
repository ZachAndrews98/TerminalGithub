""" Main program driving file. """

from github import Github

import gen_utils
import repo_utils
import user_utils
import search_utils

def main():
    """ Main function of program. """
    f = open("./KEY", "r")
    git_auth = Github(f.read().strip())

    user = git_auth.get_user()

    while True:
        option = gen_utils.option_select(
            prompt="What would you like to do",
            choices=[
                "User Info",
                "Load Repo",
                "Create Repo",
                "Search",
                "Exit"
            ]
        )
        gen_utils.cls()
        if option == "User Info":
                user_utils.get_user_info(user)
        elif option == "Load Repo":
            repos = repo_utils.load_user_repos(user)
            repo = repo_utils.select_repo(repos, user)
            if repo != "RETURN":
                repo_utils.load_repo(repo)
        elif option == "Create Repo":
            repo_utils.create_repo(user)
        elif option == "Search":
            type = gen_utils.option_select(
                prompt="Search Type:",
                choices=[
                    "RETURN",
                    "Repository",
                    "User",
                    "Topic"
                ]
            )
            if type == "Repository":
                search_utils.search_repo(git_auth)
            elif type == "User":
                search_utils.search_user(git_auth)
            elif type == "RETURN":
                continue
        elif option == "Exit":
            break


if __name__ == "__main__":
    main()
