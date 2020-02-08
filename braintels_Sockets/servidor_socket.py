import socket,pickle,time
#ESTABLECER LA IP DEL SERVIDOR (DE ESTE ORDENADOR)
HOST = '127.0.0.1'
PORT = 65432  # PUERTO
#instanciar un objeto de la clase socket del modulo socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
#escuchar conexiones del cliente
s.listen()
#aceptar la conexión
cliente,direccion=s.accept()
with cliente:
    #recibir maximo 1000 bytes del cliente
    dato=cliente.recv(1000)
    if not dato:
        #cliente se ha desconectado
        print("DESCONECTADO")
    else:
        print("-------EL CLIENTE NOS DICE ------")
        #mostrar lo que el cliente me ha enviado
        print(pickle.loads(dato))
        time.sleep(2)
        #devolver un mensaje
        cliente.sendall(pickle.dumps("*** AQUI PUES MASCOTA :v :v *** "))
s.close()
