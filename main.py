from RapidEmailCreator import RapidEmailCreator
from tempMailClients.MailTmClient import MailTmClient

temp_mail_client = MailTmClient()
email_creator = RapidEmailCreator(temp_mail_client)

print(email_creator.get_current_domain())


print(email_creator.create_email_accounts(10))



