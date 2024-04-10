import streamlit as st

st.write('Hello mundo!')

import pandas as pd
from io import StringIO

dataframe = pd.read_csv('20240402_022821_YPF.Nq.LACh-465(h).csv', skiprows=[1])
st.write(dataframe)

#uploaded_file = st.file_uploader('20240402_022821_YPF.Nq.LACh-465(h).csv')
#if uploaded_file is not None:
#    # Can be used wherever a "file-like" object is accepted:
#    dataframe = pd.read_csv(uploaded_file, skiprows=[1])
#    st.write(dataframe)
