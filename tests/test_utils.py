from app.utils import clean_name

def test_clean_name():
    # Test case 1: Basic cleaning
    assert clean_name("Company123") == "COMPANY"
    
    # Test case 2: Removing special characters
    assert clean_name("Company!@#") == "COMPANY"
    
    # Test case 3: Removing whitespace
    assert clean_name("   Company   ") == "COMPANY"
    
    # Test case 4: Removing often appearing keywords
    assert clean_name("The Marine Company") == "THECOMPANY"
    
    # Test case 5: Mixed case and numbers
    assert clean_name("CoMpAnY456") == "COMPANY"
    
    # Test case 6: Only special characters and numbers
    assert clean_name("123!@#") == ""

