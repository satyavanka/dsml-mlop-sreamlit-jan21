import streamlit as st
import pandas as pd
import yfinance as yf
import altair as alt


ticker_symbol = st.text_input("Enter the stock ticker symbol", "AAPL")

ticker_data = yf.Ticker(ticker_symbol)

starting_date = st.date_input("Enter the starting date", value=pd.to_datetime("2021-01-01"))
ending_date = st.date_input("Enter the ending date", value=pd.to_datetime("today"))


hist = ticker_data.history(start=starting_date, end=ending_date)

st.title("Creating stock market application!")

st.write("This is my app deploying!")

st.write(hist)

c = alt.Chart(hist).mark_circle().encode(
    x='Volume', y='Close', size='Close', color='Close')

st.write(c)




col1,col2 = st.columns(2)

with col1:
    st.write("This plot is for volume of the stock")
    st.line_chart(hist.Volume)

with col2:
    st.write("This plot is for volume of the stock")
    st.line_chart(hist.Close)