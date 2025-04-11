# Bachelor
Our bachelor product, an embedding of Ai in Github for automating documentation.

# How to use the test environment
Works right now only on python v.12

use this command to change you version in the current terminal(it will use your original version when you close the terminal)
for mac

```shell
alias python3 "/opt/homebrew/bin/python3.12"
```
## Github access token
You will need to add a personal access token (PAT) from Github to the .env file

### Get a PAT by going to you Github profile:
path to token:
settings -> developer settings -> Token(classic)
Press "Generate token"
Give these permissions:
    - admin:org
    - gist
    - repo
    - workflow
Go back to .env and add a variable called GITHUB_PAT = your_PAT
(Sometime you have to close down VS code for the .env to register the change)

## to-do
- [] add metadata to test results
- [] create workflow, which pushes change done to the result folder to main.