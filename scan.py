import random
import socket
import threading, os
from colorama import Fore, init
import minestat

init()

ports = [25565, 25566, 25567]
output_file = "hit.txt"
num_threads = 500

def generate_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def scan_ip(ports):
    while True:
        ip = generate_ip()
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                ms = minestat.MineStat(ip, port)
                with open(output_file, 'a') as file:
                    if ms.version != "None":
                        print(f"{ip} is a Minecraft server!")
                        file.write(f"{ip}:{port}\nVersion: {ms.version}\n")
                    else:
                        sock.close()
                        pass
                return
            sock.close()

def thread_worker():
    scan_ip(ports)

if __name__ == "__main__":

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=thread_worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
