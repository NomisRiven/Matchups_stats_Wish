import streamlit as st
import pandas as pd
from utils.data_loader import load_data


df = load_data()

st.header("📊 Data Overview")

with st.expander("🔍 Filters"):
    # Filters for roles, results, champions, etc.
    roles = df['position'].unique()
    all_roles_selected = st.checkbox("Select all roles", value=True)
    selected_roles = st.multiselect("Select roles", options=roles, default=roles if all_roles_selected else [])
    result_display_map = {1: "Win", 0: "Lose"}
    result_reverse_map = {v: k for k, v in result_display_map.items()}
    result_options = [result_display_map[r] for r in sorted(df['result'].unique())]
    all_results_selected = st.checkbox("Select all results", value=True)
    selected_result_labels = st.multiselect("Select results", options=result_options, default=result_options if all_results_selected else [])
    selected_results = [result_reverse_map[label] for label in selected_result_labels]
    champions = df['champion'].unique()
    all_champions_selected = st.checkbox("Select all champions", value=True)
    selected_champions = st.multiselect("Select champions", options=champions, default=champions if all_champions_selected else [])
    leagues = df['league'].unique()
    all_leagues_selected = st.checkbox("Select all leagues", value=True)
    selected_leagues = st.multiselect("Select leagues", options=leagues, default=leagues if all_leagues_selected else [])
    patches = df['patch'].unique()
    all_patches_selected = st.checkbox("Select all patches", value=True)
    selected_patches = st.multiselect("Select patches", options=patches, default=patches if all_patches_selected else [])

# Apply filters
filtered_df = df[
    (df['position'].isin(selected_roles)) &
    (df['result'].isin(selected_results)) &
    (df['champion'].isin(selected_champions)) &
    (df['league'].isin(selected_leagues)) &
    (df['patch'].isin(selected_patches)) 
]

# Display filtered data
st.dataframe(filtered_df, use_container_width=True)