import streamlit as st

st.write('Hello mundo!')

import pandas as pd
#from io import StringIO
import matplotlib.pyplot as plt

dfPlot = pd.read_csv('20240402_022821_YPF.Nq.LACh-465(h).csv', skiprows=[1])
st.write(dfPlot.head(4))

