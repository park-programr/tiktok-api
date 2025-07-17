from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/tiktok', methods=['GET'])
def tiktok():
    url = request.args.get('url')
    r = requests.get(f'https://tikwm.com/api/?url={url}')
    if r.status_code == 200:
        d = r.json()
        return jsonify({
            'video': d['data']['play'],
            'music': d['data']['music']
        })
    return jsonify({'error': 'فشل الاتصال'}), 400

if __name__ == '__main__':
    app.run()