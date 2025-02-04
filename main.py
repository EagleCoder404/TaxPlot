from regimes import *
import plotly.express as px
import pandas as pd

salary_range = list(range(0, 20*lakh + 1, 1000))

tax_range_2425 = map(lambda x : get_tax(x, new_regime_2425, rebate=7*lakh), salary_range)
tax_range_2526 = map(lambda x : get_tax(x, new_regime_2526, rebate=12*lakh), salary_range)

df = pd.DataFrame({"salary": salary_range, "tax_2425": tax_range_2425, "tax_2526": tax_range_2526})

fig = px.line(df, x="salary", y=df.columns[1:3], title="babushka")



xticks = list(range(0, 20, 1))
fig.update_layout(
    xaxis = dict(
        tickmode='array',
        tickvals = list(map(lambda x: x*lakh, xticks)),
        ticktext = list(map(lambda x: f'{x}L', xticks)),
    ),
    yaxis = dict(),
    font=dict(size=18, color="black"))

fig.show()