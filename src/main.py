import polars as pl
from src.utils import clean_name, get_similar_names

if __name__ == "__main__":
    df = pl.read_csv("data/mock_maritime_companies.csv")
    matches_df = get_similar_names(df)
    print(matches_df.head(10))
                
    
