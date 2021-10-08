from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep 

def buscar_result():

    sleep(3)

    Confirmados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]').text
    Curados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]').text
    Obitos = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]').text

    arquivo.write(f'\nCasos confirmados: {Confirmados}\nCasos curados: {Curados}\nCasos com mortes: {Obitos}\n\n')

opc = Options()
opc.headless = True # Mostrar navegador > opc.headless = False | Não mostrar navegador > opc.headless = True

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=opc)
driver.get('https://www.coronatracker.com/pt-br')

arquivo = open('casosdocorona.txt', "w", encoding='UTF-8') # Criando arquivo .txt

arquivo.write('#CASOS DO CORONA NO MUNDO\n')
buscar_result()

driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[1]/button').click()
driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[1]/ul/li[4]/a').click()

arquivo.write('#CASOS DO CORONA NO BRASIL\n') 
buscar_result()

driver.close()
