import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time
from PIL import Image
import base64

st.set_page_config(page_title="SMART WATER GRID", layout="wide")

def sidebar_bg(side_bg):

   side_bg_ext = 'png'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = 'logo.png'
sidebar_bg(side_bg)
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
nplaceholder = st.empty()
if live_val:
    analytics=False
    for seconds in range(200):
        val=np.random.choice(range(0,150))
        with placeholder.container():
            st.subheader('Live Values')
            col1, col2 = st.columns(2,gap="small")
            with col1:
                st.markdown(f'<h5>P1</h5>', unsafe_allow_html=True)
                fig = go.Figure()

                fig.add_trace(go.Indicator(
                    name = "my_trace",
                    domain={'x': [0, 1], 'y': [0, 1]},
                    value=val,
                    mode="gauge+number+delta",
                    title={'text': "Presure - P1"},
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
    
    for seconds in range(200):
        val=np.random.choice(range(0,150))
        with nplaceholder.container():
            ncol1, ncol2 = st.columns(2,gap="small")
            with ncol1:
                st.markdown(f'<h5>P2</h5>', unsafe_allow_html=True)
                fig = go.Figure()
                fig.add_trace(go.Indicator(
                    name = "my_trace",
                    domain={'x': [0, 1], 'y': [0, 1]},
                    value=val,
                    mode="gauge+number+delta",
                    title={'text': "Presure - P2"},
                    delta={'reference': 50},
                    gauge={'axis': {'range': [None, 500]},
                    'steps': [
                        {'range': [0, 250], 'color': "lightgray"},
                        {'range': [250, 400], 'color': "yellow"},
                        {'range': [400, 500], 'color': "red"}],
                    'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
                st.write(fig)
        
            with ncol2:
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
    df = pd.DataFrame(np.random.randint(25, size=(4, 4)))
    for seconds in range(200):
        val=np.random.choice(range(0,150))
        st.subheader("Analytics")
        col1, col2 = st.columns([3,1])
        col1.line_chart(df, columns=['P','Flow'])
        col2.table(df.head())
    time.sleep(1)
