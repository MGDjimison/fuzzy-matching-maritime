import polars as pl
from src.utils import clean_name, get_similar_names

if __name__ == "__main__":
    df = pl.read_csv("data/mock_maritime_companies.csv")

    example_name = "Djimi Ocean Transport"
    print(f"Cleaned name: {clean_name(example_name)}")
                
    
