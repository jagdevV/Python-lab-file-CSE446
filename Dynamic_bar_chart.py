#Dynamic bar chart
import plotly.express as px

# Sample Data
categories = ['Python', 'Java', 'C++', 'JavaScript']
values = [85, 70, 60, 75]

# Create Bar Chart
fig = px.bar(
    x=categories,
    y=values,
    title="Programming Language Popularity",
    text=values,
    color=values,
    color_continuous_scale="Blues"
)

# Improve Layout
fig.update_layout(
    title_font_size=20,
    xaxis_title="Programming Language",
    yaxis_title="Popularity Score",
    template="plotly_white"
)

fig.update_traces(textposition='outside')

fig.show()