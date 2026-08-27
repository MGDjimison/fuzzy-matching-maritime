import polars as pl

def clean_name(name: str) -> str:
    """
    Cleans the company name by removing numbers, whitespace, and special characters.
    
    Args:
        name (str): The company name to clean.
        
    Returns:
        str: The cleaned company name.
    """

    cleaned_name = ''.join([char for char in name if not char.isdigit() and char.isalpha()])

    return cleaned_name.upper()