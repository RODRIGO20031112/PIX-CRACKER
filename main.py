from bs4 import BeautifulSoup as BSHTML
import urllib.request

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

print(result)
# Build Command pip install -r requirements.txt
# PYTHON_VERSION 3.10.2