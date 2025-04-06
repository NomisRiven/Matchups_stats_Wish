import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv('2025_LoL_esports_match_data_from_OraclesElixir.csv')
    df_sorted_1 = df[['gameid', 'league', 'year', 'split', 'playoffs', 'date', 'game', 'patch', 'side', 'position', 'playername', 'teamname', 'champion', 'result', 'kills', 'deaths', 'assists', 'void_grubs', 'opp_void_grubs', 'firsttower', 'towers', 'turretplates', 'opp_turretplates', 'dpm', 'earnedgold', 'total cs', 'minionkills', 'golddiffat10', 'xpdiffat10', 'csdiffat10', 'killsat10', 'assistsat10', 'deathsat10',	'opp_killsat10', 'opp_assistsat10',	'opp_deathsat10', 'golddiffat15', 'xpdiffat15', 'csdiffat15', 'killsat15', 'assistsat15', 'deathsat15', 'opp_killsat15', 'opp_assistsat15',	'opp_deathsat15', 'golddiffat20', 'xpdiffat20', 'csdiffat20', 'killsat20', 'assistsat20', 'deathsat20', 'opp_killsat20', 'opp_assistsat20',	'opp_deathsat20', 'golddiffat25', 'xpdiffat25', 'csdiffat25', 'killsat25', 'assistsat25', 'deathsat25', 'opp_killsat25', 'opp_assistsat25',	'opp_deathsat25']]
    return df_sorted_1