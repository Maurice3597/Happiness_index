import pandas
import streamlit as st
import plotly.express as px

# Load the file containing the data (hppy.csv
data = pandas.read_csv("happy.csv")

# list of the column headers
coordinate = list(data.columns)
coordinate = coordinate[1:];print(coordinate)

# Titles and Select boxes for variable options
st.title("In Search For Happiness")
Y_axis = st.selectbox("Select the Variable for the Vertical Axis: ", options=coordinate,
             placeholder="Select a variable for the Y_axis",
             help="Choose the variable that represents the Y_axis")
X_axis = st.selectbox("Select the Variable for the horizontal Axis: ", options=coordinate,
             placeholder="Select a variable for the X_axis",
             help="Choose the variable that represents the V_axis")

# Assign the values of the select boxes to variables X and Y
X, Y = list(data[X_axis]), list(data[Y_axis])

# Plots and displays a plot of the selected variables
st.plotly_chart(px.scatter(x=X, y=Y, labels={'x':X_axis, 'y':Y_axis}))