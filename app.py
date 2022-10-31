
with open('app.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
import streamlit as st
st.set_page_config(page_title="SMART WATER GRID", layout="wide")

with st.container():
    st.title("SMART WATER GRID")
