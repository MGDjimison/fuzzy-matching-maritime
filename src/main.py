import polars as pl

if __name__ == "__main__":
    df = pl.read_csv("data/mock_maritime_companies.csv")
    print(df.head(5))
