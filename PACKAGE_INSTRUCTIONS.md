# Packaging and Publishing Instructions

This guide explains how to install the `rapid-email-creator` package locally and how to publish it to PyPI.

## Installation from Local Build

After building the package, you can install it locally without uploading to PyPI using:

```bash
pip install dist/rapid_email_creator-0.1.0-py3-none-any.whl
```

## Testing the Package

Once installed, you can test that it works correctly:

```python
from rapid_email_creator import RapidEmailCreator
from rapid_email_creator.tempMailClients import MailTmClient

# Create a temp mail client
mail_client = MailTmClient()
creator = RapidEmailCreator(mail_client)

# Print the domain
print(f"Current domain: {creator.get_current_domain()}")
```

## Publishing to PyPI

To publish the package to PyPI, you need to:

1. Create an account on PyPI if you don't have one already: https://pypi.org/account/register/

2. Create an API token for uploading packages:

   - Go to https://pypi.org/manage/account/
   - Click "Add API token"
   - Set token scope (project-specific is recommended)
   - Copy the token (you'll only see it once)

3. Configure your credentials:

   Create or edit the file `~/.pypirc`:

   ```
   [pypi]
   username = __token__
   password = your-token-here
   ```

4. Upload your package to PyPI:

   ```bash
   twine upload dist/*
   ```

   If you don't want to store credentials in the config file, you can also use:

   ```bash
   twine upload dist/* -u __token__ -p your-token-here
   ```

5. After uploading, your package can be installed via pip:

   ```bash
   pip install rapid-email-creator
   ```

## Updating the Package

When you want to release a new version:

1. Update the version number in:

   - `rapid_email_creator/__init__.py`
   - `setup.py`

2. Rebuild the package:

   ```bash
   python -m build
   ```

3. Upload the new version:
   ```bash
   twine upload dist/*
   ```

## Creating a Test PyPI Release

If you want to test the publishing process without affecting the main PyPI repository:

1. Register on Test PyPI: https://test.pypi.org/account/register/

2. Upload to Test PyPI:

   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```

3. Install from Test PyPI:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ rapid-email-creator
   ```
