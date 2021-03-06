from jira import JIRA
import click
import os

auth = (os.environ["JIRA_USER"], os.environ["JIRA_TOKEN"])
server = os.environ["JIRA_SERVER"]
jira = JIRA(server, basic_auth=auth)

def issue2str(issue):
    text = 'Issue: ' + issue.key
    text = text + '\nWeb: ' + issue.self
    text = text + '\nSummary: ' + issue.fields.summary
    text = text + '\nDescription: ' + issue.fields.description
    text = text + '\nAssignee: ' + issue.fields.assignee.displayName
    text = text + '\nReporter: ' + issue.fields.reporter.displayName
    return text


@click.command("show")
@click.argument("issue_id")
def show(issue_id):
    issue = jira.issue(issue_id)
    print(issue2str(issue))


if __name__ == "__main__":
    show()
