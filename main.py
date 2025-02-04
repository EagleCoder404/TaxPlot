"""The main module"""

import plotly.express as px
import pandas as pd
from tax import get_tax
from tax.regimes import NEW_REGIME_2024, NEW_REGIME_2025, LAKH


salary_range = list(range(0, 20*LAKH + 1, 1000))
tax_range_2024 = map(lambda x : get_tax(x, NEW_REGIME_2024, rebate=7*LAKH), salary_range)
tax_range_2025 = map(lambda x : get_tax(x, NEW_REGIME_2025, rebate=12*LAKH), salary_range)

df = pd.DataFrame({
        "Salary": salary_range, 
        "Tax 2024-25": tax_range_2024, 
        "Tax 2025-26": tax_range_2025
    })

fig = px.line(df, x="Salary", y=df.columns[1:3], title="babushka")



xticks = list(range(0, 20, 1))
fig.update_layout(
    xaxis = dict(
        tickmode='array',
        tickvals = list(map(lambda x: x*LAKH, xticks)),
        ticktext = list(map(lambda x: f'{x}L', xticks)),
    ),
    yaxis = dict(),
    font=dict(size=18, color="black"))

fig.show()
