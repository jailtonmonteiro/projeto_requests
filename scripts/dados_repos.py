from processamento_dados import DadosRepositorios
from manipula_repos import ManipulaRepositorios

tokenGit = 'token_git' # Cole aqui o seu token da API do GitHub
contaGit = 'openai' # Digite aqui a conta da empresa buscada
usernameGit = 'jailtonmonteiro' # Digite aqui o seu nome de usuário do GitHub

# Manipulando dados
Reps = DadosRepositorios(contaGit, tokenGit).criarDataFrame()
print('Finalizado a extração e salvamentos dos dados')

# Manipulando repositórios
novoRepo = ManipulaRepositorios(usernameGit, tokenGit)
nome_repo = 'linguagens-repositorios-empresas'

novoRepo.cria_repo(nome_repo)
novoRepo.add_arquivo(nome_repo, f'{contaGit}.csv', f'data_processed/{contaGit}.csv')