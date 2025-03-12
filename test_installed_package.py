"""
Test that the installed package works correctly
"""

from rapid_email_creator import RapidEmailCreator
from rapid_email_creator.tempMailClients import ITempMailClient, MailTmClient

def test_import():
    """Test that classes are importable"""
    print("Testing imports... ", end="")
    assert hasattr(RapidEmailCreator, 'create_email_account')
    assert issubclass(MailTmClient, ITempMailClient)
    print("OK")

def main():
    print("Testing the installed rapid-email-creator package")
    
    # Test imports
    test_import()
    
    print("\nPackage verification successful!")
    print("To test with a real API (not recommended for automated tests),")
    print("run the example.py script.")

if __name__ == "__main__":
    main() 