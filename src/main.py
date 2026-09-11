import polars as pl
from src.utils import get_top2_similar_companies, clean_name, show_chart_top2_similar_companies

if __name__ == "__main__":
    df = pl.read_csv("data/mock_maritime_companies.csv")
    # print(df)

    company = "Kawasaki Zosén (2)"
    # print(f"Top 2 similar companies for {company}:")
    top2_df = get_top2_similar_companies(company, df)
    # print(top2_df)
    show_chart_top2_similar_companies(top2_df)