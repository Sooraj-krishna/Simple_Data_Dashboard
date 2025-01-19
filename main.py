import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file=st.file_uploader("Upload The CSV File", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)

    st.subheader("Data Priviwe")
    st.write(df.head())

    st.subheader("Data Description")  
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select Column To Filter By", columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select Values", unique_values)

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)

    st.subheader("Plot Data")
    y_column = st.selectbox("Select Y-axis Column", columns)
    x_column = st.selectbox("Select X-axis Column", columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting For File Upoladng...")