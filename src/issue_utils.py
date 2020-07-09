""" Handles interactions with issues in repositories. """


from src import gen_utils


def select_issue(repo):
    """ Select an issue within a repository. """
    state = gen_utils.option_select(
        prompt="Issue Status:",
        choices=[
            "all",
            "open",
            "closed"
        ]
    )
    gen_utils.cls()
    issues = list()
    issues.append("RETURN")
    [
        issues.append(
            "# " + str(issue.number) + ": " + str(issue.title)
        ) for issue in repo.get_issues(state=state)
    ]
    if len(issues) != 1:
        issue = gen_utils.option_select(
            prompt="Issue:",
            choices=issues
        )
        gen_utils.cls()
        if issue != "RETURN":
            return repo.get_issue(
                int(issue.split(':')[0].replace("#", "").strip())
            )
        return "RETURN"
    return "None"


def load_issue(issue):
    """ Display the issue number, title, and body of an issue. """
    print("# " + str(issue.number) + ": " + issue.title)
    print(issue.body)


def create_issue(repo):
    """ Create a new issue for a repository. """
    return repo.create_issue(
        title=gen_utils.get_input(prompt="Title: ", strip=True),
        body=gen_utils.get_input(prompt="Body: ", strip=True)
    )
