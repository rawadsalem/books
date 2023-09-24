import streamlit as st
import pandas as pd
import plotly.express as px
URL = "https://github.com/rawadsalem/books/blob/60a4e58a1b1c670a92057d01c8c6dc7e9a36c097/Books.csv"
# Load the data
file_path = URL
data = pd.read_csv(file_path)

# Create a Streamlit app
st.title("Interactive Book Visualization")

# Add a sidebar for interactive features
st.sidebar.header("Interactive Features")

# Interactive feature 1: Time Frame Selector
selected_year = st.sidebar.slider("Select a Year", min_value=data['Year'].min(), max_value=data['Year'].max())

# Interactive feature 2: Genre Selector
selected_genre = st.sidebar.selectbox("Select a Genre", data['Genre'].unique())

# Filter the data based on selected features
filtered_data = data[(data['Year'] == selected_year) & (data['Genre'] == selected_genre)]

# Create Plotly Express figures
fig1 = px.scatter(
    data_frame=filtered_data,
    x='User Rating',
    y='Price',
    size='Reviews',
    color='Genre',
    hover_name='Name',
    hover_data={'Author': True},
    title=f'Book Ratings, Prices, and Reviews in {selected_year} ({selected_genre})',
    color_discrete_map={'Fiction': 'blue', 'Non Fiction': 'green'}
)

fig1.update_layout(
    xaxis_title='User Rating',
    yaxis_title='Price',
    showlegend=True,
    xaxis_range=[3, 5],
    yaxis_range=[0, 25],
    xaxis_dtick=0.5,
    yaxis_dtick=5
)

fig2 = px.histogram(
    data_frame=filtered_data,
    x="Price",
    y="User Rating",
    color="Genre",
    title=f"Price vs. User Rating in {selected_year} ({selected_genre})",
    hover_data=["Name", "Author"],
    range_x=[0, 50],
    color_discrete_map={'Fiction': 'blue', 'Non Fiction': 'green'}
)

fig2.update_traces(opacity=0.7)

fig2.update_layout(
    xaxis_title="Price In USD",
    yaxis_title="User Rating On 5",
    bargap=0.1,
)

# Create a third visualization with an interactive feature
st.header("Additional Visualization")

# Interactive feature 3: Rating Distribution Selector for Figure 3
selected_distribution = st.selectbox("Select a Rating Distribution for Figure 3", ["User Rating", "Reviews"])

# Create a distribution plot based on the selected feature
if selected_distribution == "User Rating":
    fig3 = px.histogram(
        data_frame=filtered_data,
        x="User Rating",
        color="Genre",
        title=f"User Rating Distribution in {selected_year} ({selected_genre})",
        color_discrete_map={'Fiction': 'blue', 'Non Fiction': 'green'}
    )
    fig3.update_xaxes(title="User Rating")
else:
    fig3 = px.histogram(
        data_frame=filtered_data,
        x="Reviews",
        color="Genre",
        title=f"Review Count Distribution in {selected_year} ({selected_genre})",
        color_discrete_map={'Fiction': 'blue', 'Non Fiction': 'green'}
    )
    fig3.update_xaxes(title="Review Count")

# Display the selected visualizations
st.plotly_chart(fig1)
st.plotly_chart(fig2)

# Add the "Select a Rating Distribution" interaction at the top of Figure 3
st.subheader("Select a Rating Distribution")
st.plotly_chart(fig3)

# Optionally, you can add more text or explanations here
st.write("Explore book ratings, prices, and reviews over time with the interactive features on the sidebar.")

# Close the Streamlit app
st.write("Thank you for using the Book Visualization App!")
