import requests
from datetime import date

dia_0 = date(2021,5,25)
numero_da_revista_no_dia_0 = 2629
hoje = date.today()
delta = hoje - dia_0
dias = delta.days
semanas = int(dias / 7)
numero_da_revista_atual = 'RM' + str(numero_da_revista_no_dia_0 + semanas)

url = 'http://revistas.inpi.gov.br/txt/' + numero_da_revista_atual + '.zip'
path = '<DIGITE O CAMINHO DA PASTA DE DESTINO DOS ARQUIVOS BAIXADOS>'

r = requests.get(url)
open(path + numero_da_revista_atual + '.zip', 'wb').write(r.content)
