import csv
from get_fire_image import download_satellite_images_to_s3

# Caminho para o arquivo CSV
csv_file = "fire_data_usa.csv"

# Nome do bucket S3
bucket_name = "nasa-bucket"

# Abrir e ler o arquivo CSV
with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        lat = row['latitude']
        long = row['longitude']
        acq_date = row['acq_date']
        satellite = row['satellite']
        
        # Fazer o download e upload da imagem diretamente para o S3
        download_satellite_images_to_s3(lat, long, acq_date, satellite, bucket_name)
