"""
Written by Jorge Orlando Miranda Ñahui
Este codigo es de parte de servidor que utilizara tambien un objeto SOCKET . el servidor estara escuchando
nuevas conexiones de los clientes , luego de aceptar alguna conexion se procedera a esperar datos del cliente . 
el servidor estara leyendo los datos que el cliente estara enviando . 
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
PORT =65432       # PUERTO QUE UTILIZARAN PARA EL INTERCAMBIO DE INFORMACIÓN
#crear socket con IPV4 Y PROTOCOLO TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #el metodo bind sirve para unir el socket a un HOST y Puerto determinado
    #método bind((host,port))
    s.bind((HOST, PORT))
    print("ESCUCHAR CONEXIONES")
    s.listen()
    while True:
        # habilitar al servidor para aceptar conexiones
        conn, addr = s.accept()
        print("CLIENTE CON IP Y PUERTO:", addr)
        n = 0
        flag = 0
        # cliente conectado
        with conn:
            a2 = 0
            while True:
                # leer los bytes hasta un limite maximo
                #establecer lectura de datos desde el cliente
                print("A LA ESPERA DE DATOS DEL CLIENTE")
                data = conn.recv(1000000)
                # si no hay datos
                if not data:
                    flag = 1
                    #CLIENTE DESCONECTADO DEL SERVIDOR
                    print("CLIENTE DESCONECTADO")
                    a2+=1
                    if a2==2:
                         break
                # si hay datos
                else:
                    print("DATO RECIBIDO DEL CLIENTE : ")
                    img = None
                    try:
                        # ---- de-serializar los bytes a objetos de python
                        img = pickle.loads(data)
                 
                        #SI SON NUMPY.NDARRAY MOSTRARLO CON OPENCV
                    
                        if isinstance(img,np.ndarray):
                            # realizar una interpolación
                            img2 = cv2.resize(img, (520, 480), interpolation=cv2.INTER_CUBIC)
                            cv2.imshow("IMAGEN RECIBIDA DEL CLIENTE", img2)
                            
                            #ESPERAR LA TECLA q PARA CERRAR
                            if cv2.waitKey(1) == ord("q"):
                                break
                        else:
                            #MOSTRA DATOS
                            print(img)
                    # se origino un error en el bloque try
                    except:
                        print("ERROR EN EL BLOQUE TRY")
                        pass
            #descomentar esto si en caso estan transmitiendo objetos numpy.ndarray que representaran imagenes
            #cv2.destroyAllWindows()




