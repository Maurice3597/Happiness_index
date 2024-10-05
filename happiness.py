import pandas
import streamlit as st
import plotly.express as px

data = pandas.read_csv("happy.csv")


# happiness = list(data["happiness"])
# gdp = list(data["gdp"])
# social_support = list(data["social_support"])
# life_expectancy = list(data["life_expectancy"])
# freedom_to_make_life_choices = list(data["freedom_to_make_life_choices"])
# generosity =list(data["generosity"])
# corruption = list(data["corruption"])

coordinate = list(data.columns)
coordinate = coordinate[1:];print(coordinate)

st.title("In Search For Happiness")
Y_axis = st.selectbox("Select the Variable for the Vertical Axis: ", options=coordinate,
             placeholder="Select a variable for the Y_axis",
             help="Choose the variable that represents the Y_axis")
X_axis = st.selectbox("Select the Variable for the horizontal Axis: ", options=coordinate,
             placeholder="Select a variable for the X_axis",
             help="Choose the variable that represents the V_axis")
