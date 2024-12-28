from flask import Flask, request, send_file
import requests
from urllib.parse import urlparse

app = Flask(__name__)

def download(url):
    r = requests.get(url)
    filename = urlparse(url).path.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(r.content)
    return filename

@app.route('/download', methods=['POST'])
def _():
    url = request.form.get('url')
    return download(url)

@app.route('/fid.png', methods=['GET'])
def fid():
    return send_file('fid.png')

@app.route('/fana', methods=['GET'])
def fana():
    return send_file('flag.txt')

@app.route('/exploit', methods=['GET'])
def exploit():
    return send_file('flag.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
