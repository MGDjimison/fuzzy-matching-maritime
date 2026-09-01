import polars as pl
from src.utils import get_top2_similar_companies

if __name__ == "__main__":
    df = pl.read_csv("data/mock_maritime_companies.csv")

    company = "Osaka-Kiài"
    top2_similar_companies_df = get_top2_similar_companies(company, df)
    print(top2_similar_companies_df)
    
    
