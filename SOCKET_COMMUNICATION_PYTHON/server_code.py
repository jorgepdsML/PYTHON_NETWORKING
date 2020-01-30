"""
Written by Jorge Orlando Miranda Ñahui
"""
import cv2
import numpy as np
import socket
import pickle
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT =65432       # Port to listen on (non-privileged ports are > 1023)
#crear socket con IPV4 Y PROTOCOLO TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
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
                    print("CLIENTE DESCONECTADO")
                    a2+=1
                    if a2==2:
                         break
                # si hay datos
                else:
                    print("DATO RECIBIDO DEL CLIENTE : ")
                    img = None
                    try:
                        # ---- de-serializar los bytes a datos
                        img = pickle.loads(data)
                        #print(isinstance(img, np.ndarray))
                        #SI SON NUMPY.NDARRAY MOSTRARLO CON OPENCV
                        if isinstance(img,np.ndarray):
                            # realizar una interpolación
                            img2 = cv2.resize(img, (520, 480), interpolation=cv2.INTER_CUBIC)
                            cv2.imshow("hola", img2)
                            if cv2.waitKey(1) == ord("q"):
                                break
                        else:
                            #MOSTRA DATOS
                            print(img)
                    # se origino un error en el bloque try
                    except:
                        print("ERROR EN EL BLOQUE TRY")
                        pass
            #cv2.destroyAllWindows()




