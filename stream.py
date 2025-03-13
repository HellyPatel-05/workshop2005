import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Cloud App")
st.write("Here's a quick example of a cloud app built with Streamlit.")
df=pd.DataFrame(np.random.randn(10,2),columns=['Col1','Col2'])
st.dataframe(df)
# pamda upper case  ## streamlit lower case
# streamlit integrated in github 
