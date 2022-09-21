import requests

api_key = "ZTgxNGJmNmItYjNlYy00ZjE4LTgwMzEtOTE4ZGU3YWM5Zjk2"
url = "https://api.m3o.com/v1/weather/Forecast"
localizacao = input('Digite o nome da sua cidade: ')
params = {"days":"2","location":localizacao}
headers = {
  'Content-Type': "application/json",
    'Authorization':"Bearer " + api_key
}
response = requests.request("GET", url, headers=headers, params=params)
data = response.json()

lista_detalhes = data.get('forecast')
region = data.get('country')
print(f'Você selecionou {localizacao} - {region}!\nA máxima temperatura foi de {lista_detalhes[1].get("max_temp_c")}º')
#print(data)
