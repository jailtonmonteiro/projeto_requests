#Importações
import requests
import pandas as pd
from math import ceil

class DadosRepositorios:
    
    def __init__(self, owner, tokenApi):
        self.owner = owner
        self.apiBaseUrl = 'https://api.github.com'
        self.accessToken = tokenApi
        self.headers = {'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + self.accessToken}

    def listaRepositorios(self):
        reposList = []

        #Calcular as páginas
        resp = requests.get(f'{self.apiBaseUrl}/users/{self.owner}')
        numPages = ceil(resp.json()["public_repos"]/30)

        for pageNum in range(1, numPages+1):
                try:
                        url = f'{self.apiBaseUrl}/users/{self.owner}/repos?page={pageNum}'
                        response = requests.get(url, headers=self.headers)
                        reposList.append(response.json())
                except:
                        reposList.append(None)

        return reposList
    
    def nomesRepo(self, reposList):
        nomesRepo = []

        for page in reposList:
            for repo in page:
                try:
                     nomesRepo.append(repo['name'])
                except:
                     pass

        return nomesRepo
    
    def nomesLinguagens(self, reposList):
         
        liguagensRepo = []

        for page in reposList:
             for repo in page:
                try:
                    liguagensRepo.append(repo['language'])
                except:
                     pass
        return liguagensRepo
    
    def criarDataFrame(self):
        
        repositorios = self.listaRepositorios()
        nomes = self.nomesRepo(repositorios)
        linguagens = self.nomesLinguagens(repositorios)
        
        dados = pd.DataFrame()
        dados['Respository_name'] = nomes
        dados['Repository_language'] = linguagens
        dados.to_csv(f'data_processed/{self.owner}.csv')

        return dados