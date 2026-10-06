import plotly.express as px
import pandas as pd

# update/add code below ...
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


def survival_demographics():
    df['age_group'] = pd.cut(df['age'], \
                             bins=[-1, 12, 19, 59, 999], \
                             labels=['Child', 'Teen', 'Adult', 'Senior'])

    df_class = df.groupby('pclass').agg( \
                        n_passengers=('passengerid', 'sum'), \
                        n_survivors=('survived', 'sum'))
    df_class['survival_rate'] = df_class['n_passengers'] / df_class['n_survivors']
    

    return df_class
