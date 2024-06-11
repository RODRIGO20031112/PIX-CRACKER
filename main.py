from flask import Flask, jsonify
from bs4 import BeautifulSoup as BSHTML
import urllib.request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/scrape')
def scrape():
    page = urllib.request.urlopen('https://checkout.perfectpay.com.br/payments/confirm/PPCPMTB5EN91EH?ref=PPA1VA63&urlCampaignCode=PPU38COLE43')
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

if __name__ == '__main__':
    app.run(debug=True)
