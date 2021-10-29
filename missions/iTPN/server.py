import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, client = udp.recvfrom(1024)
    print(client, msg)
udp.close()