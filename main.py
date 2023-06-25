from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/forks', methods=['GET'])
def get_forks():
    user_name = request.args.get('user')
    repo_name = request.args.get('repo')
    if not user_name:
        return jsonify({'error': 'Please provide a username.'}), 400
    if not repo_name:
        return jsonify({'error': 'Please provide a repository name.'}), 400
    
    api_url = f'https://api.github.com/repos/{user_name}/{repo_name}'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(api_url, headers=headers)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch repository information.'}), 500
    
    repo_info = response.json()
    
    return jsonify(repo_info)
