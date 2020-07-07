from github import Github

from bullet_utils import utils

from actions import repository
from actions import user
from actions import search


g = Github("username", "password")

USER = g.get_user()

while True:
    option = utils.option_select(
        prompt="What would you like to do",
        choices=[
            "User Info",
            "Load Repo",
            "Create Repo",
            "Search",
            "Exit"
        ]
    )
    utils.cls()
    if option == "User Info":
            user.get_user_info(USER)
    elif option == "Load Repo":
        repo = repository.select_repo(USER)
        if repo != "RETURN":
            repository.load_repo(repo)
    elif option == "Create Repo":
        repository.create_repo(USER)
    elif option == "Search":
        pass
    elif option == "Exit":
        break
