import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


@st.cache_data
def load_data():
    file_path = "species-filter-results(1).csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)

df = load_data()




# categories (sorted in asc order)
rl_category_mapping = {
    "LC": "Least Concern (LC)",
    "NT": "Near Threatened (NT)",
    "VU": "Vulnerable (VU)",
    "EN": "Endangered (EN)",
    "CR": "Critically Endangered (CR)",
    "EW": "Extinct in the Wild (EW)",
    "EX": "Extinct (EX)"
}
sorted_rl_categories = ["Least Concern (LC)", "Near Threatened (NT)", "Vulnerable (VU)", "Endangered (EN)", "Critically Endangered (CR)", "Extinct in the Wild (EW)", "Extinct (EX)"]
df["RL Category Full"] = df["RL Category"].map(rl_category_mapping)

st.sidebar.header("Filter Data")





# filters on side
family_filter = st.sidebar.multiselect("Select Family", df["Family"].unique())
rl_category_filter = st.sidebar.multiselect("Select RL Category (Red List Category)", sorted_rl_categories)
common_name_filter = st.sidebar.text_input("Search by Common Name")
scientific_name_filter = st.sidebar.text_input("Search by Scientific Name")

filtered_df = df





if family_filter:
    filtered_df = filtered_df[filtered_df["Family"].isin(family_filter)]
if rl_category_filter:
    selected_rl_values = [key for key, value in rl_category_mapping.items() if value in rl_category_filter]
    filtered_df = filtered_df[filtered_df["RL Category"].isin(selected_rl_values)]
if common_name_filter:
    filtered_df = filtered_df[filtered_df["Common name"].str.contains(common_name_filter, case=False, na=False)]
if scientific_name_filter:
    filtered_df = filtered_df[filtered_df["Scientific name"].str.contains(scientific_name_filter, case=False, na=False)]


