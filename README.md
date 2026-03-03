# jira-terminal-client
A CLI written in Python to query Jira issues faster from a terminal window

## Overview
The `jira-terminal-client` is a command-line interface (CLI) tool designed to interact with Jira issue tracking systems. It simplifies the process of querying and viewing Jira issues directly from your terminal. The tool is built using the `jira` library for Jira server communication and the `click` library for creating a user-friendly command-line interface.

## Architecture
The `jira-terminal-client` consists of several key components:

1. **Imports**:
   - `jira`: Manages the interaction with the Jira server.
   - `click`: Handles the creation of the command-line interface.
   - `os`: Provides access to environment variables for authentication.

2. **Authentication and Jira Instance**:
   - The script retrieves Jira credentials (`JIRA_USER`, `JIRA_TOKEN`, `JIRA_SERVER`) from environment variables.
   - A Jira instance is created using these credentials, enabling the script to communicate with the Jira server.

3. **Function: `issue2str`**:
   - Converts a Jira issue object into a formatted string, including details such as the issue key, web URL, summary, description, assignee, and reporter.

4. **Command: `show`**:
   - A Click command that accepts an issue ID as an argument.
   - Retrieves the issue from the Jira server and prints its details using the `issue2str` function.

5. **Main Execution**:
   - The script checks if it is being run as the main module.
   - If so, it calls the `show` command without arguments, prompting the user to enter an issue ID.

## Usage
To use the `jira-terminal-client`, you need to set the `JIRA_USER`, `JIRA_TOKEN`, and `JIRA_SERVER` environment variables. You can then run the script from the command line and provide an issue ID to see details about that issue.

### Example
```sh
export JIRA_USER="your_username"
export JIRA_TOKEN="your_token"
export JIRA_SERVER="https://your-jira-server.com"
python script.py show ABC-123
```

This command will output the details of the Jira issue with key `ABC-123`.

### Advanced Usage
For more advanced usage, you can explore additional commands and options provided by the `jira-terminal-client`. For example, you can list all issues, filter issues based on specific criteria, or perform other operations directly from the terminal.

## Dependencies
- **jira**: Primary dependency for interacting with the Jira server.
- **click**: Used to create the command-line interface.
- **os**: Used for accessing environment variables for authentication.

By leveraging these components and dependencies, the `jira-terminal-client` provides a powerful and efficient way to interact with Jira issues from your terminal.