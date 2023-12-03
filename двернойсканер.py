import socket
from termcolor import colored

def scan(target, ports):
    print(colored('\nНачинаю искать ' + str(target), 'red'))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        print(colored("[+] Открытая дверь " + str(port), 'red'))
        sock.close()
    except:
        pass

targets = input(colored("[*] Введите цели для сканирования (разделите их на ,): ", 'red'))
ports = int(input(colored("[*] Введите количество портов, которые вы хотите сканировать: ", 'red')))
if ',' in targets:
    print(colored("[*] Сканирование нескольких целей ", 'red'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else: 
    scan(targets, ports)

