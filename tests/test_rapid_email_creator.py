import unittest
from unittest.mock import MagicMock
import sys
import os
import random
import string

# Import from the package
from rapid_email_creator.tempMailClients import ITempMailClient
from rapid_email_creator import RapidEmailCreator

class MockTempMailClient(ITempMailClient):
    """Mock implementation of ITempMailClient for testing"""
    def __init__(self, domain="example.com", create_success=True, failure_count=0):
        self.domain = domain
        self.create_success = create_success
        self.calls = 0
        self.failure_count = failure_count
    
    def get_current_domain(self) -> str:
        return self.domain
    
    def create_email_account(self, email_address: str, password: str):
        self.calls += 1
        # Simulate failures for the first n calls if failure_count is set
        if self.failure_count >= self.calls:
            raise Exception("Simulated failure")
        
        if not self.create_success:
            raise Exception("Failed to create email account")
        return

class TestRapidEmailCreator(unittest.TestCase):
    
    def test_get_current_domain(self):
        """Test that get_current_domain returns the correct domain from the client"""
        mock_client = MockTempMailClient(domain="test.com")
        creator = RapidEmailCreator(mock_client)
        self.assertEqual(creator.get_current_domain(), "test.com")
    
    def test_create_email_account_success(self):
        """Test successful email account creation"""
        mock_client = MockTempMailClient()
        creator = RapidEmailCreator(mock_client)
        
        account = creator.create_email_account()
        self.assertIsNotNone(account)
        
        email, password = account
        self.assertTrue(email.endswith("@example.com"))
        self.assertEqual(len(password), 10)  # Default password length is 10
    
    def test_create_email_account_failure(self):
        """Test failed email account creation"""
        mock_client = MockTempMailClient(create_success=False)
        creator = RapidEmailCreator(mock_client)
        
        account = creator.create_email_account()
        self.assertIsNone(account)
    
    def test_create_multiple_accounts_success(self):
        """Test creating multiple accounts successfully"""
        mock_client = MockTempMailClient()
        creator = RapidEmailCreator(mock_client)
        
        num_accounts = 5
        accounts = creator.create_email_accounts(num_accounts)
        
        self.assertEqual(len(accounts), num_accounts)
        for email, password in accounts:
            self.assertTrue(email.endswith("@example.com"))
            self.assertEqual(len(password), 10)
    
    def test_create_multiple_accounts_with_failures(self):
        """Test creating multiple accounts with some initial failures"""
        # Mock client that fails the first 2 attempts
        mock_client = MockTempMailClient(failure_count=2)
        creator = RapidEmailCreator(mock_client)
        
        num_accounts = 3
        accounts = creator.create_email_accounts(num_accounts)
        
        # Should still get the requested number of accounts
        self.assertEqual(len(accounts), num_accounts)
        
        # But should have made more attempts
        self.assertGreater(mock_client.calls, num_accounts)

if __name__ == "__main__":
    unittest.main() 