# Code by xTyzenIV
import requests
from tqdm import tqdm

def download_cudaToolkit():
    url = "https://developer.download.nvidia.com/compute/cuda/12.3.2/local_installers/cuda_12.3.2_546.12_windows.exe"  

    response = requests.get(url, stream=True)
    taille_fichier = int(response.headers.get('content-length', 0))

    with open('cuda_12.3.2_546.12_windows.exe', 'wb') as fichier, tqdm(
        desc="Download cuda_12.3.2_546.12_windows.exe",
        total=taille_fichier,
        unit='o',
        unit_scale=True,
        unit_divisor=1024,                                                                                                                                                                                                                                                                                                                                                                                                                      # Code by xTyzenIV
    ) as barre_progression:
        for morceau in response.iter_content(chunk_size=1024):
            if morceau:
                fichier.write(morceau)
                barre_progression.update(len(morceau))

download_cudaToolkit()



# Code by xTyzenIV
