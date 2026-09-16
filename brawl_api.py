from flask import Flask, jsonify, request, abort, send_from_directory
import requests
import urllib.parse
import os

# Try to import API_KEY from BrawlStarsStats.py
API_KEY = None
try:
    from BrawlStarsStats import API_KEY as _API_KEY
    API_KEY = _API_KEY
except Exception:
    # Allow setting via ENV
    API_KEY = os.environ.get('BRAWL_API_KEY')

if not API_KEY:
    raise SystemExit('Brawl API key not found. Set API_KEY in BrawlStarsStats.py or BRAWL_API_KEY env var')

BASE_URL = 'https://api.brawlstars.com/v1'
HEADERS = { 'Authorization': f'Bearer {API_KEY}' }

app = Flask(__name__, static_folder='.', static_url_path='')


@app.after_request
def add_cors_headers(response):
    # Allow local frontend served from file:// or other origins to call API during development
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


@app.route('/')
def serve_ui():
    # serve the local brawl.html file so users can open http://localhost:5000/
    return send_from_directory('.', 'brawl.html')

@app.route('/api/player/<path:tag>')
def player(tag):
    # Accept tags with or without leading '#'. Normalize to include '#'
    tag = urllib.parse.unquote(tag)
    if not tag.startswith('#'):
        tag = '#' + tag
    encoded = tag.replace('#', '%23')
    url = f"{BASE_URL}/players/{encoded}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return jsonify(r.json())
    return abort(r.status_code, r.text)

@app.route('/api/brawlers/<path:tag>')
def brawlers(tag):
    tag = urllib.parse.unquote(tag)
    if not tag.startswith('#'):
        tag = '#' + tag
    encoded = tag.replace('#', '%23')
    url = f"{BASE_URL}/players/{encoded}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return jsonify(r.json())
    return abort(r.status_code, r.text)

@app.route('/api/leaderboard/<region>')
def leaderboard(region):
    # region: global or country code
    url = f"{BASE_URL}/rankings/{region}/players"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return jsonify(r.json())
    return abort(r.status_code, r.text)


@app.route('/api/battlelog/<path:tag>')
def battlelog(tag):
    tag = urllib.parse.unquote(tag)
    if not tag.startswith('#'):
        tag = '#' + tag
    encoded = tag.replace('#', '%23')
    url = f"{BASE_URL}/players/{encoded}/battlelog"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return jsonify(r.json())
    return abort(r.status_code, r.text)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port, debug=True)
