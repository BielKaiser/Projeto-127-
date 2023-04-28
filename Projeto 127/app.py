from bs4 import BeautifulSoup
import time 
import pandas as pd
from selenium import webdriver

siteestrela = ("https://pt.wikipedia.org/wiki/Lista_das_estrelas_mais_brilhantes")
drive = webdriver.Chrome("C:/Users/joaob/OneDrive/Área de Trabalho/Visual studio folders/Inspecionar/chromedriver.exe")
drive.get(siteestrela)
time.sleep(5)
info = []

def informacao():
    while True:
        infoht = BeautifulSoup(drive.page_source,"html.parser")
        brilhante = infoht.find("table", attrs ={"class", "wikitable"})
        tablebody = brilhante.find("tbody")
        Tr = tablebody.find("tr")

        for i in Tr:
            colunas = i.find_all("td")
            print(colunas)
            temp_list = []

            for dataCol in colunas:
                print(dataCol.text)
                data = dataCol.text.strip()
                print(data)

                temp_list.append(data)
        
        info.append(temp_list)

dataestrela = []


for i in range(0,len(info)):
    
    nomeestrela = info[info][1]
    distancia = info[i][3]
    massa = info[i][5]
    raio = info[i][6]
    luminosidade = info[i][7]

    datarequirida = [nomeestrela, distancia, massa, raio, luminosidade]
    dataestrela.append(datarequirida)

cabecalho = ['nomeestrela', 'distancia', 'massa', 'raio', 'luminosidade'] 
dataframeestrela = pd.DataFrame(dataestrela,columns = cabecalho)

dataframeestrela.to_csv('info.csv',index = True,index_label ="id")

