import streamlit as st
import pandas as pd
st.title('Doing Streamlit')
st.header('Random Heading')
st.write("This is my website")

df = pd.DataFrame({
    'Name' : ["John","Alex","Mayo","Lara"],
    "Marks" : [92,96,97,99]
})
st.write(df)
st.write(df.head(2))

st.header('Visualisation')
st.line_chart(df['Marks'])
