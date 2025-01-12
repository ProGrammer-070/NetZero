import os

# Define the parent directory by going one level up
parent_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))
folder_path = os.path.join(parent_directory, "data")
file_path = os.path.join(folder_path, "__init__.py")

# Check if the 'data' directory exists in the parent directory
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Directory '{folder_path}' created.")

# Check if the '__init__.py' file exists in the 'data' directory
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("")
    print(f"File '{file_path}' created.")
else:
    print(f"File '{file_path}' already exists.")

import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="NetZero - Carbon Footprint Tracker",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.logo("Images/menu.png")

pages = {
    "App Navigations": [
        st.Page("home.py", title="Home", icon='🏠' ,default=True),
    ],
    "Modules": [
        st.Page("user_input.py", title="Calculate My Carbon Footprint", icon='🐾'),
        st.Page("recommendations.py", title="Recommendations",  icon='🤹‍♂️'),
        st.Page("Global_Climate.py", title="Global Carbon Emission",  icon='🏭'),
        st.Page("sustainability.py", title="Sustainable Practices",  icon='🌱')
    ]
}

pg = st.navigation(pages)
pg.run()
