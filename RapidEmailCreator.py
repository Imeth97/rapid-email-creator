import requests
from tempMailClients.ITempMailClient import ITempMailClient
import random
import string
import time

class RapidEmailCreator:
    def __init__(self, temp_mail_client: ITempMailClient):
        self.temp_mail_client = temp_mail_client
    def get_current_domain(self):
        return self.temp_mail_client.get_current_domain()
    
    def create_email_account(self):
        # generate random username and password
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        try:
            address = username + "@" + self.temp_mail_client.get_current_domain()
            self.temp_mail_client.create_email_account(address, password)
            return (address, password)
        except Exception as e:
            print(e)
            return None
        
    def create_email_accounts(self, number_of_accounts: int):
        accounts = []
        base_delay = 1  # Initial delay in seconds
        max_delay = 60  # Maximum delay in seconds
        
        while len(accounts) < number_of_accounts:
            account = self.create_email_account()
            if account is not None:
                accounts.append(account)
                base_delay = 1  # Reset delay after successful attempt
            else:
                # Implement exponential backoff
                delay = min(base_delay * 2, max_delay)
                time.sleep(delay)
                base_delay = delay
                continue
            
            # Add small delay between successful requests
            if len(accounts) < number_of_accounts:
                time.sleep(1)
                
        return accounts
        