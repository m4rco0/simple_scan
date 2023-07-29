# Simple Scan.  
- [X] Verificar as portas abertas e fechadas em cada endereço IP.  
- [ ] Transformando o scan de forma assyncrona.
- [x] argumentos no comando.  
- [x] Identificar os serviços em execução em cada porta aberta.  
- [ ] Verificar se há vulnerabilidades conhecidas nos serviços em execução.

## Como usar
Você pode usar a ferramenta de duas maneiras:

### 1. Executando o arquivo `main.py` diretamente
```bash
python3 main.py
```
Esta é a maneira mais simples de usar a ferramenta, um modo interativo.

### 2. Executando o arquivo `main.py` com argumentos
Exemplo:
```bash
python3 main.py 192.168.0.1 21-3000
```
Sixtaxe:
`python3 main.py <ip> <porta-inicial>-<porta-final>`

<div aling= "center">
  <img src="https://github.com/m4rco0/simple_scan/assets/54968908/52aa130f-518d-4cd3-b409-7a613269d7fc" width= "800px">
</div>
