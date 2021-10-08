from selenium import webdriver
import smtplib
import email.message
import time
from selenium.webdriver.chrome.options import Options
import PySimpleGUI as sg

#Criado por Fabio Augusto

class Tracker():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe',options=chrome_options)
        print('entrando no site...')
        self.driver.get('https://www.coronatracker.com/pt-br')
        self.email_message = email.message.Message()
        time.sleep(3)
        print('feito')

    def varrer(self):
        #varre dados do mundo
        print('iniciando varredura de dados mundial...')
        curados = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]')
        print('curados ok')
        confirmados = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
        print('confirmados ok')
        obitos = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]')
        print('obitos ok')
        print('convertendo para texto')
        self.confirmados = confirmados.text
        print('confirmados ok')
        self.curados = curados.text
        print('curados ok')
        self.obitos = obitos.text
        print('obitos ok')
        print('feito')
        #varre dados do Brasil
        print('alterando fonte de dados para o BR...')
        self.driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[1]/button').click()
        self.driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[1]/ul/li[4]/a').click()
        time.sleep(3)
        print('feito')
        print('iniciando varredura de dados do Brasil ')
        br_confirmados = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
        print('confirmados ok')
        br_curados = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]')
        print('curados ok')
        br_obitos = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]')
        print('obitos ok')
        print('feito')
        print('convertendo para texto')
        self.br_confirmados = br_confirmados.text
        print('confirmados ok')
        self.br_curados = br_curados.text
        print('curados ok')
        self.br_obitos = br_obitos.text
        print('obitos ok')
        print('dados varridos com sucesso!')
        time.sleep(2)

    def enviar_email(self, email,senha,destino):
        self.email = email
        self.senha = senha
        self.destino = destino
        print('definindo corpo do email..')
        corpo_email = f"""
        <p><font size=+2>CORONA VIRUS STATUS</font></p>
        <p></p>
        <p><b><font size=+1>Corona virus no mundo</font></b></p>
        <p></p>
        <p><font face="arial"><font color="#DAA520">confirmados:</font></font> {self.confirmados}</p>
        <p><font face="arial"><font color="#00FF00">curados:</font></font>{self.curados}</p>
        <p><font face="arial"><font color="#DC143C">mortos:</font></font> {self.obitos}</p>
        <p></p>
        <p></p>
        <p></p>
        <p><b><font size=+1>Corona no Brasil</font></b></p>
        <p></p>
        <p><font face="arial"><font color="#DAA520">confirmados:</font></font>{self.br_confirmados}</p>
        <p><font face="arial"><font color="green">curados:</font></font> {self.br_curados}</p>
        <p><font face="arial"><color="#DC143C">mortos:</font></font>{self.br_obitos}</p>
        <p></p>
        <p></p>
        <p>Dados retirados instantaneamente do site CoronaTrack disponivel em https://www.coronatracker.com/pt-br</p>
        """
        print('feito')
        print('enviando email')
        msg = self.email_message
        msg['Subject'] = "Dados do Corona"
        msg['From'] = self.email
        msg['To'] = self.destino
        password = self.senha 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado com sucesso para {self.destino}')
        time.sleep(2)
    
    def gravar_txt(self):
        #grava os dados do corona no mundo:
        print('criando arquivo')
        arquivo = open('casosdocorona.txt', "w", encoding='UTF-8')
        print('gravando dados do mundo...')
        arquivo.write('#CASOS DO CORONA NO MUNDO\n')
        arquivo.write('Casos confirmados: ')
        arquivo.write(self.confirmados)
        arquivo.write('\n')
        arquivo.write('Casos curados:')
        arquivo.write(self.curados)      
        arquivo.write('\n')
        arquivo.write('Casos com mortes: ')
        arquivo.write(self.obitos)
        arquivo.write('\n\n')
        print('feito!')
        
        #grava os dados do corona no Brasil
        print('gravando dados do Brasil...')
        arquivo.write('#CASOS DO CORONA NO BRASIL')
        arquivo.write('\n')
        arquivo.write('confirmados:')
        arquivo.write(self.br_confirmados)
        arquivo.write('\n')
        arquivo.write('Curados: ')
        arquivo.write(self.br_curados)
        arquivo.write('\n')
        arquivo.write('Óbitos: ' )
        arquivo.write(self.br_obitos)
        print('feito')
        arquivo.close()
        print('arquivo gravado com sucesso!')

     
class Tela():
    def __init__(self):
        layout = [
            [sg.Text('varredura do site Coronatrack')],
            [sg.Text('digite o email de destino'),sg.Input(key='destino')],
            [sg.Text('digite o seu email'),sg.Input(key='remetente')],
            [sg.Text('digite sua senha'),sg.Input(key='senha')],
            [sg.Checkbox('Enviar Email',key='enviar'), sg.Checkbox('Gravar em um arquivo de texto', key='gravar')],
            [sg.Button('iniciar varredura')],
            [sg.Output(size=(30,30))]
        ]   
        self.janela = sg.Window('Dados do Corona').layout(layout)
        


    def ir(self):
        while True:
            self.button, self.values = self.janela.Read()
            self.destino = self.values['destino']
            self.remetente = self.values['remetente']
            self.senha = self.values['senha']
            self.enviar = self.values['enviar']
            self.gravar = self.values['gravar']
            self.corona = Tracker()
            self.corona.varrer()
            if self.enviar == True:
                self.corona.enviar_email(self.remetente,self.senha,self.destino)
            else:
                pass
            if self.gravar == True:
                self.corona.gravar_txt()
            else: pass


def main():
    teste = Tela()
    teste.ir()


if __name__=='__main__':
    main()