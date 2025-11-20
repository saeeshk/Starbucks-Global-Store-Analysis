import streamlit as st
import pandas as pd

st.title("Starbucks Global Store Analysis Dashboard")

cleaned_url = "https://raw.githubusercontent.com/<username>/<repo>/main/starbucks_cleaned.csv"
country_url = "https://raw.githubusercontent.com/<username>/<repo>/main/country_features_opportunity.csv"
cluster_url = "https://raw.githubusercontent.com/<username>/<repo>/main/clusters_summary.csv"

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

st.header("Cleaned Starbucks Dataset")
st.dataframe(load_data(cleaned_url))

st.header("Country Features & Opportunity Score")
st.dataframe(load_data(country_url))

st.header("Cluster Summary")
st.dataframe(load_data(cluster_url))
