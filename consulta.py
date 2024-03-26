import requests
import json
import pyperclip as pc
import re

urlinc = "https://publica.cnpj.ws/cnpj/"
entrada = str(input("Insira o cnpj da empresa a ser consultada: "))
urlcomp = urlinc + entrada.replace('.', '').replace('/', '').replace('-', '')
cnpj_req = requests.get(urlcomp)
status = cnpj_req.status_code

if status == 200:

  js = dict(json.loads(cnpj_req.text))
  nome = str('\nNome: ' + js['razao_social'])
  cnpjexpo = str('\nCNPJ: ' + entrada)
  endereco = str('\nEndereço: ' + js['estabelecimento']['logradouro'])

  try:
    cep_slice = str('\nCEP: ' + js['estabelecimento']['cep'][0:5] + '-' + js['estabelecimento']['cep'][5:8])
    bairro = str('\nBairro: ' + js['estabelecimento']['bairro'])
    cidade = str('\nMunicípio: ' + js['estabelecimento']['cidade']['nome'])
  except:
    ('Não foi possível encontrar o CEP da dita empresa.')
  print(nome, cnpjexpo, endereco, cep_slice, bairro, cidade)
  saida = (nome + cnpjexpo + endereco + cep_slice + bairro + cidade)
  pc.lazy_load_stub_copy(saida)
elif status == 429:
  print('A API de consulta está com problema, aconselhamos que espere um pouco.')