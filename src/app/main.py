import polars as pl
from dash import Dash, Input, Output, dcc, html

from app.constants import MARITIME_COMPANIES_FILEPATH, TOP2_SIMILAR_COMPANIES_FILEPATH
from app.utils import (
    compute_top2_similar_companies,
    create_chart_top2_similar_companies,
    get_top2_similar_companies,
)

if __name__ == "__main__":
    df = pl.read_csv(MARITIME_COMPANIES_FILEPATH)
    inactive_companies = (
        df.filter(pl.col("is_active") == False).select("name").to_series().to_list()
    )
    app = Dash(__name__)

    # create a simple layout with a text input and a button to trigger the search top 2 similar companies
    app.layout = html.Div(
        [
            html.H3("Top 2 Similar Companies"),
            dcc.Dropdown(
                id="company-input",
                options=[
                    {"label": company, "value": company}
                    for company in inactive_companies
                ],
                placeholder="Select a company",
            ),
            dcc.Graph(id="output-chart"),
            html.P(
                "Or click the button below to compute the top 2 similar companies for all inactive companies."
            ),
            dcc.Button(
                "Compute Top 2 Similar Companies", id="compute-button", n_clicks=0
            ),
            html.Div(id="output-message"),
        ],
        style={"width": "70%", "margin": "auto", "textAlign": "center"},
    )

    # create a callback to update the chart based on the selected company
    @app.callback(Output("output-chart", "figure"), Input("company-input", "value"))
    def update_bar_chart(value: str):
        if value:
            top2_df = get_top2_similar_companies(value, df)
            fig = create_chart_top2_similar_companies(top2_df)
            return fig

    # create a callback to compute the top 2 similar companies for all inactive companies
    @app.callback(
        Output("output-message", "children"), Input("compute-button", "n_clicks")
    )
    def compute_top2_similar_companies_callback(n_clicks: int):
        if n_clicks > 0:
            result_df = compute_top2_similar_companies(df)
            result_df.write_csv(TOP2_SIMILAR_COMPANIES_FILEPATH)
            return html.Span(
                f"Saved {len(result_df)} matches for {len(inactive_companies)} companies.",
                className="success-message",
            )

    app.run(debug=True, port=8050)
