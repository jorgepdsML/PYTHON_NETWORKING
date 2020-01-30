"""
Written by Jorge Orlando Miranda Ñahui
Este codigo es de parte de servidor que utilizara tambien un objeto SOCKET . el servidor estara escuchando
nuevas conexiones de los clientes , luego de aceptar alguna conexion se procedera a esperar datos del cliente .
el servidor estara leyendo los datos que el cliente estara enviando . los datos que se leera estaran en formato bytes
se tiene que convertir de bytes al tipo de dato que esperamos . Se debe saber de antemano cual fue la codificación que
el cliente ha realizado en los bytes que transmitira al servidor.

Se utilizara el modulo pickle para realizar los procesos de Serialización y Deserealización .
Serialización permite convertir un objeto de python a uno de flujo de bytes
Deserialización permite convertir de flujo de bytes al correspondiente objeto de python.

El servidor y cliente  utilizaran el protocolo de transporte conocido como TCP y tambien dirección IP V4
para construir un objeto (SOCKET) se utilizara la clase socket del modulo socket
socket.AF_INET indica indica IP V4
socket.SOCK_STREAM indica TCP
"""
import cv2
import numpy as np
import socket
import pickle

HOST = '127.0.0.1'  # LOCAL host
PORT = 65432  # PUERTO QUE UTILIZARAN PARA EL INTERCAMBIO DE INFORMACIÓN
# crear socket con IPV4 Y PROTOCOLO TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # el metodo bind sirve para unir el socket a un HOST y Puerto determinado
    # método bind((host,port))
    s.bind((HOST, PORT))
    print("ESCUCHAR CONEXIONES")
    s.listen()
    while True:
        # habilitar al servidor para aceptar conexiones
        conn, addr = s.accept()
        print("-------UN CLIENTE CON IP Y PUERTO:", addr)
        n = 0
        # cliente conectado
        with conn:

            while True:
                # leer los bytes hasta un limite maximo
                # establecer lectura de datos desde el cliente
               # print("-----ESPERANDO DATOS DEL CLIENTE----------")
                data = conn.recv(1000000)
                # si no hay datos
                if not data:

                    # CLIENTE DESCONECTADO DEL SERVIDOR
                    print("----CLIENTE DESCONECTADO----")
                    print("-----BUSCAR OTRAS CONEXIONES----")
                    break
                # si hay datos
                else:
                    print("-------DATO RECIBIDO DEL CLIENTE ES:  ",end=" ")
                    img = None
                    try:
                        # ---- Deserializar los bytes a objetos de python
                        img = pickle.loads(data)
                        #MOSTRAR LOS DATOS QUE SE HAN RECIBIDO DEL CLIENTE
                        print(img)
                    # se origino un error en el bloque try
                    except:
                        print("ERROR EN EL BLOQUE TRY")
                        pass
            # descomentar esto si en caso estan transmitiendo objetos numpy.ndarray que representaran imagenes
            # cv2.destroyAllWindows()



