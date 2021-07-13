import requests
from bs4 import BeautifulSoup

# Necessário para correto funcionamento do script
headers = {'User-Agent': 'Mozilla/5.0'}

# Busca o código HTML da página que quer analisar
pagina = requests.get('https://fundamentus.com.br/fii_resultado.php', headers=headers)

# Instancie o BeautifulSoul, passando o HTML no construtor e o parser
soup = BeautifulSoup(pagina.text, 'html.parser')

# Ache o dado que quer na página (passo 2)
dados = soup.find("table", {"id": "tabelaResultado"}).find('tbody').find_all('tr')

# Agora é com você! ;)
for fundo in dados:
    dados_fundo = fundo.find_all("td")
    print(
        f"[{dados_fundo[0].text}]\n"
        f"\tCotação: {dados_fundo[2].text}\n"
        f"\tSetor: {dados_fundo[1].text}\n"
        f"\tDY %: {dados_fundo[4].text}\n"
        f"\tP/VP: {dados_fundo[5].text}\n"
    )
