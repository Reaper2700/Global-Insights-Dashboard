from Data.dataframe import dataframe
import polars as pl
import streamlit as st

def industrialization():
    df = dataframe()

    st.title("### Indicators of industrialization")
    st.write("head", df.head())

industrialization()
