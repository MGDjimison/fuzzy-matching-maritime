import polars as pl
from app.constants  import MARITIME_COMPANIES_FILEPATH
from app.utils import clean_name, get_top2_similar_companies

if __name__ == "__main__":
    df = pl.read_csv(MARITIME_COMPANIES_FILEPATH)
    # print(df.head(5))

    company = "Kawsaki Zosén (2)"
    print(f"Top 2 similar companies for {company}:")
    top2_df = get_top2_similar_companies(company, df)
    print(top2_df)
    # show_chart_top2_similar_companies(top2_df)