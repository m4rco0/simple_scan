import socket
GREEN = "\033[32m"
WHITE = '\033[0m'
def banner():
    with open("art.txt", "r") as  f:
        conteudo =  f.read()
        return conteudo



def conexao(ip, port, tipo):
    if tipo == "TCP":
        for portas in range(1, port + 1):
            destino = (ip, portas)
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.settimeout(1)
            try:
                tcp.connect((ip, portas))
                print(f'porta({portas}) = OPEN', end = " |   ")
            except:
                pass
            tcp.close()
    return "\nScan finalizado"

art = banner()
print(GREEN + art)
#print(WHITE +"\nInfrome o tipo de conexão que tu vai querer:\n opções: TCP")
tipo = "TCP"
if tipo == "TCP":
    print("informe o ip e o range de porta separados por um espaço:\tex \"ip port\"")
    ip, port = input().split()
    saida = conexao(ip, int(port), tipo)
    print(f'{saida}')
