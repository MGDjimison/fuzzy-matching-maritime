import polars as pl
from thefuzz import fuzz, process
from tqdm import tqdm
import plotly.express as px
from app.constants import OFTEN_KEYWORDS

def clean_name(name: str) -> str:
    """
    Cleans the company name by removing numbers, whitespace, 
    special characters and often appearing keywords.
    
    Args:
        name (str): The company name to clean.
        
    Returns:
        str: The cleaned company name.
    """

    name = ''.join([char for char in name if not char.isdigit() and char.isalpha()])
    
    for keyword in OFTEN_KEYWORDS:
        if keyword in name:
            name = name.replace(keyword, "")
            

    return name.upper()



def get_top2_similar_companies(company: str, df: pl.DataFrame) -> pl.DataFrame:
    if company not in df["name"].to_list():
        raise ValueError(f"Company '{company}' not found in the DataFrame.")
    
    active_companies_df = df.filter(pl.col("is_active") == True)
    data = []

    results = process.extract(company, choices=active_companies_df["name"].to_list(), limit=200, scorer=fuzz.ratio)
    for item in results:
        best_company_match = item[0]

        fuzzy_matching_score = item[1]

        score_with_cleaned_name = fuzz.ratio(
            clean_name(company), clean_name(best_company_match)
        )

        score_3ch = fuzz.ratio(
            clean_name(company[:3]),
            clean_name(best_company_match[:3])
        )
        if score_3ch == 100:
            score_3ch += 20

        score_5ch = fuzz.ratio(
            clean_name(company[:5]),
            clean_name(best_company_match[:5])
        )
        if score_5ch == 100:
            score_5ch += 50

        data.append(
            {
                "name": company,
                "best_match": best_company_match,
                "fuzzy_matching_score": fuzzy_matching_score,
                "score_with_cleaned_name": score_with_cleaned_name,
                "score_3ch": score_3ch,
                "score_5ch": score_5ch
            }
        )

    result_df = pl.DataFrame(data=data)
    # calculate total score and rank the results
    result_df = result_df.with_columns(
        (
            pl.col("fuzzy_matching_score")
            + pl.col("score_with_cleaned_name")
            + pl.col("score_3ch")
            + pl.col("score_5ch")
        ).alias("total"),
        # add a position column based on the total score, to rank the results
    ).with_columns(
        pl.col("total").rank("dense", descending=True).over("name").alias("position")
    )

    result_df = result_df.sort(by="position", descending=False).limit(2)

    return result_df



def compute_top2_similar_companies(df: pl.DataFrame) -> pl.DataFrame:
    list_top2 = []
    
    for company in tqdm(df["name"].to_list()):
        top2_df = get_top2_similar_companies(company, df)
        if isinstance(top2_df, pl.DataFrame):
            list_top2.append(top2_df)
        

    result_df = pl.concat(list_top2)
    return result_df


def show_chart_top2_similar_companies(df: pl.DataFrame) -> None:
    fig = px.bar(
        df, x="best_match", y="total", 
        color="name", title=df['name'].unique()[0],
        labels={"best_match": "Best Company Match", "total": "fuzzy matching Score"}
    )
    fig.show()