import socket,pickle
#---COLOCAR IP DE SERVIDOR AL QUE NOS CONECTAREMOS
# O EL LOCAL HOST 127.0.0.1
HOST = '127.0.0.1'
#PUERTO DE COMUNICACIÓN
PORT = 65432
#CREAR UN OBJETO
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#CONECTARSE AL SERVIDOR
s.connect((HOST,PORT))
#nuestro mensaje a enviar
datos=pickle.dumps("*** HOLA BRAINTELS LABS TE HABLA EL CLIENTE ***")
#enviando el mensaje
s.sendall(datos)
#Leer lo que el servidor respondera
mensaje=s.recv(1000)
#convertir de bytes al un objeto de python
dato=pickle.loads(mensaje)
print("----EL SERVIDOR BRAINTELS  LABS NOS RESPONDE------: ")
#MOSTRAR LO QUE EL SERVIDOR BRIANTELS NOS HA RESPONDIDO
print(dato)
#cerrar la comunicación con el servidor
s.close()