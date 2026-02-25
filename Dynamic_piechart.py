#Dynamic piechart
import plotly.express as px

# Sample Data
labels = ['Python', 'Java', 'C++', 'JavaScript']
values = [35, 25, 20, 20]

# Create Pie Chart
fig = px.pie(
    names=labels,
    values=values,
    title="Programming Language Usage",
    hole=0.3  # Makes it donut style (dynamic look)
)

# Improve Layout
fig.update_traces(
    textinfo='percent+label',
    pull=[0.05, 0, 0, 0]  # Slightly explode first slice
)

fig.update_layout(
    title_font_size=20
)

fig.show()