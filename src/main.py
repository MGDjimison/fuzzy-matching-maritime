import polars as pl
from src.utils import get_top2_similar_companies, clean_name

if __name__ == "__main__":
    df = pl.read_csv("data/mock_maritime_companies.csv")
    # print(df)

    company = "Osaka-Kiài"
    top2_df = get_top2_similar_companies(company, df)
    print(top2_df)
