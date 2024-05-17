import scrapy
import json
import os

class RadioAmBot(scrapy.Spider):
    name = "Radio AM Bot"
    start_urls = ["https://imirante.com/miranteam", "https://imirante.com/miranteam/noticias"]
    
    def parse(self, response):
        # Definindo os caminhos de salvamento
        save_path_remote = r"\\viena02\Public\Victor\VMIX - Radio AM"
        save_path_local = os.getcwd()  # Pasta local onde o script está sendo executado
        
        if "noticias" in response.url:
            # Extrai todos os elementos <h3> com a classe 'artigoListagem__titulo'
            array = response.css('h3.artigoListagem__titulo::text').extract()
            
            # Cria uma lista para armazenar os objetos JSON
            noticias = []

            # Adiciona cada título como um objeto JSON à lista
            for item in array:
                noticias.append({'noticia': item.strip()})

            # Salvando noticias.json
            for path in [save_path_remote, save_path_local]:
                noticias_path = os.path.join(path, 'noticias.json')
                with open(noticias_path, 'w', encoding='utf-8') as json_file:
                    json.dump(noticias, json_file, ensure_ascii=False, indent=4)
            
            # Converte todos os títulos para letras maiúsculas
            noticias_uppercase = [titulo['noticia'].upper() for titulo in noticias]

            # Cria uma string para armazenar os títulos separados por '|'
            noticias_concatenados = ' | '.join(noticias_uppercase)

            # Cria um dicionário com a chave 'noticias' e a string concatenada como valor
            dados_json = {'noticias': noticias_concatenados}

            # Salvando novo_noticias.json
            for path in [save_path_remote, save_path_local]:
                novo_noticias_path = os.path.join(path, 'novo_noticias.json')
                with open(novo_noticias_path, 'w', encoding='utf-8') as json_file:
                    json.dump([dados_json], json_file, ensure_ascii=False, indent=4)
        else:
            # Extrai o elemento <p> com a classe 'programaNoAr__titulo'
            titulo_programa = response.css('p.programaNoAr__titulo::text').extract_first()
            if titulo_programa:
                # Cria um dicionário com o título do programa
                dados_json = {'titulo_programa': titulo_programa.strip().upper()}

                # Salvando titulo_programa.json
                for path in [save_path_remote, save_path_local]:
                    titulo_programa_path = os.path.join(path, 'titulo_programa.json')
                    with open(titulo_programa_path, 'w', encoding='utf-8') as json_file:
                        json.dump([dados_json], json_file, ensure_ascii=False, indent=4)

            # Extrai o elemento <p> com a classe 'programaNoAr__apresentador'
            nome_apresentador = response.css('p.programaNoAr__apresentador::text').extract_first()
            if nome_apresentador:
                # Cria um dicionário com o nome do apresentador
                dados_json = {'nome_apresentador': nome_apresentador.strip().upper()}

                # Salvando nome_apresentador.json
                for path in [save_path_remote, save_path_local]:
                    nome_apresentador_path = os.path.join(path, 'nome_apresentador.json')
                    with open(nome_apresentador_path, 'w', encoding='utf-8') as json_file:
                        json.dump([dados_json], json_file, ensure_ascii=False, indent=4)