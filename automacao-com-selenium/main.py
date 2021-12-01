from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium import webdriver

# Cria um Service para gerenciar o WebDriver (aquele baixado anteriormente)
service = Service('./driver/chromedriver')
options = webdriver.ChromeOptions()

# DESCOMENTE A LINHA ABAIXO caso queira habilitar o "modo silencioso"
# options.headless = True

driver = webdriver.Chrome(service=service, options=options)

# Navega para o site Canaltech e expande a tela
driver.get('https://canaltech.com.br/')
driver.set_window_size(width=1900, height=1080)

# Navega pela página buscando o banner das Principais Notícias
secao_noticias = driver.find_element(By.XPATH, '/html/body/main/section[1]')
noticias = secao_noticias.find_elements(By.CLASS_NAME, 'feature-item')

# Pega a lista de Links através dos atributos "href" das tags <a href="">
links = [n.get_attribute('href') for n in noticias]

try:
    # Itera sobre os links, navegando para a página da notícia a cada elemento
    for link in links:
        driver.get(link)

        secoes = driver.find_elements(By.TAG_NAME, 'section')
        titulo = secoes[0].find_element(By.TAG_NAME, 'h1').text
        descricao = secoes[1].find_elements(By.TAG_NAME, 'p')[1].text

        print(f'\n\nTÍTULO: {titulo}\nDESCRIÇÃO:\n\t{descricao}\n\tLINK: {link}')
except ElementNotInteractableException:
    pass



