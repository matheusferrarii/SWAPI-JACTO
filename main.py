from funcoes import listar_personagens, detalhar_um_personagem, filtrar_por_gênero, organizar_naves,listar_filmes,recomendar_a_sequência_de_filmes



while True:
    print("_"*30 + "Seja bem-vindo a sua central de controle Star Wars" + "_"*30)
    perguntas = int(input(""" 
Aqui, você pode:
    1️⃣ Visualizar os 10 primeiros personagens da saga.
    2️⃣ Obter detalhes completos sobre cada um deles.
    3️⃣ Filtrá-los por gênero.
    4️⃣ Descobrir em quais filmes seu personagem favorito aparece.
    5️⃣ Explorar informações detalhadas sobre as naves, organizadas dentro de suas ordenações.
    6️⃣ Receber sugestões personalizadas sobre a melhor ordem para assistir à saga, com base em filtros específicos.
    7️⃣ Encerrar expedição!!

Tudo isso para tornar sua jornada interespacial ainda mais épica! Escolha seu lado da Força e embarque nessa aventura no universo de Star Wars! 🚀✨
                          \n"""))

    if perguntas == 1:
        listar_personagens()
    
    elif perguntas == 2:
        detalhar_um_personagem()


    elif perguntas == 3:
        filtrar_por_gênero()
    elif perguntas == 4:
       listar_filmes()

    elif perguntas == 5:
        organizar_naves()
    
    elif perguntas == 6:
       recomendar_a_sequência_de_filmes()

    elif perguntas == 7:
        print("Que a força esteja com você!!")
        break
        
    
    else:
        print("Opção inválida")