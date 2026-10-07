import plotly.express as px
import pandas as pd

# update/add code below ...
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

def survival_demographics():
    '''
    This function groups the df by class, sex, and age group, and returns
    a DataFrame of aggregate values for each.
    '''
    df['age_group'] = pd.cut(df['age'], \
                             bins=[-1, 12, 19, 59, 999], \
                             labels=['Child', 'Teen', 'Adult', 'Senior'])

    df_demographics = df.groupby(['pclass', 'sex', 'age_group'], \
                          observed=False).agg( \
                            n_passengers=('passengerid', 'sum'), \
                            n_survivors=('survived', 'sum')) \
                            .sort_values(by=['sex', 'age_group']) \
                            .reset_index()
    df_demographics['survival_rate'] = df_demographics['n_survivors'] \
                                / df_demographics['n_passengers']
    
    return df_demographics


def visualize_demographic():
    '''
    This function returns a px bar chart showing survival rates across
    classes and age groups.
    '''
    fig = px.bar(survival_demographics(), x='pclass', y='survival_rate', \
                color='sex', barmode='group', facet_col='age_group', \
                title='Survival Rates by Class and Age Group', \
                labels={
                    'pclass': 'Class', 
                    'survival_rate': 'Survival Rate',
                    'sex': 'Sex', 
                    'age_group': 'Age Group'
                    })
    fig.for_each_annotation(lambda label: label.update( \
                            text=label.text.split('=')[1]))
    return fig


def family_groups():
    '''
    This function calculates the family size of each passenger and returns
    an updated DataFrame with information about the ticket fares of different
    family groups.
    '''
    df['family_size'] = df['sibsp'] + df['parch'] + 1
    df_families = df.groupby(['family_size', 'pclass']).agg( \
                            n_passengers=('passengerid', 'count'), \
                            avg_fare=('fare', 'mean'), \
                            min_fare=('fare', 'min'), \
                            max_fare=('fare', 'max')) \
                            .sort_values(by=['pclass', 'family_size']) \
                            .reset_index()
    return df_families


def last_names():
    '''
    This function extracts the last name of each passenger from the name
    column and returns a Series with each last name and the number of
    passengers with whom it is associated.
    '''
    df['last_names'] = df['name'].str.split(',').str[0]
    df_last_names = df['last_names'].value_counts()

    return df_last_names


def visualize_families():
    '''
    This function returns a px box chart showing fare distribution
    across classes.
    '''
    fig = px.box(family_groups(), x='pclass', y='avg_fare', \
              title='Fare Distribution by Class', \
                labels={'pclass': 'Class', 'avg_fare': 'Average Fare'})
    return fig