from abc import ABC, abstractmethod

class ITempMailClient(ABC):
    """
    Interface for temporary email clients used by RapidEmailCreator.
    
    Any implementation of this interface must provide methods
    to get the current domain and create email accounts.
    """

    @abstractmethod
    def get_current_domain(self) -> str:
        """
        Get the current domain used for creating email addresses
        
        Returns:
            str: The domain string (e.g., 'example.com')
        """
        pass

    @abstractmethod
    def create_email_account(self, email_address: str, password: str) -> None:
        """
        Create an email account with the given address and password
        
        Args:
            email_address: The full email address to create
            password: The password for the account
            
        Raises:
            Exception: If account creation fails
        """
        pass 