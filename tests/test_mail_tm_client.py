import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json

# Import from the package
from rapid_email_creator.tempMailClients import MailTmClient

class TestMailTmClient(unittest.TestCase):
    
    @patch('requests.get')
    def test_init_success(self, mock_get):
        """Test successful initialization with valid domain response"""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "hydra:member": [
                {"domain": "test-domain.com"}
            ]
        }
        mock_get.return_value = mock_response
        
        # Create client
        client = MailTmClient()
        
        # Assertions
        mock_get.assert_called_once_with(MailTmClient.GET_DOMAINS_URL)
        self.assertEqual(client.get_current_domain(), "test-domain.com")
    
    @patch('requests.get')
    def test_init_failure(self, mock_get):
        """Test initialization failure with error response"""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        # Create client should raise exception
        with self.assertRaises(Exception) as context:
            client = MailTmClient()
        
        self.assertTrue("Failed to get domains" in str(context.exception))
    
    @patch('requests.get')
    @patch('requests.post')
    def test_create_email_account_success(self, mock_post, mock_get):
        """Test successful email account creation"""
        # Setup mock responses
        mock_get_response = MagicMock()
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = {
            "hydra:member": [
                {"domain": "test-domain.com"}
            ]
        }
        mock_get.return_value = mock_get_response
        
        mock_post_response = MagicMock()
        mock_post_response.status_code = 201
        mock_post.return_value = mock_post_response
        
        # Create client and test account creation
        client = MailTmClient()
        client.create_email_account("test@test-domain.com", "password123")
        
        # Assertions
        mock_post.assert_called_once_with(
            MailTmClient.CREATE_EMAIL_ACCOUNT_URL, 
            json={"address": "test@test-domain.com", "password": "password123"}
        )
    
    @patch('requests.get')
    @patch('requests.post')
    def test_create_email_account_failure_with_error_message(self, mock_post, mock_get):
        """Test email account creation failure with error message"""
        # Setup mock responses
        mock_get_response = MagicMock()
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = {
            "hydra:member": [
                {"domain": "test-domain.com"}
            ]
        }
        mock_get.return_value = mock_get_response
        
        mock_post_response = MagicMock()
        mock_post_response.status_code = 400
        mock_post_response.json.return_value = {
            "hydra:description": "Email address already in use"
        }
        mock_post.return_value = mock_post_response
        
        # Create client and try to create account
        client = MailTmClient()
        
        # Should raise exception with error message
        with self.assertRaises(Exception) as context:
            client.create_email_account("test@test-domain.com", "password123")
        
        self.assertTrue("Email address already in use" in str(context.exception))

if __name__ == "__main__":
    unittest.main() 