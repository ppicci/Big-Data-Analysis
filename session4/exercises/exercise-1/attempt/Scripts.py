import os
import requests
import random
def file_opener(filepath):
    urls=[]
    with open(filepath, 'r') as file:
        for line in file:
            line_data = line.strip()
            urls.append(line_data)
        return urls

def photo_downloader(url):
    output_dir = "output"

    os.makedirs(output_dir, exist_ok=True)

    img_bytes = requests.get(url).content

    name = random.randint(1, 10000)

    img_name = f'{name}.jpg'

    full_path = output_dir+'/'+img_name

    with open(full_path, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded and saved in {output_dir}...')



