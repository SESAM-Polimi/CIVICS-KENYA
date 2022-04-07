#%%
import sys

sys.path.append("/Users/mohammadamintahavori/Documents/GitHub/MARIO")

from mario import parse_from_excel, set_log_verbosity

set_log_verbosity("CRITICAL")
#%%
kenya = parse_from_excel(
    path="Data/database.xlsx",
    table="SUT",
    year=2014,
    name="CIVICS Kenya",
    source="Causapé, A.J.M.; Boulanger, P.; Dudu, H.; Ferrari, E.; Mcdonald, S. Social Accounting Matrix of Kenya; 2014; ISBN 978-92-79-77708-0.",
)

#%%
# Aggregation on consumption categories
kenya.aggregate(
    io="Data/aggregation.xlsx", levels="Consumption category",
)
# %%
# priniting datbase info
print(kenya)
#%%
# Checking the database balance
kenya.is_balanced("coefficients")
#%%
scenarios = ["Biomass", "Ecopulpers", "Shading Trees"]

#%%
for scenario in scenarios:
    # scenario excel path
    io = f"Scenarios/{scenario}.xlsx"
    # Investment Phase
    kenya.shock_calc(io=io, Y=True, scenario=f"{scenario} Investment")
    kenya.shock_calc(
        io=io, z=True, v=True, e=True, scenario=f"{scenario} non Investment"
    )
#%%
# aggregating the database for better visulization
kenya_aggregated = kenya.aggregate(
    io="Data/aggregation.xlsx",
    levels=["Activity", "Commodity", "Factor of production"],
    inplace=False,
)
# %%
