import pandas as pd

# Utilizing Jupyter Notebook, and utilizing data set https://github.com/fivethirtyeight/data/tree/master/thanksgiving-2015

data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
print(data['Do you celebrate Thanksgiving?'].value_counts())

data = data[data["Do you celebrate Thanksgiving?"] == "Yes"]

data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()

data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]["Do you typically have gravy?"]

ate_pies = (pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
&
pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])
&
pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])

ate_pies.value_counts()

def extract_age(age_value):
    if pd.isnull(age_value):
        return None
    age_str = age_value.split(" ")[0].replace("+", "")
    return int(age_str)

data['int_age'] = data['Age'].apply(extract_age)

def extract_household_income(income_value):
    if pd.isnull(income_value):
        return None
    income_str = income_value.split(" ")[0]
    if income_str == "Prefer":
        return None
    income_str = income_str.replace("$", "")
    income_str = income_str.replace(",", "")
    return int(income_str)

data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(extract_household_income)
data["int_income"].describe()  



data[data["int_income"] < 150000]["How far will you travel for Thanksgiving?"].value_counts()

data[data["int_income"] > 150000]["How far will you travel for Thanksgiving?"].value_counts()

data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_age"
)

data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)
