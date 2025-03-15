import socket
from colors import *
""" Construtor de um scanner"""
class Scanner:
    def __init__(self, target, portaInicia, portaFinal):
        self.target = target
        self.portaInicia = portaInicia
        self.portaFinal = portaFinal
    
    """ 
    função que executar o scan dos alvos até as portas determinadasd
    percorre de porta_inicial até porta final de forma linear O(n)
    e insere em uma tupla, com cada linha possuindo (porta, serviço)
    que são retornada no final do scan para serem printados no log da interface
    """
    def scannear(self):
        portas_abertas = []
        print(f"iniciando scan em {self.target} ({self.portaInicia}-{self.portaFinal})")
        """Função que realiza a conexão com o host e verifica se a porta está aberta"""
        for porta in range(self.portaInicia, self.portaFinal + 1):
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.settimeout(0.3)
            resultado = tcp.connect_ex((self.target, porta))
            if resultado == 0:
                try:
                    servico = socket.getservbyport(porta)
                except OSError:
                    servico = "Desconhecido"
                print("Porta aberta ", porta, servico)
                portas_abertas.append((porta, servico))
                tcp.close()
        print("Scan acabou")
        return portas_abertas
    
    """ Metodos para definir valores"""

    """ metodo set_target, setando o alvo
        - target string no formato '0.0.0.0' de ip
    """
    def set_target(self, target):
        self.target = target

    """ metodo par mudar avariavel da prota inicia
       init_port -> porta inicial do scan
    """
    def set_initial_port(self, init_port):
        self.portaInicia = init_port

    """ metodo para setar a porta final do scan"""
    def set_end_port(self, end_port):
        self.portaFinal = end_port

    """ método para retornar o alvo do scan"""
    def get_target(self):
        return self.target
    
    """ método para retornar a porta inicial do scan"""
    def get_init_port(self):
        return self.portaInicia
    
    """ método para retornar a porta final do scan"""
    def get_end_port(self):
        return self.portaFinal
    
