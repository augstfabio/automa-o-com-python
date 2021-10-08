from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Se quiser mostrar o navegador     | opc.headless = False
# Se não quiser mostrar o navegador | opc.headless = True

opc = Options()
opc.headless = True
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=opc)

driver.get('https://www.coronatracker.com/pt-br')

time.sleep(3)

#mundo

curados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]')
confirmados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
obitos = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]')

confirmadostxt = confirmados.text
curadostxt = curados.text
obitostxt = obitos.text

print('dados do corona no mundo foram armazenados com sucesso!')

#BR

br = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[1]/button').click()
br1 = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[1]/ul/li[4]/a').click()
time.sleep(3)

br_confirmados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
br_curados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]')
br_obitos = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]')

br_confirmadostxt = br_confirmados.text
br_curadostxt = br_curados.text
br_obitostxt = br_obitos.text

arquivo = open('casosdocorona.txt', "w", encoding='UTF-8')

arquivo.write(f'''\
#CASOS DO CORONA NO MUNDO
Casos confirmados: {confirmadostxt}
Casos curados: {curadostxt}
Casos com mortes: {obitostxt}

#CASOS DO CORONA NO BRASIL
Casos confirmados: {br_confirmadostxt}
Casos curados: {br_curadostxt}
Casos com mortes: {br_obitostxt}
''')

arquivo.close()
driver.close()

print('dados do Brasil armazenados no arquivo com sucesso!')






