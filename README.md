# Rapid Email Creator

**Rapid Email Creator** is a Python-based tool that automates the creation of temporary email accounts using pluggable temp mail clients.
It generates random email addresses and credentials while implementing exponential backoff for reliability.

To use the tool, you need to install the dependencies and run the script.

```bash
pip install -r requirements.txt
python main.py
```

The class `RapidEmailCreator` is the main class that you need to use. It has the following methods:

- `create_email_account()`: Creates a single email account.
- `create_email_accounts(number_of_accounts: int)`: Creates a specified number of email accounts.

It must be initialized with a temp mail client that implements the `ITempMailClient` interface.
Currently only one client is implemented and uses https://docs.mail.tm/
