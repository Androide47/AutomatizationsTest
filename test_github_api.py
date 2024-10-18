import requests
import json
import os

#github_token = os.environ.get('TOKEN')

CONFIG_PATH = 'config.json'

with open(CONFIG_PATH) as config:
    config = json.load(config)
    github_url = config['github_url']
    github_user = config['github_user']
    github_repo = config['github_repo']
    github_token = config['github_token']
    github_branch = config['github_branch']
    github_branches = config['github_branches']
    github_labels = config['github_labels']

url = "https://api.github.com/user/repos"
#url = f'{github_url}/repos/{github_user}/{github_repo}/branches'
headers = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Make a request to the GitHub API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    print(f"Repo Name: {github_repo}")
    print(f"Repo URL: {github_url}")
    print(f"Branches: {github_branches}")
    print(f"Labels: {github_labels}")
    print(f"Features")
    print(f"Automates branch-based actions with GitHub Actions")
else:
    print("Request failed with status code:", response.status_code)
    print(f"Error: {response.text}")