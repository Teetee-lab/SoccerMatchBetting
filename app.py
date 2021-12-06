import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np
from PIL import Image


html_temp = """
<div style = "background-color:yellow;padding:13px">
<h1 style="color:black;text-align:center;">Soccer Match Fixture Betting App</h1>
</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)


st.image("https://www.pinnacle.com/Cms_Data/Contents/Guest/Media/betting-articles/soccer/strategy/ultimate-guide-soccer-hero.jpg")


st.header("This App predict Soccer match fixture using the Soccer Power Index and the Probabilities of winning at Home or Away.")

st.markdown("""<a href="https://projects.fivethirtyeight.com/global-club-soccer-rankings/">Real-time SPI Rankings</a>""",
            unsafe_allow_html=True)

html= """
<div style = "background-color:yellow;padding:8px">
<h1 style="color:black;text-align:center;">Club Data</h1>
</div>
"""

st.markdown(html,unsafe_allow_html=True)

df= pd.read_csv("Data/soccer-spi/club_data.csv",index_col=0)

st.write(df)

st.subheader("Please Input match data below:")

season = st.number_input(
    label="What season is the match",
    min_value=2016, 
    max_value=2022)

spi1 = st.slider("What is the home team's ESPN SPI rating?", 
                 min_value=1.00, max_value=100.00)

spi2 = st.slider("What is the away team's ESPN SPI rating?",
                 min_value=1.00, max_value=100.00)

prob1 = st.slider("What are the bookmaker odds on the home team winning?",
                 min_value=0.001, max_value=1.000)

prob2 = st.slider("What are the bookmaker odds on the away team winning?",
                 min_value=0.001, max_value=1.000)

probtie = round((1.000 - (prob1 + prob2)), 3)

importance1 = st.number_input(
    label="How important is the match to the Home team?",
    min_value=1.00, 
    max_value=99.00)

importance2 = st.number_input(
    label="How important is the match to the Away team?",
    min_value=1.00, 
    max_value=99.00)

xg1 = st.number_input(
    label="What is the expected goals on the Home team?",
    min_value=0.01, 
    max_value=5.00)

xg2 = st.number_input(
    label="What is the expected goals on the Away team?",
    min_value=0.01, 
    max_value=5.00)


if st.button("Click here to run!"):
    st.subheader("Modeling match results off these features:")
    st.write(f"Season: {season}")
    st.write(f"Home team SPI: {spi1}")
    st.write(f"Away team SPI: {spi2}")
    st.write(f"Bookmaker odds for home win: {prob1}")
    st.write(f"Bookmaker odds for away win: {prob2}")
    st.write(f"Bookmaker odds for tie: {probtie}")
    st.write(f"importance of match to Home team: {importance1}")
    st.write(f"importance of match to Away team: {importance2}")
    st.write(f"prob of expected goals Home team: {xg1}")
    st.write(f"prob of expected goals Away team: {xg2}")
     
    
    deploy_model = pickle.load(open('model.sav','rb'))

    pred = deploy_model.predict([[season, spi1, spi2, prob1, prob2, probtie, importance1,
       importance2, xg1, xg2]])
    
    if pred[0] == 0:
        st.success("The predicted match result is a: Draw")
    elif pred[0] == 1:
        st.success("The predicted match result is : Home Win")
    else:
        st.success("The predicted match result is : Away Win")
            