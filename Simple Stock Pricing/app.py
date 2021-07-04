import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Apple Inc.

""")

#define the tickerSymbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2011-6-30', end='2021-6-30')

# Open      High        Low     Close      Volume       Dividends       Stocks Splits
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)