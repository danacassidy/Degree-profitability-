import pandas as pd
import streamlit as st
import seaborn as sns



df = pd.read_csv(r'/Users/danacassidy/Downloads/degrees-that-pay-back.csv', index_col=0)

df.drop('Percent change from Starting to Mid-Career Salary', axis=1, inplace=True)
st.markdown("## Undergraduate Majors and salaries")

st.table(df)


df2 = pd.read_csv(r'/Users/danacassidy/Downloads/degrees-that-pay-back.csv', index_col=0)
useless_cols = ['Percent change from Starting to Mid-Career Salary','Mid-Career Median Salary',
                'Mid-Career 10th Percentile Salary','Mid-Career 25th Percentile Salary',
                'Mid-Career 75th Percentile Salary','Mid-Career 90th Percentile Salary']


df2.drop(useless_cols, axis=1, inplace=True)

st.markdown("## Starting salaries highest to lowest by major")
sort_by_salary= df2.sort_values('Starting Median Salary', ascending = False)

st.table(df2)






