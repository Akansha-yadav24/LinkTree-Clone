# link_tree_clone.py
import streamlit as st
from PIL import Image
from st_functions import load_css, st_button

load_css()

# Display Photo
col1, col2, col3 = st.columns(3)
# Open the image
image = Image.open("profile-pic.png")

# Add image to col2 with a specified width
col2.image(image, width=180)


# User name and small description
st.title("Hey!👋 "+ " I'm Akansha Yadav")

st.write("Empowering 600+ Students in Data Science & Coding (Python) | IBM Skills Instructor & Content Creator")

icon_size = 20

# Creating buttons for social media links
st_button(
    "portfolio",
    "https://www.notion.so/Akansha-Yadav-f33faf191c114cd6a68a00c7246fe315?pvs=4",
    "See My Work: Portfolio",
    icon_size,
)
st_button(
    "github",
    "https://github.com/Akansha-yadav24",
    "Checkout My Projects: GitHub Repositories",
    icon_size,
)
st_button(
    "instagam",
    "https://www.instagram.com/codingdidi/",
    "Explore My community jouney: Instagram",
    icon_size,
)
st_button(
    "linkedin",
    "https://www.linkedin.com/in/akansha-yadav24/",
    "Let's Connect: LinkedIn",
    icon_size,
)
