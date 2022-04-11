# CIVICS-KENYA
Enhancing Kenyan Coffee Supply Chain Through Integrated Multidimensional Analysis

# Input-Output Analyis
The model adopted in this research is a demand driven input-output model based on Supply and Use Tables (SUT).
For performing the impact assessment using the Input-Output Analysis, **mario** is used. [**mario**](https://github.com/SESAM-Polimi/MARIO) is a python package for handling input-output tables and scenario analysis.

## How To Use
Inside **Input-Output Analysis** folder, following files can be found:
- **main.py** : The python script for running the scenarios and performing the analysis
- **Data** : This folder contains the database (database.xlsx) and the aggregations inofrmation (aggregation.xlsx)
- **Scenarios** : This filder contains the scenario data in mario format as excel files

## How To Read Scenarios
In mario, scenarios should be defined throguh a multi-sheet excel file. Each excel file contains the following sheets:
- **indeces** : Extra information for tracking the validation of data (not to be used by the user)
- **main** :  Contains all the intermediate calculations along with extra information (like references) for the specific scenario
- **Y** : Represents the changes on *Final Demand* in the specific scenario.
- **z** : Represents the changes on *Intermediate Demand* in the specific scenario.
- **e** : Represents the changes on *Satellite accounts* in the specific scenario.
- **v** : Represents the changes on *Value Added* in the specific scenario.

In the following picture, you can see an example of the **main** sheet:

![example](https://github.com/SESAM-Polimi/CIVICS-KENYA/blob/main/statics/main_example.png?raw=true)

# Energy System Modelling Analyis
The model adopted in this research for modelling the *Kenya Energy System* is a linear programming framework for spatial–temporal energy system optimization called [**calliope**](https://github.com/calliope-project/calliope). This model has been built and tested with **Calliope 0.6.4**. The figure below, shows the geo-spatial structure of the energy model.

![regions](https://github.com/SESAM-Polimi/CIVICS-KENYA/blob/main/statics/Kenya_Regions.png?raw=true)

## How To Use
Inside **Energy System Modelling Analysis** folder, following files can be found:
- **1Node_No_Coffee**  : A single node Kenya energy system model without the coffee biomass intervention
- **4Nodes_No_Coffee** : A four nodes Kenya energy system model without the coffee biomass intervention
- **4Nodes_W_Coffee**  : A four nodes Kenya energy system model with the coffee biomass intervention

Inside every folder, the specific model inputs can be found along with a jupyter file for running the model.





