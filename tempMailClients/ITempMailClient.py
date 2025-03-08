from abc import ABC, abstractmethod

class ITempMailClient(ABC):
    """Interface for temp email clients"""

    @abstractmethod
    def get_current_domain(self) -> str:
        """Must be implemented to get the current domain"""
        pass

    @abstractmethod
    def create_email_account(self) -> str:
        """Must be implemented to create an email account"""
        pass
        