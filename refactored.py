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
