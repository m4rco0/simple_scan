import socket
import concurrent.futures
from colors import *
import queue
""" Construtor de um scanner"""
class Scanner:
    def __init__(self, target, portaInicia, portaFinal, max_threads):
        self.target = target
        self.portaInicia = portaInicia
        self.portaFinal = portaFinal
        self.fila = queue.Queue()
        self.max_threads = max_threads

    """ 
    função que executar o scan dos alvos até as portas determinadasd
    percorre de porta_inicial até porta final de forma linear O(n)
    e insere em uma tupla, com cada linha possuindo (porta, serviço)
    que são retornada no final do scan para serem printados no log da interface
    """
    def scannear(self):
        """Função que realiza a conexão com o host e verifica se a porta está aberta"""
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            futures = {
                    executor.submit(self.scan_with_threads, self.fila, porta): porta
                    for porta in range(self.portaInicia, self.portaFinal + 1)
                    }
            for future in concurrent.futures.as_completed(futures):
                porta = futures[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"Erro escanear a prota {porta}: {e}")


    def scan_with_threads(self,fila , porta):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.settimeout(3)
            
            resultado = tcp.connect_ex((self.target, porta))
            if resultado == 0:
                try:
                    servico = socket.getservbyport(porta)
                except OSError:
                    servico = "Desconhecido"
                fila.put(f"Porta {porta} aberta rodando {servico}")
                tcp.close()
        except socket.timeout :
            self.fila.put(f"Porta {porta} filtrada rodando unknow")
        except socket.error as e:
            self.fila.put(f"Erro ao conectar com a porta {porta}: {e}")
               

    def getfila(self):
        return self.fila
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

    def set_qts_threads(self, qts_threads):
        self.max_threads = qts_threads -1
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

  

