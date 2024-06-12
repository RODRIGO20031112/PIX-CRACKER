from flask import Flask, request, jsonify
from bs4 import BeautifulSoup as BSHTML
import urllib.request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        page = urllib.request.urlopen(url)
        soup = BSHTML(page, features="lxml")

        image = soup.find('img', alt='pix_qrcode')
        image_src = image['src'] if image else None

        qrCode_input = soup.find('input', id='qrCode')
        qrCode_value = qrCode_input.get('value') if qrCode_input else None

        result = {
            'imagem_src': image_src,
            'qrCode_value': qrCode_value
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
