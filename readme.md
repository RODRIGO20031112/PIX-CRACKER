# Bem vindos ao PIX CRACKER 💸

## Implantação 🧩

### Apenas clone este repositório e repita o processo abaixo

No diretório raiz 🌱  

```bash
pip install -r requirements.txt
```

## Isenção de responsabilidade ⚠️

Todos os bancos existentes tem como premissa serem transparentes em relação a como utilizam os dados dos clientes, alguns mais vulneráveis que outros, quando você utiliza dessas vulnerabilidades para explorar vantagens em pessoas você está cometendo um crime, seja responsável e utilize esse software simples apenas em casos em que ele realmente pode ser útil e legal.

Conforme mencionado no título não me responsabilizo por quaisquer atitude imprópria sobre o uso indevido da ferramenta, encare ela como campos de estudo e pesquisa para desenvolvimento financeiro.

## Como funciona ? ⚙️

### Na raiz do projeto inicie o app

```bash
python main.py
```

### Apenas dispare uma requisição para a rota iniciada

```bash
curl -X GET "http://localhost:5000/scrape?url=https://checkout.perfectpay.com.br/payments/confirm/PPCPMTB5ENH5DI?ref=PPA1VC6I&ref=PPA1VC6I&urlCampaignCode=PPU38COLMCB"
```

### Você pode usar o Insominia 🔮

### Respostas da requisição 🌐

```json
{
"imagem_src": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQ...",
"qrCode_value": "00020126860014br.gov.bcb.pix2564pix-qrcode.sic..."
}
```

- **imagem_src:** QrCODE gerado pra cobrança Pix 🖼️
- **qrCode_value:** Pix copia e cola 🩹

### Repare nos parêmtros de URL

- **URL:** https://checkout.perfectpay.com.br/payments/confirm/PPCPMTB5ENH5DI?ref=PPA1VC6I&ref=PPA1VC6I&urlCampaignCode=PPU38COLMCB

### Essa é a URL onde o pix é gerado, você pode fazer uma no site da Perfect Pay ⬜

Conheça a <a href="https://app.perfectpay.com.br/refer/REFPPU15CH11K6">Perfect Pay</a>

## Considerações finais 🚩

O Pix Cracker apenas mascára o recebedor, isso pode ser útil pra muitas coisas, tendo em vista que não é necessário ter uma conta CNPJ ou CPF vinculada diretamente ao recebedor, porque quem no caso recebe é a Perfect Pay

Fique atento as taxas, isso tudo infelizmente ou felizmente só funciona porque de certa forma elas existem, por sua vez é o que garante a discrição dos dados da transação do PIX