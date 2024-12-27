import socket
from colors import *
def conexao(ip, start_port, end_port):
    """Função que realiza a conexão com o host e verifica se a porta está aberta"""
    for porta in range(start_port, end_port + 1):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.settimeout(1)
        resultado = tcp.connect_ex((ip, porta))
        if resultado == 0:
            servico = socket.getservbyport(porta)
            print(GREEN + f"Porta: {porta} ABERTA  \tServiço: {servico}" + END)
            tcp.close()
    return "\nScan Finalizado!"
