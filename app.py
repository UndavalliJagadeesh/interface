import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time
st.set_page_config(page_title="SMART WATER GRID", layout="wide")
img, name = st.columns([1,20])
with img:
    st.image('logo.png', width=150)
with name:
    st.markdown(f'<h1>VISHNU INSTITUTE OF TECHNOLOGY</h1>',unsafe_allow_html=True)

with open('app.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.title("SMART WATER GRID")



left_bt, right_bt = st.columns(2)
live_val=left_bt.button("Live Values")
analytics=right_bt.button("Analytics")

data = pd.read_csv('DataSet.csv')
placeholder = st.empty()

if live_val:
    analytics=False
    for seconds in range(200):
        val=np.random.choice(range(0,150))
        with placeholder.container():
            st.subheader('Live Values')
            col1, col2 = st.columns(2,gap="small")
            with col1:
                fig = go.Figure()

                fig.add_trace(go.Indicator(
                    name = "my_trace",
                    domain={'x': [0, 1], 'y': [0, 1]},
                    value=val,
                    mode="gauge+number+delta",
                    title={'text': "Presure"},
                    delta={'reference': 50},
                    gauge={'axis': {'range': [None, 500]},
                    'steps': [
                        {'range': [0, 250], 'color': "lightgray"},
                        {'range': [250, 400], 'color': "yellow"},
                        {'range': [400, 500], 'color': "red"}],
                    'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
                st.write(fig)
        
            with col2:
                fig = go.Figure(go.Indicator(
                domain={'x': [0, 1], 'y': [0, 1]},
                value=val**(1.2),
                mode="gauge+number+delta",
                title={'text': "Flow Rate"},
                delta={'reference': 150},
                gauge={'axis': {'range': [None, 500]},
                'steps': [
                    {'range': [0, 250], 'color': "lightgray"},
                    {'range': [250, 400], 'color': "yellow"},
                    {'range': [400, 500], 'color': "red"}],
                    'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
                st.write(fig)
            time.sleep(1)


if analytics:
    live_val=False
    st.subheader("Analytics")
    col1, col2 = st.columns([3,1])
    df = pd.DataFrame(data, columns=['P2 [psi]','P1 [psi]'])
    col1.line_chart(df.head())
    col2.table(df.head())
