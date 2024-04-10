import streamlit as st

st.write('Hello mundo!')

import pandas as pd
#from io import StringIO
import matplotlib.pyplot as plt

dfPlot = pd.read_csv('20240402_022821_YPF.Nq.LACh-465(h).csv', skiprows=[1])
st.write(dfPlot.head(4))

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()

ax1.plot(dfPlot['DEPTH'], dfPlot['ROP'], c='red', label='ROP', linewidth = 0.8)

ax2.plot(dfPlot['DEPTH'], dfPlot['GRCX'], c='green', label='GR', linewidth = 0.8)

#plt.xlim(5000, 5100)
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
