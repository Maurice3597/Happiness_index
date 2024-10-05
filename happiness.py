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

coordinate = list(data.columns);print(coordinate)
print("Hello world")
coordinate = coordinate[1:];print(coordinate)

