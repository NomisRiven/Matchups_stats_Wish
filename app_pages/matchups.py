import streamlit as st
import pandas as pd
from utils.data_loader import load_data  

df = load_data()

st.subheader("⚔️ General Matchup Stats")

champions = df['champion'].unique()

selected_champions = st.multiselect("Select two champions to compare", options=champions, default=champions[:2])

# Ensure that exactly two champions are selected
if len(selected_champions) == 2:
    champion_1, champion_2 = selected_champions
    
    # Find games where both champions played. We'll use 'gameId' to match them.
    # First, filter the rows for the selected champion and store the games (gameId).
    champion_1_games = df[df['champion'] == champion_1]['gameid'].unique()
    champion_2_games = df[df['champion'] == champion_2]['gameid'].unique()
    
    # Find the intersection of games where both champions played
    common_games = list(set(champion_1_games) & set(champion_2_games))
    
    # Now, filter the dataframe for those common games and make sure to capture both champions' data
    matchup_df = df[df['gameid'].isin(common_games)]
    
    # Now, we need to pair champions in the same game. We can do this by checking that the 'role' and 'gameId' match
    # and that the champion played by the second player is the opponent.
    
    # For each gameId, we create a new column 'opponent' to show the champion of the opponent.
    matchup_df['opponent'] = matchup_df.groupby('gameid')['champion'].transform(
        lambda x: x[x != x.iloc[0]].values[0] if len(x) > 1 else None
    )
    
    # Now filter the dataframe where the opponent matches the other selected champion
    matchup_df = matchup_df[
        ((matchup_df['champion'] == champion_1) & (matchup_df['opponent'] == champion_2)) |
        ((matchup_df['champion'] == champion_2) & (matchup_df['opponent'] == champion_1))
    ]
    
    # Display filtered data for the matchup
    st.dataframe(matchup_df, use_container_width=True)
    
    # Display average stats for the matchup
    avg_matchup_stats = matchup_df[['kills', 'deaths', 'assists', 'dpm', 'earnedgold']].mean()
    st.write(f"Average Stats for {champion_1} vs {champion_2}:")
    st.write(avg_matchup_stats)
else:
    st.warning("Please select exactly two champions to compare.")