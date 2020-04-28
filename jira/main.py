from jira import JIRA
import click
import os

auth = (os.environ["JIRA_USER"], os.environ["JIRA_TOKEN"])
server = os.environ["JIRA_SERVER"]
jira = JIRA(server, basic_auth=auth)


def issue2shortstr(issue):
    return "({}) {}: {}".format(
        issue.fields.status.name, issue.key, issue.fields.summary
    )


def issue2str(issue):
    text = "Issue: " + issue.key
    text = text + "\nWeb: " + issue.self
    text = text + "\nSummary: " + issue.fields.summary
    text = text + "\nStatus: " + issue.fields.status.name
    text = text + "\nAssignee: " + issue.fields.assignee.displayName
    text = text + "\nReporter: " + issue.fields.reporter.displayName
    text = text + "\nDescription: " + issue.fields.description
    subtasks = "\n".join(list(map(issue2shortstr, issue.fields.subtasks)))
    text = text + "\nSubtasks: \n" + subtasks + "\n"
    return text


@click.group()
def cli():
    return


@cli.command("show")
@click.argument("issue_id")
def show(issue_id):
    issue = jira.issue(issue_id)
    print(issue2str(issue))


@cli.command("assigned")
@click.option(
    "fq",
    "--filter",
    default=None,
    help="An additional filter query to apply to the jira search",
)
def assigned(fq):
    jql = "assignee=currentUser() AND status != Done"
    if fq:
        jql = jql + " AND " + fq

    for issue in jira.search_issues(jql):
        print(issue2shortstr(issue))


if __name__ == "__main__":
    cli()
