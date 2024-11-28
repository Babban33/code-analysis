import requests
from urllib.parse import urlparse
import streamlit as st

def extract_repo_info(repo_url):
    try:
        parsed_url = urlparse(repo_url)
        path_parts = parsed_url.path.strip('/').split('/')
        
        if len(path_parts) >= 2:
            return path_parts[0], path_parts[1]
        else:
            st.error("Invalid GitHub repository URL format.")
            return None, None
    except Exception as e:
        st.error(f"Error parsing the URL: {e}")
        return None, None

def fetch_contributors(repo_owner, repo_name, token=None):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contributors"
    headers = {'Authorization': f'token {token}'} if token else {}
    params = {'per_page': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching contributors: {e}")
        return []

def display_contributions(contributors):
    """Generate contribution stats for each contributor."""
    if not contributors:
        st.info("No contributors found.")
        return
    
    total_commits = sum(contributor['contributions'] for contributor in contributors)
    st.write(f"### Total commits: {total_commits}")
    
    contribution_data = []
    for contributor in contributors:
        login = contributor['login']
        commits = contributor['contributions']
        percentage = (commits / total_commits) * 100
        contribution_data.append((login, commits, percentage))
    
    for login, commits, percentage in sorted(contribution_data, key=lambda x: x[1], reverse=True):
        st.write(f"- **{login}**: {commits} commits ({percentage:.2f}%)")