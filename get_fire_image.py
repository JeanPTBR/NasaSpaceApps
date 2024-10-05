import requests
import boto3
from io import BytesIO

# Inicializa o cliente do S3
s3_client = boto3.client('s3')

# Função para baixar imagens de satélites usando lat/long e data de aquisição e enviar diretamente para o S3
def download_satellite_images_to_s3(lat, long, acq_date, satellite, bucket_name):
    # Definir a URL base (exemplo para LANDSAT ou VIIRS)
    url = f"https://api.nasa.gov/planetary/earth/imagery?lon={long}&lat={lat}&date={acq_date}&dim=0.1&api_key=YOUR_API_KEY"
    
    # Fazer a requisição GET para baixar a imagem
    response = requests.get(url)
    
    if response.status_code == 200:
        # Criar o nome do arquivo no formato desejado
        file_name = f"sat_fire_images/image_{satellite}_{lat}_{long}_{acq_date}.png"
        
        # Armazenar o conteúdo da imagem em memória usando BytesIO
        image_data = BytesIO(response.content)
        
        # Fazer o upload para o S3
        try:
            s3_client.upload_fileobj(image_data, bucket_name, file_name)
            print(f"Imagem {file_name} enviada com sucesso para o S3.")
        except Exception as e:
            print(f"Erro ao enviar a imagem para o S3: {e}")
    else:
        print(f"Erro ao baixar a imagem: {response.status_code}")
