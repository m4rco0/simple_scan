#1/usr/bin/python3
import argparse
from art import banner
from colors import *
import scanner
def main():
    """ Configuração do cli do programa """
    parser = argparse.ArgumentParser(
                      prog="SimpleScan",
                      description="Scanner de rede para forma de estudos sobre alguma rede",
                      epilog="ta foda msm"
                      )
    parser.add_argument("ip", help="Ip do host que vai ser escaneado")
    parser.add_argument("-p", "--ports", help="Utilize o range de portas que vai buscar 0-80 ou apenas uma porta 80")
    args =parser.parse_args()

    banner()
    """ Inicializando variaveis para o scann"""
    ip = args.ip
    startPort = 0
    endPort = 80
    """ Testando se precisa scanear 1 porta ou um range de portas"""
    if args.ports != None:
        if len(args.ports.split("-")) == 1:
            endPort = int(args.ports)
            startPort = endPort
        elif(len(args.ports.split("-")) == 2):
            startPort, endPort = args.ports.split("-")
            startPort = int(startPort)
            endPort = int(endPort)
        else:
            print(RED + "[-] ERRO NA FORMATAÇÃO DO RANGE DE PORTAS")
            return
    scan = scanner.Scanner(ip, startPort, endPort)
    scan.scannear()

        
if __name__ == '__main__':
    main()
