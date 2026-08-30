import polars as pl
from thefuzz import fuzz, process
from src.constants import OFTEN_KEYWORDS

def clean_name(name: str) -> str:
    """
    Cleans the company name by removing whitespace and often appearing keywords.
    
    Args:
        name (str): The company name to clean.
        
    Returns:
        str: The cleaned company name.
    """

    name = name.replace(" ", "")

    for keyword in OFTEN_KEYWORDS:
        if keyword in name:
            name = name.replace(keyword, "")
            

    return name.upper()


def get_similar_names(df: pl.DataFrame) -> pl.DataFrame:
    # all active company names
    active_companies_df = df.filter(pl.col("is_active") == True)
    similar_companies = []

    for company_name in df["name"].to_list():
        for active_company in active_companies_df["name"].to_list():
            # fuzzy matching score between the two names
            matching = fuzz.token_sort_ratio(company_name, active_company)
            if matching >= 85:
                similar_companies.append((company_name, active_company, matching))

    similar_companies_df = pl.DataFrame(data=similar_companies, schema=["company_name", "similar_company", "fuzzy_matching_score"])

    # do not include exact matches (fuzzy_matching_score == 100)
    similar_companies_df = similar_companies_df.remove(pl.col("fuzzy_matching_score") == 100)

    return similar_companies_df
