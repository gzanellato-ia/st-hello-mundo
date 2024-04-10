import streamlit as st

st.write('Hello mundo!')

import numpy as np
import pandas as pd
#from io import StringIO
import matplotlib.pyplot as plt

df1 = pd.read_csv('20240402_022821_YPF.Nq.LACh-465(h).csv', skiprows=[1])
st.write(df1.head(4))

DepthIn = 2624
DepthOut = 2651
dfPlot = df1[(df1['DEPTH']>DepthIn) & (df1['DEPTH']<DepthOut)]

# Plotting -----------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()

ax1.plot(dfPlot['DEPTH'], dfPlot['ROP'], c='red', label='ROP', linewidth = 0.8)

ax2.plot(dfPlot['DEPTH'], dfPlot['GRCX'], c='green', label='GR', linewidth = 0.8)

ax1.set_xlim(2620, 2660)
ax1.set_ylim(0, 50)
ax2.set_ylim(0, 180)
ax1.legend(loc="lower left")
ax2.legend(loc="lower center")

# giving labels to the axises
ax1.set_xlabel('DEPTH(m)')
ax1.set_ylabel('ROP(m/h)')

# secondary y-axis label
ax2.set_ylabel('GR(api)')

ax1.set_yticks(np.arange(0, 60.1, 60/6))
ax2.set_yticks(np.arange(0, 180.1, 180/6)) #, minor=True)

plt.grid(linestyle = '--', linewidth = 0.4)

#plt.savefig("Curva_ROP_GR.png")
st.pyplot(fig)


