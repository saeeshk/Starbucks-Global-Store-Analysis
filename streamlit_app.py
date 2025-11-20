import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide", page_title="Starbucks Analysis")

st.title("Starbucks Global Store Analysis Dashboard")

# LOCAL paths (from your upload)
LOCAL_CLEANED = "/mnt/data/starbucks_cleaned (1).csv"
LOCAL_COUNTRY = "/mnt/data/country_features_opportunity.csv"
LOCAL_CLUSTER = "/mnt/data/clusters_summary.csv"

# optional: remote raw GitHub fallbacks (edit if you want)
GITHUB_CLEANED = "https://raw.githubusercontent.com/<your-username>/<repo>/main/starbucks_cleaned.csv"
GITHUB_COUNTRY = "https://raw.githubusercontent.com/<your-username>/<repo>/main/country_features_opportunity.csv"
GITHUB_CLUSTER = "https://raw.githubusercontent.com/<your-username>/<repo>/main/clusters_summary.csv"

@st.cache_data
def load_csv(preferred_local_path, fallback_url=None):
    """
    Try to load CSV from a provided local path first.
    If not available, try fallback_url (raw github URL).
    Returns a DataFrame or raises the original exception.
    """
    # 1) local
    if preferred_local_path and os.path.exists(preferred_local_path):
        try:
            return pd.read_csv(preferred_local_path)
        except Exception as e:
            # if local exists but fails to read, raise so user can inspect
            raise RuntimeError(f"Failed to read local file {preferred_local_path}: {e}") from e

    # 2) fallback remote URL (optional)
    if fallback_url:
        try:
            return pd.read_csv(fallback_url)
        except Exception as e:
            raise RuntimeError(f"Failed to read remote fallback {fallback_url}: {e}") from e

    # 3) neither present
    raise FileNotFoundError(
        f"Neither local file found at {preferred_local_path} nor fallback URL provided/working."
    )

st.header("Datasets (loaded from local paths if available)")

# Load and show cleaned dataset
try:
    df_cleaned = load_csv(LOCAL_CLEANED, fallback_url=GITHUB_CLEANED)
    st.subheader("Cleaned Starbucks Data")
    st.write(f"Loaded from: {LOCAL_CLEANED if os.path.exists(LOCAL_CLEANED) else 'remote fallback'}")
    st.dataframe(df_cleaned.head(200))
except Exception as e:
    st.error("Could not load cleaned dataset.")
    st.code(str(e))

# Country features
try:
    df_country = load_csv(LOCAL_COUNTRY, fallback_url=GITHUB_COUNTRY)
    st.subheader("Country Features & Opportunity Score")
    st.write(f"Loaded from: {LOCAL_COUNTRY if os.path.exists(LOCAL_COUNTRY) else 'remote fallback'}")
    st.dataframe(df_country.head(200))
except Exception as e:
    st.error("Could not load country features dataset.")
    st.code(str(e))

# Cluster summary
try:
    df_cluster = load_csv(LOCAL_CLUSTER, fallback_url=GITHUB_CLUSTER)
    st.subheader("Cluster Summary")
    st.write(f"Loaded from: {LOCAL_CLUSTER if os.path.exists(LOCAL_CLUSTER) else 'remote fallback'}")
    st.dataframe(df_cluster.head(200))
except Exception as e:
    st.error("Could not load clusters dataset.")
    st.code(str(e))

st.markdown("---")
st.info("If you still see errors: check that the files exist in the repository or in the runtime at the exact paths shown above.")
