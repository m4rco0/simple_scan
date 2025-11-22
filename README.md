# Simple Scan.
<img width="200" height="400" alt="Image" src="https://github.com/user-attachments/assets/6a249cd5-a822-4451-93f0-0ba4e6a77fb0" />


### ✨ Funcionalidades
* [x] **Scan de Portas:** Verifica portas comuns (ex: 21, 22, 80, 443) ou intervalos personalizados.
* [x] **Multithreading:** Utiliza threads para realizar varreduras simultâneas, reduzindo drasticamente o tempo de espera.
* [x] **Identificação de Serviços:** Tenta identificar qual serviço está rodando na porta descoberta (Banner Grabbing).
* [x] **Interface:** [Mencione se é via Linha de Comando (CLI) ou Interface Gráfica (Tkinter)].
* [ ] **Verificar Vulns** (Em andamento ...)
## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Socket:** Para conexões de rede de baixo nível.
* **Threading:** Para paralelismo e velocidade.
* **pillow:** Para mostrar background do gui.


## 🎃 Estrutura dos arquivos
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
## 🚀 Como Executar
### Pré-requisitos
- Python instalado.
- pip instalado.

### Instalação
1. Clonar o repositorio:
```bash
git clone https://github.com/m4rco0/simple_scan.git
```
2. Entre no arquivo:
```bash
cd simple_scan
```
3. Instale as dependências (se houver):
```bash
pip install -r requirements.txt
```
ou
```bash
pip install pillow
```
## Uso

Os programas a serem executados, devem ser apenas `run_cli.py` e `run_gui.py` executados nas pastas `simple_scan/` que é a raiz do projeto. Utilizando se das duas formas abaixo:
## Sem interface grafica
### Executando o arquivo `run_cli.py` com argumentos. 

Exemplo:
```bash
python3 run_cli.py 192.168.0.1 -p 21-3000
```
<img width="936" height="309" alt="Image" src="https://github.com/user-attachments/assets/cf49d709-ae85-46ec-931a-eb95bf63bf7b" />

Sixtaxe:

<img width="870" height="305" alt="image" src="https://github.com/user-attachments/assets/f3586ad2-115b-4cfd-a9a7-f0fe3b5b4e0b" />



## Com interface grafica
Só precisa executar o codigo no src

```bash
python3 run_gui.py 
```
<img width="989" height="843" alt="Image" src="https://github.com/user-attachments/assets/c647edeb-4a22-49b7-b502-1093ad096588" />

