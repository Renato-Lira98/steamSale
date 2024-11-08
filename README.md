# Projeto de Extração de Dados - SteamDB Sales

Este projeto realiza a extração de informações da base de dados disponível no site [SteamDB Sales](https://steamdb.info/sales/), armazena os dados no Google BigQuery e, em seguida, os dados são disponibilizados no Google Sheets.

## Objetivos

- Realizar web scraping para coletar informações da página de vendas do SteamDB.
- Armazenar os dados extraídos em uma tabela no Google BigQuery.
- Exportar ou conectar os dados do BigQuery a um Google Sheets para análise e visualização.

## Tecnologias Utilizadas

- **Python**: Para o desenvolvimento do processo de extração e manipulação dos dados.
- **Proxies**: Para o web scraping dos dados do site.
- **Google Cloud BigQuery**: Para armazenar os dados extraídos.
- **Google Sheets API**: Para exportar ou conectar os dados no Google Sheets.
- **BeautifulSoup**: Para o web scraping dos dados do site.
- **Pandas**: Para manipulação de dados antes do upload para o BigQuery.

## Como Executar o Projeto

1. Instalar as bibliotecas necessárias:

```bash
pip install pandas beautifulsoup4 requests
```

2. Como executar o projeto:
   
- Este projeto consiste em dois scripts principais: steamdbProxy.py e dataCollector.py. O fluxo de execução deve seguir a ordem descrita abaixo:
- Coleta de Dados Brutos: Execute o script steamdbProxy.py para coletar o HTML bruto do site. O arquivo resultante será salvo como um arquivo .html.
- Extração e Processamento de Dados: Após a coleta do HTML, execute o script dataCollector.py. Este script irá ler o arquivo .html, extrair as informações relevantes e salvar os dados em um arquivo .csv para posterior análise.
