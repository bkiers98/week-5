import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
'''
# Titanic Visualization 1

'''
)

st.write(
    '''
    Did women and children have higher survival rates in each class than men?
    '''
    )
# Generate and display the figure
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)

st.write(
'''
# Titanic Visualization 2
'''
)

st.write(
    '''
    Findings: The number of passengers who share a surname does not line up
    with the number and size of family units as calculated by each passenger's
    sibling/spouse and parent/child information. For example, 9 people share
    the name 'Andersson', but there are no calculated family units of nine
    people. This suggests that multiple families shared surnames, and that
    some passengers may have inaccurate family size information. 
    '''
)

st.write(
    '''
    How do the average fares of families compare across the three passenger
    classes?
    '''
)
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)