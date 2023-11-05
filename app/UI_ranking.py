# app.py

import streamlit as st
import pandas as pd

# Load data
@st.cache_data  # This will cache the data and won't reload unless the file changes.
def load_data():
    return pd.read_csv("data/ranking_dec.csv", index_col=0)

df = load_data()

df.sort_values(by=['score_normal_current'], inplace=True, ascending=False)

# Title
st.title("Team Stats Interactive UI")

# Sidebar Filters
team_names = df.index.unique()
selected_team = st.sidebar.selectbox("Select a Team", team_names)

filtered_df = df[df.index == selected_team]

# Display Data
st.write(df[['score_normal_current']].head(20))
st.write(f"Data for {selected_team}")
st.write(filtered_df)

# Maybe you want to display some stats:
st.write(f"Total Goals: {filtered_df['goals'].sum()}")
st.write(f"Total xgShot: {filtered_df['xgShot'].sum()}")

# Add more features, charts, and interactions as required.

if __name__ == "__main__":
    pass
