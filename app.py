import streamlit as st
from api import extract_repo_info, fetch_contributors, display_contributions

st.title("Code Analysis")
st.write("Enter the GitHub repository link below to analyze the contributors and their commits.")

repo_url = st.text_input("GitHub Repository URL", "")
token = st.text_input("GitHub Token (Optional)", type="password")

if st.button("Analyze"):
    if repo_url:
        repo_owner, repo_name = extract_repo_info(repo_url)
        if repo_owner and repo_name:
            st.write(f"### Analyzing Repository: {repo_owner}/{repo_name}")
            contributors = fetch_contributors(repo_owner, repo_name, token)
            display_contributions(contributors)
    else:
        st.error("Please enter a valid GitHub repository URL.")