import requests

def listar_personagens():
    url = "https://swapi.dev/api/people/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        characters = data["results"]
        i = 1
        for character in characters[:10]:
            print(f"      Personagem {i}")
            print(f"""
            Nome: {character["name"]}
            Altura: {character["height"]}
            Peso:  {character["mass"]}
            """)
            print("_"*30)
            i += 1
    else:
        print("Erro ao acessar a API:", response.status_code)

def get_name(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("name") or response.json().get("title", "Desconhecido")
    return "Erro ao obter nome"

def get_names_list(urls):
    if urls:
        result = []
        for url in urls:
            result.append(get_name(url))
        return result
    else:
        return "Nenhum"
    
def detalhar_um_personagem():
    url = "https://swapi.dev/api/people/"
    i = 1
    while True:
        pergunta = int(input("1. Abrir catálogo de personagens\n2. Selecionar personagem\n3. Fechar\n"))
        if pergunta == 1:
            print("Catálogo de personagens")
            while url:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    characters = data["results"]

                    for character in characters:
                        print(f"      Personagem id:{i}")
                        print(f"Nome: {character['name']}")
                        print("_" * 30)
                        i += 1
                    url= data["next"]
                else:
                    print("Erro ao acessar a API:", response.status_code)
                    break
        elif pergunta == 2:
            id = int(input("Insira o id do seu personagem favorito\n"))
            if id >16:
                id += 1 
            url = f"https://swapi.dev/api/people/{id}/"
            response = requests.get(url)

            if response.status_code == 200: 
                data = response.json()  
                print(f"\nDetalhes do Personagem:")
                print(f"""
                    Nome: {data["name"]}
                    Altura: {data["height"]}
                    Peso: {data["mass"]}
                    Cor do cabelo: {data["hair_color"]}
                    Cor da pele: {data["skin_color"]}
                    Cor dos olhos: {data["eye_color"]}
                    Ano de nascimento: {data["birth_year"]}
                    Gênero: {data["gender"]}
                    Planeta: {get_name(data["homeworld"])}
                    Filmes: {get_names_list(data["films"])}
                    Espécies: {get_names_list(data["species"])}
                    Veículos: {get_names_list(data["vehicles"])}
                    Naves estelares: {get_names_list(data["starships"])}
                    """)
      
      
            else:
                print("Erro ao acessar a API:", response.status_code)
    
        elif pergunta == 3:
            print("Fechando")
            break

        else:
            print("Opção inválida")

def filtrar_por_gênero():
    url = "https://swapi.dev/api/people/"
    genders = int(input("Filtrar por gênero:\n1. Masculino \n2. Feminino \n3. Outros\n"))
    id = 0
    if genders == 1:
        gender_filter = "male"
    elif genders == 2:
        gender_filter = "female"
    elif genders == 3:
        gender_filter = "n/a"
    else:
        print("Opção inválida")

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            characters = data["results"]

            for character in characters:
                id +=1
                if character['gender'] == gender_filter:
                    print(f"      Personagem {id}")
                    print(f"Nome: {character['name']}")
                    print("_" * 30)

                url = data["next"]


def listar_filmes():
    url_films = "https://swapi.dev/api/films/"
    list_movies = int(input("""\n
1. Para ver todos os filmes e seu elenco 
2. Abrir catálogo de filmes 
3. Selecione um filme e veja seu elenco
4. Veja em qual filme seu personagem favorito aparece\n"""))

    if list_movies == 1:
        id_films = 1
        response = requests.get(url_films)
        if response.status_code == 200:
            data = response.json()
            films = data["results"]

            for film in films:
                print(f"\nFilme {id_films}")
                print(f"Título: {film['title']}")
                print("_" * 30)
                print("Elenco:")

                for character_url in film['characters']:
                    characters = requests.get(character_url)
                    if characters.status_code == 200:
                        characters_data = characters.json()
                        print(f"- {characters_data['name']}") 
                    else:
                        print("Erro ao carregar personagem")
                id_films += 1
    
    elif list_movies == 2:
        id_films = 0
        while True:
            response = requests.get(url_films)
            if response.status_code == 200:
                data = response.json()
                films = data["results"]

            for film in films:
                id_films +=1
                print(f"      Movies {id_films}")
                print(f"Título: {film['title']}") 
                print("_" * 30)
            break

    elif list_movies == 3:
        id_films = input("Digite o id do filme:\n")
        url_films = f"https://swapi.dev/api/films/{id_films}/"
        while True:
            response = requests.get(url_films)
            if response.status_code == 200:
                data = response.json()

                print(f"\nFilme {id_films}")
                print(f"Título: {data['title']}")
                print("_" * 30)
                print("Elenco:")

                for characters_url in data['characters']:
                    characters = requests.get(characters_url)
                    if characters.status_code == 200:
                        characters_data = characters.json()
                        print(f"- {characters_data['name']}") 
                    else:
                        print("Erro ao carregar personagem")
                break
    elif list_movies == 4:
        mostrar_filme_do_personagem()

    else:
        print("Opção inválida")


def organizar_naves():
    ordenar = int(input(f"""Escolha a forma de ordenar as naves:
1. Comprimento(ordem crescente)
2. Comprimento(ordem decrescente)
3. Tripulação(ordem crescente)
4. Tripulação(ordem decrescente)
5. Passageiros(ordem crescente)
6. Passageiros(ordem decrescente)\n{"_"*30}\n
"""))

    url_starships = "https://swapi.dev/api/starships/"
    starship_list = []

    while url_starships:
        response = requests.get(url_starships)

        if response.status_code == 200:
            data = response.json()
            starships = data["results"]

        for starship in starships:
            try:
                length = float(starship["length"].replace(",", ""))
            except ValueError:
                length = float('nan') 

            try:
                crew = int(starship["crew"].replace(",", "").split("-")[0])
            except ValueError:
                crew = float('nan') 

            try:
                passengers = int(starship["passengers"].replace(",", "").split("-")[0])
            except ValueError:
                passengers = float('nan') 

            starship_list.append({
                "name": starship["name"],
                "length": length,
                "crew": crew,
                "passengers": passengers
            })
            url_starships= data["next"]
    if ordenar == 1:
        starship_list.sort(key=lambda x: x["length"])
    elif ordenar == 2:
        starship_list.sort(key=lambda x: x["length"], reverse=True)
    elif ordenar == 3:
        starship_list.sort(key=lambda x: x["crew"])
    elif ordenar == 4:
        starship_list.sort(key=lambda x: x["crew"], reverse=True)
    elif ordenar == 5:
        starship_list.sort(key=lambda x: x["passengers"])
    elif ordenar == 6:
        starship_list.sort(key=lambda x: x["passengers"], reverse=True)
    else:
        print("Opcao invalida")

    for i,ship in enumerate(starship_list,1):
        print(f"\nNave {i}: {ship['name']}")
        print(f"Comprimento: {ship['length']}")
        print(f"Tripulação: {ship['crew']}")
        print(f"Passageiros: {ship['passengers']}")
        print("_" * 30)
    


def recomendar_a_sequência_de_filmes():
    ordem = int(input(f"""Você deseja assistir Star Wars em qual ordem:
    1. Ordem de lançamento
    2. Ordem cronológica 
    3. História de um personagem 
    {"_"*30}\n
    """))
    url_films = "https://swapi.dev/api/films/"
    films_list = []
    while url_films:
        response = requests.get(url_films)
        if response.status_code == 200:
            data = response.json()
            films = data["results"]

            for film in films:
                films_list.append({
                "title": film["title"],
                "episode_id": film["episode_id"], 
                "release_date": film["release_date"]
                         })
      
            url_films = data["next"]
        else:
            print("Erro ao acessar a API.")
            break


    if ordem == 1:
        films_list.sort(key=lambda x: x["release_date"])
    elif ordem == 2:
        films_list.sort(key=lambda x: x["episode_id"])
    elif ordem == 3:
        print("\nOrdem recomendada:")
        mostrar_filme_do_personagem()
        return  
    if films_list:
        print("\nOrdem recomendada:")
        for film in films_list:
            print(f"{film['title']} (Episódio {film['episode_id']}) - {film['release_date']}")
    else:
        print("\nNenhum filme encontrado para a opção selecionada.")





def mostrar_filme_do_personagem():
    id = int(input("Insira o id do seu personagem favorito\n"))
    if id >16:
        id += 1 
    url = f"https://swapi.dev/api/people/{id}/"
    response = requests.get(url)

    if response.status_code == 200: 
        data = response.json()  
        print(f"\nNome: {data['name']}")
        print("_"*30)
        print("Filmes:")
        
        films = data["films"]

        if films:
                for film_url in films:
                    response = requests.get(film_url)
                    if response.status_code == 200:
                        film_data = response.json()
                        print(f"{film_data['title']} (Episódio {film_data['episode_id']}) - {film_data['release_date']}")
                    else:
                        print(f"Erro ao acessar o filme: {film_url}")
        else:
            print("Nenhum filme encontrado para este personagem.")
