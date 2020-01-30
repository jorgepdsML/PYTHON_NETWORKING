"""
written by Jorge Orlando Miranda Ñahui
Codigo del lado del cliente que se creara un SOCKET con un HOST local y PUERTO 65432 .
Los datos que se enviaran al servidor se convertiran a un blujo de bytes (STREAM BYTES ) mediante 
el uso del modulo pickle ,este paso es llamado Serialización . 
Los datos que se enviaran deben estar en formato de BYTES 
La serialización se realizara mediante la función dumps del modulo pickle
"""
import socket
import numpy as np
import cv2
import pickle
import time
HOST = '127.0.0.1'  # hostname del servidor o dirección IP
PORT = 65432        # puerto de comunicación
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("CONECTADO AL SERVIDOR")
    print("5 SEGUNDOS ")
    time.sleep(5)
    #mensaje a enviar
    img="PYTHON SOCKET CLIENTE"
    # serializar de objetos de python a flujo de bytes
    datos=pickle.dumps(img)
    print("RECIEN ENVIANDO DESPUES DE 1 SEGUNDO")
    time.sleep(1)
    # enviar todo los bytes al servidor
    s.sendall(datos)
    time.sleep(4)
    s.sendall(datos+bytes("120","utf-8"))
    print("CLIENTE : 10 SEGUNDOS")
    time.sleep(10)
    #Enviar ultimo mensaje
    s.sendall(pickle.dumps("EL CLIENTE HA CADUCADO"))

#codigo de fin de programa
print("FIN PROGRAMA DEL  CLIENTE")
