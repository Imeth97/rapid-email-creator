import requests
from tempMailClients.ITempMailClient import ITempMailClient

class MailTmClient(ITempMailClient):
    GET_DOMAINS_URL = "https://api.mail.tm/domains"
    CREATE_EMAIL_ACCOUNT_URL = "https://api.mail.tm/accounts"
    
    def __init__(self):
        domains_response = requests.get(self.GET_DOMAINS_URL)
        domains = domains_response.json()
        if domains_response.status_code == 200:
            self.current_domain = domains["hydra:member"][0]["domain"]
        else:
            raise Exception("Failed to get domains")

    def get_current_domain(self):
        return self.current_domain

    def create_email_account(self, email_address: str, password: str):
        account_creation_response = requests.post(self.CREATE_EMAIL_ACCOUNT_URL, json={"address": email_address, "password": password})
        if account_creation_response.status_code == 201:
            return
        else:
            error_msg = f"Failed to create email account (Status code: {account_creation_response.status_code})"
            try:
                error_data = account_creation_response.json()
                if "hydra:description" in error_data:
                    error_msg += f" - {error_data['hydra:description']}"
                elif "detail" in error_data:
                    error_msg += f" - {error_data['detail']}"
            except:
                error_msg += f" - {account_creation_response.text}"
            raise Exception(error_msg)