import polars as pl
from app.constants import MARITIME_COMPANIES_FILEPATH
from app.utils import create_chart_top2_similar_companies, get_top2_similar_companies
from dash import Dash, dcc, html, Input, Output

if __name__ == "__main__":
    df = pl.read_csv(MARITIME_COMPANIES_FILEPATH)
    inactive_companies = df.filter(pl.col("is_active") == False).select("name").to_series().to_list()
    app = Dash(__name__)

    # create a simple layout with a text input and a button to trigger the search top 2 similar companies
    app.layout = html.Div([
        html.H3('Top 2 Similar Companies'),
        dcc.Dropdown(
            id='company-input',
            options=[{'label': company, 'value': company} for company in inactive_companies],
            placeholder='Select a company'
        ),
        dcc.Graph(id='output-chart'),
    ])

    # create a callback to update the chart based on the selected company
    @app.callback(
        Output('output-chart', 'figure'),
        Input('company-input', 'value')
    )
    def update_bar_chart(value: str):
        if value:
            top2_df = get_top2_similar_companies(value, df)
            fig = create_chart_top2_similar_companies(top2_df)
            return fig

    app.run(debug=True, port=8050)
