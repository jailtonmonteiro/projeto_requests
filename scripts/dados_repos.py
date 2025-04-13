from processamento_dados import DadosRepositorios

tokenGit = 'token_git' # Cole aqui o seu token da API do GitHub
contaGit = 'amzn' # Digite aqui a conta da empresa buscada

Reps = DadosRepositorios(contaGit, tokenGit).criarDataFrame()
print('Finalizado a extração e salvamentos dos dados')
