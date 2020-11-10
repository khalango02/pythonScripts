#!/usr/bin/python3

import socket
import sys

portas = [80, 443, 21, 22, 23, 25, 3306, 3380, 8080, 6380, 27017, 27018, 4369, 5672, 6379]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

def portScanner(portas):
    for porta in portas:
        if sock.connect_ex((sys.argv[1], porta)):
            print("Porta ", porta," fechada")
        else:
            print("Porta ", porta, " aberta")
    print("Concluído")
sock.close

portScanner(portas)
