
import streamlit as st

st.set_page_config(page_title='Obsidian MLB AI', layout='wide')

from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=1800000, key="auto-refresh")

st.title("⚾ Obsidian MLB AI")
st.write("This is your custom MLB AI model interface. Includes prop predictions and ladder plays.")

# Simulated output (Replace with real AI model logic)
st.success("Top Prop: Corbin Burnes OVER 6.5 K (Confidence: 90%)")
st.success("Safe 2-Man: Burnes OVER Ks + Soto OVER Total Bases (Confidence: 88%)")
