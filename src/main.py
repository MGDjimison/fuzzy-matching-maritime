import polars as pl
from src.utils import compute_top2_similar_companies

if __name__ == "__main__":
    df = pl.read_csv("data/mock_maritime_companies.csv")
    # print(df)

    result_df = compute_top2_similar_companies(df)
    print(result_df)
    result_df.write_csv("data/top2_similar_companies.csv")
