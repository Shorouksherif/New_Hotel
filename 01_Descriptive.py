import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('df.csv')

df.drop('Unnamed: 0', axis=1, inplace=True)

# Set up the Streamlit page configuration
st.set_page_config(
    layout='wide',
    page_title='Descriptive Analysis',
    page_icon='📊'
)

st.markdown('<h1 style="text-align:center; color: #4169E1;">Descriptive Analysis</h1>', unsafe_allow_html=True)

# Create tabs for different analyses
tap1, tap2 = st.tabs(['📈 Numeric', '📊 Categorical'])

# Numeric Descriptive Statistics
with tap1:
    st.subheader('Numerical Descriptive Statistics')
    
    # Filter for numerical columns
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    selected_numeric_column = st.selectbox('Select a numeric column:', options=['All Columns'] + numeric_columns)

    if selected_numeric_column == 'All Columns':
        # Display overall numerical statistics
        st.subheader('All Numerical Columns Descriptive Statistics')
        num = df.describe()
        st.dataframe(num.T, 500, 400)
    else:
        # Display descriptive statistics for the selected numeric column
        st.subheader(f'Descriptive Statistics for: {selected_numeric_column}')
        num_stats = df[selected_numeric_column].describe().to_frame().T
        st.dataframe(num_stats, 500, 400)

# Categorical Descriptive Statistics
with tap2:
    st.subheader('Categorical Descriptive Statistics')
    
    # Filter for categorical columns
    categorical_columns = df.select_dtypes(include='object').columns.tolist()
    selected_categorical_column = st.selectbox('Select a categorical column:', options=['All Columns'] + categorical_columns)

    if selected_categorical_column == 'All Columns':
        # Display overall categorical statistics
        st.subheader('All Categorical Columns Descriptive Statistics')
        cat = df.describe(include='O')
        st.dataframe(cat.T, 500, 400)
    else:
        # Display descriptive statistics for the selected categorical column
        st.subheader(f'Descriptive Statistics for: {selected_categorical_column}')
        # For categorical columns, we show count, unique, top, freq
        cat_stats = df[selected_categorical_column].describe().to_frame().T
        st.dataframe(cat_stats, 500, 400)
