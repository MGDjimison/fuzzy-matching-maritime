# fuzzy-matching-maritime

## Context

International companies were duplicated in the database (example: Thales, Tales, Talece), so Google research was needed to identify the correct spelling of each company name. This project is a Dash application that helps determine which companies should be merged by using a fuzzy-matching method.

The project aims to produce clean, reliable data. It is inspired by a real use case from professional experience, but all data used in this project is fictional.

## How it works

The app reads a company dataset and compares inactive companies with active ones using fuzzy matching from the TheFuzz library.

1. Company names are cleaned to remove digits, spaces, special characters, and recurring business keywords.
2. Similarity scores are calculated between the target company and all candidate companies.
3. The algorithm keeps the two closest matches and ranks them using a total score built from multiple fuzzy comparisons.
4. The Dash interface lets the user select a company and visualize the top two similar matches, or generate the full matching results as a CSV.

This workflow is designed to support data deduplication and help teams merge records that represent the same company under slightly different spellings.

## Installation

```bash
git clone https://github.com/MGDjimison/fuzzy-matching-maritime
cd maritime_companies
uv sync
```

## Run the application

```bash
cd src
uv run python -m app.main
```

<img src="images/app.png" width="700" />

## Tests

```bash
uv run pytest
```
