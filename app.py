import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

# --- CONFIGURATION FROM SECRETS --

MEETING_DATE = datetime(2024, 10, 8, 0, 0)

# --- PAGE SETUP ---
st.set_page_config(page_title="S²: The Saga", page_icon="❤️")

tab1 = st.tabs(["🕒 Our Journey"])

with tab1:
    st.header("Time Since First 'Hello'")
    diff = datetime.now() - MEETING_DATE
    col1, col2, col3 = st.columns(3)
    col1.metric("Days", diff.days)
    col2.metric("Hours", diff.seconds // 3600)
    col3.metric("Minutes", (diff.seconds // 60) % 60)

    st.write("---")






