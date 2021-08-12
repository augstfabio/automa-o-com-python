from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time



driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver.get('https://www.coronatracker.com/pt-br')

#mundo
curados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]')
confirmados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
obitos = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]')

confirmadostxt = confirmados.text
curadostxt = curados.text
obitostxt = obitos.text

#grava os dados do corona no mundo

arquivo = open('casosdocorona.txt', "w", encoding='UTF-8')
arquivo.write('#CASOS DO CORONA NO MUNDO\n')
arquivo.write('Casos confirmados: ')
arquivo.write(confirmadostxt)
arquivo.write('\n')
arquivo.write('Casos curados:')
arquivo.write(curadostxt)
arquivo.write('\n')
arquivo.write('Casos com mortes: ')
arquivo.write(obitostxt)
arquivo.write('\n\n')
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

#grava os dados do corona no brasil

arquivo.write('#CASOS DO CORONA NO BRASIL')
arquivo.write('\n')
arquivo.write('confirmados:')
arquivo.write(br_confirmadostxt)
arquivo.write('\n')
arquivo.write('Curados: ')
arquivo.write(br_curadostxt)
arquivo.write('\n')
arquivo.write('Óbitos: ' )
arquivo.write(br_obitostxt)

arquivo.close()

print('dados do Brasil armazenados no arquivo com sucesso!')






