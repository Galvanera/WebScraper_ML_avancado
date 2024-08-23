Web Scraper de Produtos do Mercado Livre
Este repositório contém um script Python que utiliza Selenium e BeautifulSoup para fazer scraping de produtos do site Mercado Livre. O script acessa a página, extrai os dados desejados e os exibe no console.

Funcionalidades
Acesso Automático à Página: Utiliza Selenium para abrir a página do Mercado Livre e buscar produtos.
Extração de Dados: Coleta os nomes, preços e links dos produtos listados na página.
Navegação Automática: Percorre as páginas de resultados automaticamente.
Exibição dos Dados: Imprime os dados dos produtos no console.
Configuração Flexível: Pode ser executado em modo headless (sem interface gráfica) para maior eficiência.
Como Usar
Instale as bibliotecas necessárias:
pip install selenium beautifulsoup4 pandas

Baixe o WebDriver do Chrome:
Faça o download do ChromeDriver compatível com a versão do seu navegador Chrome.
Adicione o caminho do ChromeDriver ao seu PATH do sistema ou coloque o executável na mesma pasta do script.
Clone este repositório:
git clone https://github.com/seu-usuario/webscraper_ml_avancado.git
cd webscraper_ml_avancado

Execute o script:
python Raspagem_paginas.py
