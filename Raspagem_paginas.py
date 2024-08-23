from selenium import webdriver
from time import sleep
import scrapy
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


Options = Options()
Options.add_argument('window-size=400,800')
# Options.add_argument('--headless')
produto1 = input('Qual produto deseja?: ')
navegador = webdriver.Chrome(options=Options)

url = navegador.get('https://www.mercadolivre.com.br/')
sleep(0.3)
ok = navegador.find_element(By.TAG_NAME, 'input')
ok.click()
sleep(0.2)
ok.send_keys(produto1)
ok.submit()
sleep(2)

lista_produtos = []
page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

pag = site.find('li', attrs={
                'class': 'andes-pagination__button andes-pagination__button--next'})
while pag:
    next = pag.find('a', attrs={'class': 'andes-pagination__link'})

    produtos = site.findAll('li', attrs={'class': 'ui-search-layout__item'})
    for produto in produtos:
        Nome = produto.find('a', attrs={
                            'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
        Preco = produto.find('span', attrs={
            'class': 'andes-money-amount__fraction'})
        Link = produto.find('a', attrs={
                            'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
        lista_produtos.append(
            [Nome['title'], Preco.text, Link['href']])
    # print('produto:', titulo.text)
    # print('link do produto:', link['href'])
    link_pag = (next['href'])
    url = navegador.get(link_pag)
    page_content = navegador.page_source
    site = BeautifulSoup(page_content, 'html.parser')
    pag = site.find('li', attrs={
                    'class': 'andes-pagination__button andes-pagination__button--next'})

produtos = site.findAll('li', attrs={'class': 'ui-search-layout__item'})
for produto in produtos:
    Nome = produto.find('a', attrs={
        'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
    Preco = produto.find('span', attrs={
        'class': 'andes-money-amount__fraction'})
    Link = produto.find('a', attrs={
        'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
    lista_produtos.append(
        [Nome['title'], Preco.text, Link['href']])

news = pd.DataFrame(lista_produtos, columns=[
                    'Título', 'Preço', 'Link'])
news.to_excel(produto1+' '+'Produto.xlsx', index=False)
print('Tabela criada com sucesso!')
# site = BeautifulSoup(navegador.page_source,'html.parser')
# print(site.prettify())

while True:
    time.sleep(1000)
