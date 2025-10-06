# Simple Scan.  
- [X] Verificar as portas abertas e fechadas em cada endereço IP.  
- [X] Transformando o scan de forma assyncrona.
- [x] argumentos no comando.  
- [x] Identificar os serviços em execução em cada porta aberta.  
- [ ] Verificar se há vulnerabilidades conhecidas nos serviços em execução.
- [x] Alternativa grafica do scan

## Como usar
Primeiro o programa necessita que o usuario esteja na pasta `src/`. Utilizando se das duas formas abaixo:
## Sem interface grafica
### Executando o arquivo `simple_scan.py` com argumentos. 

Exemplo:
```bash
python3 simple_scan.py 192.168.0.1 -p 21-3000
```
Sixtaxe:
`python3 main.py <ip> <porta-inicial> -p <porta-final>`

## Com interface grafica
Só precisa executar o codigo no src

```bash
python3 simple_scan_ui.py 
```
![Image](https://github.com/user-attachments/assets/a62b8d68-1bb1-4a22-b070-f04871d5ff5e)

