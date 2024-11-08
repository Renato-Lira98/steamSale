import pandas as pd
from bs4 import BeautifulSoup

# Carrega o arquivo HTML
with open("steam_sales.html", "r", encoding="utf-8") as file:
    content = file.read()

# Analisa o HTML com BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Localiza a tabela que contém as informações dos jogos
table = soup.find("table", {"class": "table-sales"})

# Lista para armazenar os dados dos jogos
games_data = []

for row in table.tbody.find_all("tr", {"class": "app"}):
    game_data = {
        "id": row["data-appid"],  # ID do jogo
        "name": row.select_one("td:nth-of-type(3) a").text.strip(),  # Nome do jogo
        "discount": row.select_one("td:nth-of-type(4)").text.strip(),  # Desconto
        "price": row.select_one("td:nth-of-type(5)").text.strip(),  # Preço
        "rating": row.select_one("td:nth-of-type(6)").text.strip(),  # Avaliação
        "release": row.select_one("td:nth-of-type(7)").text.strip(),  # Lançamento
        "ends": row.select_one("td:nth-of-type(8)").get("data-sort"),  # Fim da promoção
        "start": row.select_one("td:nth-of-type(9)").get("data-sort")  # Início da promoção
    }
    games_data.append(game_data)

# Salva os dados extraídos em um arquivo de texto para depuração de erros.
with open("games_data.txt", "w", encoding="utf-8") as file:
    for game in games_data:
        file.write(str(game) + "\n")
      
# Criar um DataFrame
df = pd.DataFrame(games_data)

df.to_csv('steam_sales_data.csv', index=False)
