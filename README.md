# Rapid Email Creator

**Rapid Email Creator** is a Python-based tool that automates the creation of temporary email accounts using pluggable temp mail clients.
It generates random email addresses and credentials while implementing exponential backoff for reliability.

## Installation

You can install the package via pip:

```bash
pip install rapid-email-creator
```

## Usage

Basic usage example:

```python
from rapid_email_creator import RapidEmailCreator
from rapid_email_creator.tempMailClients import MailTmClient

# Create a temp mail client
temp_mail_client = MailTmClient()

# Initialize the email creator
email_creator = RapidEmailCreator(temp_mail_client)

# Get the current domain being used
domain = email_creator.get_current_domain()
print(f"Using domain: {domain}")

# Create a single email account
account = email_creator.create_email_account()
if account:
    email, password = account
    print(f"Created account: {email} with password: {password}")

# Create multiple email accounts
accounts = email_creator.create_email_accounts(5)
print(f"Created {len(accounts)} accounts:")
for email, password in accounts:
    print(f"- {email} : {password}")
```

## Creating Custom Temp Mail Clients

You can create custom temp mail clients by implementing the `ITempMailClient` interface:

```python
from rapid_email_creator.tempMailClients import ITempMailClient

class MyCustomMailClient(ITempMailClient):
    def get_current_domain(self) -> str:
        # Return the domain to use for email addresses
        return "example.com"

    def create_email_account(self, email_address: str, password: str) -> None:
        # Implement account creation logic
        # Raise an exception if creation fails
        pass
```

## Features

- **Pluggable Architecture**: Use different temp mail services by implementing the `ITempMailClient` interface
- **Reliability**: Built-in exponential backoff for handling API rate limits and errors
- **Simple API**: Easy-to-use methods for creating single or multiple accounts

## Available Temp Mail Clients

Currently, the following clients are implemented:

- **MailTmClient**: Uses the [mail.tm](https://docs.mail.tm/) service

## License

MIT
