import pandas as pd
from playwright.sync_api import sync_playwright

#Parte do código responsavel por fazer o scrap dos filmes
url = "https://www.imdb.com/chart/top/"
url_base = "https://www.imdb.com"

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto(url)
    pagina.wait_for_timeout(3000)
    
    anos = []
    generos = []
    filmes = pagina.locator("li.ipc-metadata-list-summary-item")
    quantidade = filmes.count()
    for i in range(200):
        filme = filmes.nth(i)
        href = filme.locator("a.ipc-title-link-wrapper").get_attribute("href")
        ano = filme.locator("span.sc-15ac7568-7.cCsint.cli-title-metadata-item").first.text_content().strip()
        if ano:
            anos.append(ano)
            
        link = url_base + href
        
        informacoes = navegador.new_page()
        informacoes.goto(link)
        informacoes.wait_for_timeout(1000)
        genero = informacoes.locator("div.ipc-chip-list__scroller a").first.text_content().strip()
        if genero:
            generos.append(genero)
        
        informacoes.close()
    
    navegador.close()
    
#Parte do codigo responsavel por salvar os dados coletados
dados = pd.DataFrame({
    "ano": anos,
    "genero": generos
})

dados.to_csv("dados_filmes250.csv", index=False, encoding="utf-8")