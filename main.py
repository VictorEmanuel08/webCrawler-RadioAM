import scrapy
import json
class RadioAmBot(scrapy.Spider):
    name="Radio AM Bot"
    start_urls = ["https://imirante.com/miranteam", "https://imirante.com/miranteam/noticias"]
    
    def parse(self, response):
        if "noticias" in response.url:
            
            #JSON SIMPLES#
            # Extrai todos os elementos <h3> com a classe 'artigoListagem__titulo'
            array = response.css('h3.artigoListagem__titulo::text').extract()

            # Cria uma lista para armazenar os objetos JSON
            noticias = []

            # Adiciona cada título como um objeto JSON à lista
            for item in array:
                noticias.append({'noticia': item.strip()})

            # Salva a lista de objetos JSON em um arquivo JSON com codificação UTF-8
            with open('noticias.json', 'w', encoding='utf-8') as json_file:
                json.dump(noticias, json_file, ensure_ascii=False, indent=4)
            
            #JSON CONCATENADO POR | #
            # Extrai todos os elementos <h3> com a classe 'artigoListagem__titulo'
            noticias = response.css('h3.artigoListagem__titulo::text').extract()

            # Converte todos os títulos para letras maiúsculas
            noticias_uppercase = [titulo.upper() for titulo in noticias]

            # Cria uma string para armazenar os títulos separados por '|'
            noticias_concatenados = ' | '.join(noticias_uppercase)

            # Cria um dicionário com a chave 'noticias' e a string concatenada como valor
            dados_json = {'noticias': noticias_concatenados}

            # Salva os dados como um arquivo JSON
            with open('novo_noticias.json', 'w', encoding='utf-8') as json_file:
                json.dump(dados_json, json_file, ensure_ascii=False, indent=4)
        else:
            #TITULO DO PROGRAMA#
            # Extrai o elemento <p> com a classe 'programaNoAr__titulo'
            titulo_programa = response.css('p.programaNoAr__titulo::text').extract_first()

            # Cria um dicionário com o título do programa
            dados_json = {'titulo_programa': titulo_programa.strip().upper()}

            # Salva os dados como um arquivo JSON
            with open('titulo_programa.json', 'w', encoding='utf-8') as json_file:
                json.dump(dados_json, json_file, ensure_ascii=False, indent=4)

            #APRESENTADOR#
            # Extrai o elemento <p> com a classe 'programaNoAr__titulo'
            titulo_programa = response.css('p.programaNoAr__apresentador::text').extract_first()

            # Cria um dicionário com o título do programa
            dados_json = {'nome_apresentador': titulo_programa.strip().upper()}

            # Salva os dados como um arquivo JSON
            with open('nome_apresentador.json', 'w', encoding='utf-8') as json_file:
                json.dump(dados_json, json_file, ensure_ascii=False, indent=4)