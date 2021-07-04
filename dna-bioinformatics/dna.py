#importing libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# page title

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""

# DNA Nucleotide Count Web App

This app counts the nucleotide cimposition of query DNA!

***
""")

