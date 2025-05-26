
import streamlit as st

st.set_page_config(page_title='Obsidian WNBA AI', layout='wide')

from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=1800000, key="auto-refresh")

st.title("🏀 Obsidian WNBA AI")
st.write("This is your custom WNBA AI model. Real-time props and matchup-based predictions.")

# Simulated output (Replace with real AI model logic)
st.success("Top Prop: A'ja Wilson OVER 20.5 PTS (Confidence: 89%)")
st.success("Safe 2-Man: Wilson OVER PTS + Plum OVER AST (Confidence: 87%)")
