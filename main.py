import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px

st.set_page_config(
    page_title="Research Demo",
    page_icon=":microscope:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": "This is a demo for research purposes."
    }
)

st.header("Research Demo")

# Initialize session state for the DataFrame
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["Total Rotation Speed (X1)", "Feed (X2)", "Shoulder Pin Dia (X3)", "Temperature (X4)", "Force (Y1)", "Torque (Y2)", "Result"])

with st.container(border=True):
    # Create input fields for each column
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    input1 = col1.number_input("Total Rotation Speed (X1)", value=0.00)
    input2 = col2.number_input("Feed (X2)", value=0.00)
    input3 = col3.number_input("Shoulder Pin Dia (X3)", value=0.00)
    input4 = col4.number_input("Temperature (X4)", value=0.00)
    input5 = col5.number_input("Force (Y1)", value=0.00)
    input6 = col6.number_input("Torque (Y2)", value=0.00)

    # Calculate the result in the desired format
    result = f"a{input1} + a{input2} + a{input3} + a{input4} + a{input5} + a{input6} + C"

    if st.button("Submit"):
        # Create a new row as a DataFrame
        new_row = pd.DataFrame({
            "Total Rotation Speed (X1)": [input1],
            "Feed (X2)": [input2],
            "Shoulder Pin Dia (X3)": [input3],
            "Temperature (X4)": [input4],
            "Force (Y1)": [input5],
            "Torque (Y2)": [input6],
            "Result": [result]
        })
        
        # Concatenate the new row to the existing DataFrame
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)

# Display the DataFrame as a table
st.write(st.session_state.df)

# Create and display charts based on the table data
if not st.session_state.df.empty:    
    st.header("Charts based on Data")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Line chart
    col1.subheader("Line Chart")
    col1.line_chart(st.session_state.df.set_index('Result'))

    # Bar chart
    col2.subheader("Bar Chart")
    col2.bar_chart(st.session_state.df.set_index('Result'))

    # Area chart
    col3.subheader("Area Chart")
    # area = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    col3.area_chart(st.session_state.df.set_index('Result'))

    # Scatter plot
    col4.subheader("Scatter Plot")
    col4.scatter_chart(st.session_state.df, x='Total Rotation Speed (X1)', y='Force (Y1)', color='Result')

# Display a map of Bangalore
df_blr = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [12.971599, 77.594566],
    columns=['lat', 'lon']
)

st.subheader("Demo Scatter Plot on Bengaluru Map")
st.map(df_blr)



st.header("Demo Graphs")

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

# Scatter plot using Plotly Express
df_iris = px.data.iris()  # iris is a pandas DataFrame
fig_scatter = px.scatter(df_iris, x="sepal_width", y="sepal_length", title="Iris Dataset Scatter Plot")

# Plot scatter plot
st.plotly_chart(fig_scatter, key="iris_scatter")

# Scatter plot with additional features
fig_scatter_enhanced = px.scatter(
    df_iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
    title="Enhanced Iris Dataset Scatter Plot"
)

# Plot enhanced scatter plot
st.plotly_chart(fig_scatter_enhanced, key="iris_scatter_enhanced")


# st.subheader("Demo colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
    title = "Iris Dataset Scatter Plot with Red Color Scale"
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title="Population Dataset Scatter Plot"
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
