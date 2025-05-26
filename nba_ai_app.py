
import streamlit as st

st.set_page_config(page_title='Obsidian NBA AI', layout='wide')

from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=1800000, key="auto-refresh")

st.title("🏀 Obsidian NBA AI 2.0")
st.write("This is your custom NBA AI model interface. Auto-updates every 30 mins.")

# Simulated output (Replace with real AI model logic)
st.success("Top Prop: Jalen Brunson OVER 24.5 PTS (Confidence: 91%)")
st.success("Safe 2-Man: Brunson OVER PTS + Hartenstein OVER REB (Confidence: 89%)")
