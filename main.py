import streamlit as st
from app_pages import data_overview, matchups

st.set_page_config(page_title="Matchup Stats Explorer - Valiant Baguette", page_icon="📊", layout="wide")

st.markdown("<h1 style= 'white-space: nowrap;'> Welcome to the Matchups Data Explorer</h1>", unsafe_allow_html=True)


data_overview_page = st.Page("app_pages/data_overview.py", title="Data Overview", icon="📊")
matchups_page = st.Page("app_pages/matchups.py", title="Matchups", icon="⚔️")

pg = st.navigation([data_overview_page, matchups_page])
pg.run()
