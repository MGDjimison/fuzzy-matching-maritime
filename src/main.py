import polars as pl
from src.utils import clean_name

if __name__ == "__main__":
    # df = pl.read_csv("data/mock_maritime_companies.csv")
    # print(df.head(5))
    print(clean_name("Company 123!@# Name"))  # Example usage of the clean_name function
