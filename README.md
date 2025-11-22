# Simple Scan.

- [X] Verificar as portas abertas e fechadas em cada endereço IP.  
- [X] Transformando o scan de forma assyncrona.
- [x] argumentos no comando.  
- [x] Identificar os serviços em execução em cada porta aberta.
- [x] Pegar banner de serviços
- [ ] Verificar se há vulnerabilidades conhecidas nos serviços em execução.
- [x] Alternativa grafica do scan

```
├── README.md
├── requirements.txt   
├── run_cli.py        ==> arquivo para rodar no terminal
├── run_gui.py        ==> arquivo para rodar na interface grafica
└── src
    ├── assets
    │   ├── fonts
    │   │   ├── Jaini-Regular.ttf    ==> Fonte usada na interface, instalar antes
    │   │   └── NotoSansSyriacWestern-VariableFont_wght.ttf
    │   └── images
    │       └── background.png
    ├── core        ==> Arquivos principais para rodar o scanner
    │   ├── banner_grapping.py
    │   ├── __init__.py
    │   └── scanner.py
    ├── __init__.py
    ├── interface    ==> interfaces que utilizam o core como base
    │   ├── cli.py
    │   ├── gui.py
    │   └── __init__.py
    └── utils      ==> utilitarios como cores e banner do scann
        ├── art.py
        ├── colors.py
        ├── __init__.py
```
## Como usar
Primeiro o programa necessita que o usuario esteja na pasta `src/`. Utilizando se das duas formas abaixo:
## Sem interface grafica
### Executando o arquivo `simple_scan.py` com argumentos. 

Exemplo:
```bash
python3 run_cli.py 192.168.0.1 -p 21-3000
```
Sixtaxe:
`python3 run_cli.py <ip> <porta-inicial> -p <porta-final>`

<img width="936" height="309" alt="Image" src="https://github.com/user-attachments/assets/cf49d709-ae85-46ec-931a-eb95bf63bf7b" />
## Com interface grafica
Só precisa executar o codigo no src

```bash
python3 run_gui.py 
```
<img width="989" height="843" alt="Image" src="https://github.com/user-attachments/assets/c647edeb-4a22-49b7-b502-1093ad096588" />

