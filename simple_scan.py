import socket
import sys

GREEN = "\033[32m"
WHITE = '\033[0m'
END = '\033[0m'


def banner():
    """Função que retorna o banner do programa"""
    with open("art.txt", "r") as f:
        conteudo = f.read()
        return conteudo


def conexao(ip, start_port, end_port, tipo):
    """Função que realiza a conexão com o host e verifica se a porta está aberta"""
    if tipo == "TCP":
        for porta in range(start_port, end_port + 1):
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.settimeout(1)
            resultado = tcp.connect_ex((ip, porta))
            if resultado == 0:
                print(GREEN + f"Porta: {porta} ABERTA" + END)
                tcp.close()
    return "\nScan Finalizado!"


if __name__ == '__main__':
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        port = sys.argv[2]

        if '-' in port:  # Verifica se o usuário informou um range de portas ou apenas uma porta
            port = port.split('-')

        tipo = "TCP"

        art = banner()
        print(GREEN + art + END)
        print()

        if len(port) > 1:  # Verifica se o usuário informou um range de portas ou apenas uma porta
            print(conexao(ip, int(port[0]), int(port[1]), tipo))
        else:
            print(conexao(ip, int(port), int(port), tipo))

    else:
        art = banner()
        print(GREEN + art + END)

        # print("\nInforme o tipo de conexão que tu vai querer:")
        # print("Opções:")
        # print("TCP")

        tipo = "TCP"

        # tipo = input("Conexão desejada: ")
        if tipo == "TCP":
            print("\nInforme o IP e o RANGE de portas: \t Ex: 192.168.0.1 21-8080")
            ip, port = input().split()

            if '-' in port:  # Verifica se o usuário informou um range de portas ou apenas uma porta
                port = port.split('-')
                print(conexao(ip, int(port[0]), int(port[1]), tipo))
            else:
                print(conexao(ip, int(port), int(port), tipo))
