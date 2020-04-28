from jira import JIRA
import curses
import click
import os

auth = (os.environ["JIRA_USER"], os.environ["JIRA_TOKEN"])
server = os.environ["JIRA_SERVER"]
jira = JIRA(server, basic_auth=auth)

results = None


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
    text = text + "\nDescription: " + (issue.fields.description or "None")
    subtasks = "\n".join(list(map(issue2shortstr, issue.fields.subtasks)))
    text = text + "\nSubtasks: \n" + subtasks + "\n"
    return text


def handle(screen, selected=None):
    screen.clear()
    if selected != None:
        text = issue2str(results[selected])
        screen.addstr(text)
    else:
        for idx, issue in enumerate(results):
            screen.addstr("\t{}. {}\n".format(idx, issue2shortstr(issue)))

    screen.refresh()


def start_interactive(screen):
    handle(screen, None)

    instr = ""
    while True:
        c = screen.getch()
        screen.addstr(chr(c))
        if c == curses.KEY_ENTER or c == 10 or c == 13:
            handle(screen, int(instr))
            instr = ""
        elif c == curses.KEY_F4:
            return
        elif c == curses.KEY_F2:
            instr = ""
            handle(screen)
        else:
            instr = instr + chr(c)


@click.group()
def cli():
    return


@cli.command("show")
@click.argument("issue_id")
def show(issue_id):
    issue = jira.issue(issue_id)
    print(issue2str(issue))


@cli.command("assigned")
@click.option("interactive", "-i", is_flag=True, help="Start an interactive session")
@click.option(
    "fq",
    "--filter",
    default=None,
    help="An additional filter query to apply to the jira search",
)
def assigned(interactive, fq):
    jql = "assignee=currentUser() AND status != Done"
    if fq:
        jql = jql + " AND " + fq

    if interactive:
        global results
        results = jira.search_issues(jql)
        curses.wrapper(start_interactive)
    else:
        for issue in jira.search_issues(jql):
            print(issue2shortstr(issue))


if __name__ == "__main__":
    cli()
