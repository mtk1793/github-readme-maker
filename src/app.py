import streamlit as st
import os


def load_template(theme):
    theme_path = os.path.join("themes", f"{theme}.md")
    try:
        with open(theme_path, "r") as file:
            template = file.read()
        return template
    except FileNotFoundError:
        st.error(f"Theme file '{theme}.md' not found in 'themes' directory.")
        return None


st.title(":zap: Github Profile Beautifier")

# Getting the personal information
st.header("Personal Information Form")

with st.expander("Personal Information"):
    st.write("Please provide your personal details")
    col1, col2 = st.columns(2)
    name = col1.text_input("Name *", placeholder="Required")
    email = col1.text_input("Email *", placeholder="Required")
    phone = col2.text_input("Phone Number")
    gender = col2.selectbox("Gender", ["Male", "Female", "Other"])
    location = st.text_input("Location")
    aboutme = st.text_input("About Me")

# Social Media
st.header("Social Media")
with st.expander("Social Media"):
    st.markdown("Enter only your social media usernames, not any link:")
    st.write("Please provide your social media details")
    col1, col2 = st.columns(2)
    github_username = col1.text_input("GitHub Username *", placeholder="Required")
    twitter_username = col1.text_input("Twitter Username")
    linkedin_username = col2.text_input("LinkedIn Username")
    outlook_username = col2.text_input("Outlook Username")

# Select Themes
st.header("Select Theme")
theme = st.selectbox("Theme", ["default", "dark", "light"])

# Generate Readme
st.header("Generate Readme")
if st.button("Generate Readme"):
    if not name or not email or not github_username:
        st.error("Please fill out all required fields marked with *.")
    else:
        template = load_template(theme)
        if template:
            readme_content = template.format(
                name = name,
                email = email,
                phone = phone,
                gender = gender,
                location = location,
                aboutme = aboutme,
                github_username=github_username,
                linkedin_username=linkedin_username,
                outlook_username=outlook_username,
            )
            st.code(readme_content, language="markdown")
