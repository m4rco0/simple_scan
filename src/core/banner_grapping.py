from telnetlib import Telnet
import socket
import src.utils.colors as colors

def pegar_banner(host, porta, proto):
    # Socket utilizado apra pegar o banner
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.settimeout(5)

    try:
        #tenta conexão
        tcp.connect((host, porta))
        
        #enviar entrada deacordo com o serviço rodando
        if proto == 'http':
            request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: Mozilla/5.0\r\nConnection: close\r\n\r\n"
            tcp.send(request.encode())
        

        # recebendo os bytes do serviço
        banner_bytes = tcp.recv(3072)
        banner_limpo = banner_bytes.decode('utf-8', errors='ignore').strip().split('\n')
        
        # --------------extração de protocolos---------------------
        if proto == 'http':
            for linha in banner_limpo:
                if linha.lower().startswith('server:'):
                    print(linha.lower())
                    return linha.split(':', 1)[1].strip()
            return "x.x.x"
        

        elif proto == 'ftp':
            # Geralmente o ftp tem o formato de numero e versão
            # 220 (vsFTPd 2.3.4) => [220], [vsFTPd 2.3.4], []
            version_ftp = banner_limpo[0].split('(')[1].split(')')[0].strip()
            return version_ftp
        
        elif proto == 'ssh':
            #exemplo de banner
            # SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
            return banner_limpo[0]
        
        elif proto == 'telnet':
            return banner_bytes if banner_bytes else "Linux telnet"
        elif proto == 'smtp':
            #Servidor de emails utilizando normalment Postfix
            #
            
            return banner_limpo[0].strip()
        else:
            return banner_bytes if banner_bytes else "Nenhum dado recebido"
        
    except socket.timeout as e:
        print(f"Porta {porta}: {e}")
    except socket.error as e:
        print(f"Não foi possivel conectar na porta {porta}: {e}")
    finally:
        tcp.close()
