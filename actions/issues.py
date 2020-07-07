from bullet_utils import utils


def select_issue(REPO):
    state = utils.option_select(
        prompt="Issue Status:",
        choices=[
            "all",
            "open",
            "closed"
        ]
    )
    utils.cls()
    issues = list()
    [
        issues.append(
            "# " + str(issue.number) + ": " + str(issue.title)
        ) for issue in REPO.get_issues(state=state)
    ]
    issue = utils.option_select(
        prompt="Issue:",
        choices=issues
    )
    utils.cls()
    return REPO.get_issue(int(issue.split(':')[0].replace("#","").strip()))


def load_issue(ISSUE):
    print("# " + str(ISSUE.number) + ": " + ISSUE.title)
    print(ISSUE.body)


def create_issue(REPO):
    return REPO.create_issue(
        title=utils.get_input(prompt="Title: ", strip=True),
        body=utils.get_input(prompt="Body: ", strip=True)
    )
