"""
Example usage of the Rapid Email Creator package
"""

from rapid_email_creator import RapidEmailCreator
from rapid_email_creator.tempMailClients import MailTmClient

def main():
    # Create a temp mail client
    try:
        temp_mail_client = MailTmClient()
        
        # Initialize the email creator
        email_creator = RapidEmailCreator(temp_mail_client)
        
        # Get the current domain being used
        domain = email_creator.get_current_domain()
        print(f"Using domain: {domain}")
        
        # Create a single email account
        print("\nCreating a single account...")
        account = email_creator.create_email_account()
        if account:
            email, password = account
            print(f"Created account: {email} with password: {password}")
        else:
            print("Failed to create account")
        
        # Create multiple email accounts
        num_accounts = 3
        print(f"\nCreating {num_accounts} accounts...")
        accounts = email_creator.create_email_accounts(num_accounts)
        print(f"Created {len(accounts)} accounts:")
        for email, password in accounts:
            print(f"- {email} : {password}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 