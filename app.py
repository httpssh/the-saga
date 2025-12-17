import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

# --- CONFIGURATION FROM SECRETS ---
try:
    CLIENT_ID = st.secrets["CLIENT_ID"]
    CLIENT_SECRET = st.secrets["CLIENT_SECRET"]
    PLAYLIST_URL = st.secrets["PLAYLIST_URL"]
except Exception as e:
    st.error(
        "Secrets not found! Make sure secrets.toml or Streamlit Cloud Secrets are set.")
    st.stop()

MEETING_DATE = datetime(2024, 10, 8, 0, 0)

# --- PAGE SETUP ---
st.set_page_config(page_title="S²: The Saga", page_icon="❤️")

tab1, tab2 = st.tabs(["🕒 Our Journey", "🎵 Our Frequency"])

with tab1:
    st.header("Time Since First 'Hello'")
    diff = datetime.now() - MEETING_DATE
    col1, col2, col3 = st.columns(3)
    col1.metric("Days", diff.days)
    col2.metric("Hours", diff.seconds // 3600)
    col3.metric("Minutes", (diff.seconds // 60) % 60)

    st.write("---")

with tab2:
    st.header("The Soundtrack of Us")
    try:
        auth_manager = SpotifyClientCredentials(
            client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        playlist = sp.playlist(PLAYLIST_URL)

        col_l, col_r = st.columns([1, 2])
        col_l.image(playlist['images'][0]['url'])
        col_r.subheader(playlist['name'])

        st.write("### Top Songs:")
        for item in playlist['tracks']['items'][:5]:
            track = item['track']
            st.write(f"🎵 **{track['name']}** - {track['artists'][0]['name']}")
    except:
        st.warning("Check your Spotify URL or API keys.")

