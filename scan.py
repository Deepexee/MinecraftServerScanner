# J'ai décris toutes les parties du scripts pour que tout le monde puisse comprendre
# n'hésitez pas a proposer des mise a jour pour crée quelque chose de vraiment optimiser

# https://twitch.tv/deepexee

import random # l'aléatoire
import socket # La connexion
import threading, os # La puissance et les commandes de base de windows
from colorama import Fore, init # La couleur

init()

ports = [25565, 25566, 25567] # Vous pouvez changer les port pour scanner d'autres choses, 80 & 443 = http, 2024 ou 22 = ssh
output_file = "hit.txt" # Nom du fichier
num_threads = 2500 # Changez cette valeur pour augementer la puissance

def generate_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4)) # Crée une adresse ip aléatoire

def scan_ip(ports):
    while True: # Crée une boucle
        ip = generate_ip() # La variable Ip appelle la fonction Ligne 17 qui crée une adresse ip 
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port)) # Ce connecte
            if result == 0: # Si le script arrive a ce connecter
                print(f"{ip} is a Minecraft server!") # Affiche dans la console
                with open(output_file, 'a') as file: # Ouvre le fichier texte
                    file.write(f"{ip}\n") # Ecris dans le fichier texte 
                sock.close()
                return
            else: # Sinon
                pass # Continue a chercher
            sock.close()

def thread_worker():
    scan_ip(ports)

if __name__ == "__main__":
    os.system('title MinecraftScan - twitch.tv/deepexee') # je change le nom de la fenetre

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=thread_worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()