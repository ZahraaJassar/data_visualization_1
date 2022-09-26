import streamlit as st
import pandas as pd
import plotly as plt 
import plotly.express as px
from streamlit_option_menu import option_menu
import json
from streamlit_lottie import st_lottie
import requests

df = pd.read_csv("gdp_1960_2020.csv")

with st.sidebar:
  selected = option_menu(
    menu_title= "Main Menu",
    options= ["Home", "Data Summary", "Continental GDP", "Country Plot"],
    icons= ["house", "book", "globe", "geo-alt-fill"],
  )

if selected == "Home":
 st.title("Global GDP evolution from 1960-2020")
 st.caption('This dashboard explores the Global GDP evolution over 60 years')
 def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
      return None
    return r.json()
 lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_MjPjfi.json")
 st_lottie(
      lottie_hello,
      speed= 0.5,
      loop= True,
      quality= "low",
      height= None,
      width= None,
      key= None,
    )
    
if selected == "Data Summary":
  st.subheader('GDP of countries from 1960-2020')
  st.write(df.head(20))
if selected == "Continental GDP":
  selected2 = option_menu(
    menu_title= "Continental GDP",
    options= [" change over time", " contribution for one year"],
    orientation= "horizontal",
    icons= ["percent", "percent"], )
  if selected2 == " change over time":
      st.subheader('Continental GDP percentage change over time')
      fig = px.bar(df, x="state", y="gdp_percent", color="state",
      animation_frame="year", animation_group="state", range_y=[0,1], title= "Continental GDP percentage change over time")
      st.plotly_chart(fig)
  if selected2 == " contribution for one year":
      st.subheader("Continental GDP percentage distribution for one year")
      yearss= (1960, 1970, 1980, 1990, 2000, 2010, 2020)
      drop= st.selectbox("Select a year", yearss)
      gdp_per= df[["year", "state", "gdp_percent"]]
      gdp_years= gdp_per.loc[gdp_per["year"] == drop]
      fig5 = px.pie(gdp_years, values='gdp_percent', names='state', title= "Continents' yearly contribution to the global GDP")
      st.plotly_chart(fig5)
if selected == "Country Plot":
  selected3 = option_menu(
    menu_title= "National GDP",
    options= ["GDP evolution over time", "GDP rank over time"],
    orientation= "horizontal", 
    icons= ["graph-up", "award"])
  if selected3 == "GDP evolution over time":
      st.subheader('GDP evolution in countries over time')
      countries= ("France", "India",'China', 'Japan', 'Italy', 'the United States', 'United Kingdom', 'Canada', 'Australia', 'Brazil', 'Sweden', 'Egypt')
      dropdown= st.selectbox("Select Country", countries)
      gdp5= df[["year", "country", "gdp"]]
      gdp_fr= gdp5.loc[gdp5["country"] == dropdown]
      fr= gdp_fr.sort_values(by= ["year"])
      fig2 = px.line(fr, x="year", y="gdp", title='GDP variation in countries over time')
      st.plotly_chart(fig2)
  if selected3 == "GDP rank over time":
    st.subheader("Change of countries' GDP rank over time")
    count= ("France", "India",'China', 'Japan', 'Italy', 'the United States', 'United Kingdom', 'Canada', 'Australia', 'Brazil', 'Sweden', 'Egypt')
    dropdown2= st.selectbox("Select a country", count)
    gdp2= df[["year", "gdp", "country", "rank"]]
    ind= gdp2.loc[gdp2["country"] == dropdown2]
    fig3 = px.scatter(ind, x="year", y="rank", size="gdp", hover_name="country", log_x=True, size_max=60, title= "Country's GDP's global economic rank")
    st.plotly_chart(fig3)











  