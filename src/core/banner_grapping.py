import socket
import src.utils.colors as colors
def pegar_banner(host, porta):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.settimeout(5)
    try:
        tcp.connect((host, porta))

        if porta in [80, 8080, 8000, 443]:
            request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\n\r\n"
            tcp.send(request.encode())

        banner_bytes = tcp.recv(1024)

        if banner_bytes:
            banner_limpo = banner_bytes.decode('utf-8', errors='ignore').split('\n')
            return banner_limpo[0]

    except socket.timeout:
        print(f" {colors.RED
              }  [-] Conexão na porta {porta} expirou {colors.END}")
    except socket.error as e:
        print(f"Não foi possivel conectar na porta {porta}: {e}")
    finally:
        tcp.close()

