import requests

# Definir a URL com o token e parâmetros
url = "https://firms.modaps.eosdis.nasa.gov/api/country/csv/460bac4dee9749ed9d693a610dce6fa7/VIIRS_SNPP_NRT/USA/10"

# Fazer a requisição GET
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Salvar os dados em um arquivo CSV
    with open("fire_data_usa2.csv", "wb") as file:
        file.write(response.content)
    print("Dados de incêndios florestais baixados com sucesso!")
else:
    print(f"Erro na requisição: {response.status_code}")
