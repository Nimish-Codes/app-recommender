import streamlit as st
import pandas as pd

# Sample CSV data
csv_data = ('App_list.csv')

# Create DataFrame from CSV data
df = pd.read_csv(pd.compat.StringIO(csv_data))

def get_related_apps(selected_apps, data):
    selected_categories = data[data['App Name'].isin(selected_apps)]['Category'].tolist()
    related_apps = data[data['Category'].isin(selected_categories) & ~data['App Name'].isin(selected_apps)]
    return related_apps

# Streamlit app
st.title("App Category Explorer")

# Dropdown to select apps
selected_apps = st.multiselect("Select Apps:", df['App Name'].unique())

# Display selected apps
if selected_apps:
    st.write("Selected Apps:", selected_apps)

    # Get related apps based on selected categories
    related_apps = get_related_apps(selected_apps, df)

    # Display related apps
    if not related_apps.empty:
        st.write("Related Apps:")
        st.table(related_apps)
    else:
        st.write("No related apps found.")
