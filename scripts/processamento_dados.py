import requests
import pandas as pd

class DadosRepositorios:
    
    def __init__(self, owner):
        self.owner = owner
        self.apiBaseUrl = 'https://api.github.com'
        self.accessToken = 'token_git'
        self.headers = {'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + self.accessToken}