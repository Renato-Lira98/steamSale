import requests

# Este código tem a função de coletar o conteúdo HTML bruto da URL fornecida e, ao final, salvar esses dados em um arquivo HTML.
response = requests.get(
    url='https://proxy.scrapeops.io/v1/',
    params={
        'api_key': '488c0bc2-f71b-44f9-83c0-7ea9ed9bc0d5',
        'url': 'https://steamdb.info/sales/', 
    },
)

# Salva a resposta em um arquivo HTML
with open("steam_sales.html", "wb") as file:
    file.write(response.content)
