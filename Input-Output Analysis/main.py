#%%
import sys
import pandas as pd

def calc_PRoI(investment_scenario,saving_scenario):

    investment = investment_scenario['V'].sum().sum()
    saving = saving_scenario['V'].sum().sum()

    return saving/investment


def calc_PPBT(PRoI):
    return 1/PRoI


def calc_impact(investment_scenario,saving_scenario,p_lifetime,impact,matrix):

    saving = saving_scenario[matrix].loc[impact,:].sum().sum()
    investment = investment_scenario[matrix].loc[impact,:].sum().sum()

    return investment - p_lifetime * saving

#%%
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
# Scenarios and their p_lifetime

scenarios = {
    "Biomass" : 10, 
    "Ecopulpers" : 10, 
    "Shading Trees" : 10
    }

#%%
for scenario in scenarios:
    # scenario excel path
    io = f"Scenarios/{scenario}.xlsx"
    # Investment Phase
    kenya.shock_calc(io=io, Y=True, scenario=f"{scenario} Investment")
    kenya.shock_calc(
        io=io, z=True, v=True, e=True, scenario=f"{scenario} Saving"
    )
#%%
# aggregating the database for better visulization
kenya.aggregate(
    io="Data/aggregation.xlsx",
    levels=["Activity", "Commodity", "Factor of production"],
)

#%%
impacts_satellite = {
    "Water" : ['Blue Water','Grey Water','Green Water'],
    "Land"  : ["Proxy Land","Arable land","Permanent crops",],
    "CO2"   : ["CO2 by Electricity and Heat","CO2 by Industry","CO2 by Transport","CO2 by Residential","CO2 by Cement production","CO2 by Other",]
}

impact_value_added = {
    "Labor"   : ["Labor - Skilled","Labor - Semi Skilled","Labor - Unskilled",],
    "Capital" : ["Capital - Machines"],
    "Imports" : ["Import"]
}



#%%
columns = ['PRoI',"PPBT"] + [*impacts_satellite] + [*impact_value_added]
results = pd.DataFrame(0,index=scenarios,columns=columns)

# %%
# calculating the PRoI

for scenario,p_lifetime in scenarios.items():

    investment_scenario = kenya[f"{scenario} Investment"]
    saving_scenario = kenya[f"{scenario} Saving"]

    PRoI = calc_PRoI(
        investment_scenario= investment_scenario,
        saving_scenario= saving_scenario,
        )

    results.loc[scenario,"PRoI"] = PRoI
    results.loc[scenario,"PPBT"] = calc_PPBT(PRoI)

    for impact,items in impacts_satellite.items():
        results.loc[scenario,impact] = calc_impact(
            investment_scenario=investment_scenario,
            saving_scenario=saving_scenario,
            p_lifetime=p_lifetime,
            impact = items,
            matrix = "E"
        )

    for impact,items in impact_value_added.items():
        results.loc[scenario,impact] = calc_impact(
            investment_scenario=investment_scenario,
            saving_scenario=saving_scenario,
            p_lifetime=p_lifetime,
            impact = items,
            matrix = "V"
        )


# %%
