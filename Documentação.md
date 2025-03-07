Visão Geral:
Este projeto permite explorar informações sobre personagens, filmes e naves espaciais, utilizando a API SWAPI (Star Wars API).
O sistema fornece detalhes sobre os personagens, permite filtrar por gênero, listar filmes, organizar naves e recomendar sequências para assistir à saga.

Requisitos:
Antes de executar, verifique se possui os seguintes itens instalados:
Python 3.12
Biblioteca requests (para acessar a API SWAPI)
Para instalar a biblioteca, execute o seguinte comando:
pip install requests

Como rodar:
Primeiramente, clone o repositório:
https://github.com/matheusferrarii/SWAPI-JACTO.git
Após clonar, execute o arquivo main.
Para interagir com o sistema, abra o terminal e insira o número correspondente à funcionalidade que deseja acessar.
Dentro de cada funcionalidade, você verá opções adicionais. Para selecionar uma delas, basta inserir o número correspondente à opção desejada.
Se sua pesquisa for sobre um personagem específico, insira apenas o ID do personagem. O ID pode ser encontrado no catálogo de personagens, acessível na funcionalidade 2 (Detalhar um personagem).
Se sua pesquisa for sobre filmes, insira o número do filme que deseja consultar. O número do filme pode ser visualizado no catálogo de filmes, acessível na funcionalidade 4 (Descobrir em quais filmes seu personagem favorito aparece).
Caso tenha alguma dúvida ou queira saber o raciocínio utilizado, acesse o vídeo:
https://youtu.be/ac7Mc_vS2OI

Como está estruturado:
O projeto está dividido em dois arquivos principais:
main.py: Contém o menu interativo para o usuário escolher a funcionalidade desejada.
funcoes.py: Contém todas as funções responsáveis por acessar a API e processar os dados.

Funcionalidades:
1. Listar Personagens
Exibe os 10 primeiros personagens da saga com informações como:  nome, altura e peso.

2. Detalhar um Personagem
Permite visualizar informações completas de um personagem, como:
nome, altura, peso cor do cabelo, cor da pele, cor dos olhos, ano de nascimento, gênero, planeta natal, filmes em que aparece, epécies, veículos e naves estelares.
Para acessar tudo isso basta apenas inserir o ID do personagem selecionado, que pode ser visualizado na função catálogo de personagens. 

4. Filtrar personagens por Gênero
Filtra personagens de acordo com o seu gênero: masculinos, femininos ou outros.

4. Listar Filmes
Exibe todos os filmes e seus elencos;
Expõe o catálogo de filmes;
Permite selecionar um filme para ver os personagens que aparecem nele;
Possibilita a pesquisa para visualizar em qual/quais filmes um determinado personagem aparece;

5. Organizar Naves
Ordena as naves estelares com base em:
Comprimento (crescente ou decrescente);
Tamanho da tripulação(crescente ou decrescente); 
Capacidade de passageiros(crescente ou decrescente). 
Para que assim, possam ser visualizadas várias informações sobre as naves, de acordo com a organização escolhida 

6. Recomendar sequência de filmes
Sugere formas diferentes de assistir a saga, dentro dos critérios:
Ordem de lançamento;
Ordem cronológica;
Ordem baseada na história de um personagem específico.

7. Sair do programa
Finaliza a execução do sistema.

Possíveis erros e soluções:
Erro de conexão com a API: Verifique sua internet e tente novamente.
Personagem ou Filme Não Encontrado: Certifique-se de que o ID inserido é válido. 
Você pode verificar os IDs disponíveis nas listagens de personagens ou filmes.

Conclusão:
Após embarcar nesta aventura espacial por meio do código, você terá a oportunidade de explorar e aproveitar ao máximo as funcionalidades deste projeto. 
O objetivo é não apenas aprofundar seus conhecimentos sobre o universo de Star Wars, mas também facilitar suas pesquisas e ajudá-lo a se tornar um verdadeiro Jedi!
