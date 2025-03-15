import tkinter as tk
from tkinter import  scrolledtext
import scanner
import threading
import logging
""" Classe ScannApp é oque engloba interface e o scanner e printa os resultados
   root = é a interface root do tkinter
   lbl_host = a lable para inserir o alvo do scan
   log_area = area onde vai sair o resultado

"""
class ScannApp:
   def __init__(self, root):
      self.root = root
      self.root.title("Simplescan")
      self.root.geometry('1000x400')
      frame = tk.Frame(root)

      frame.pack(pady=5)
      # criando os inputs
      self.lbl_host = tk.Label(frame, text="IP:")
      self.txt_host = tk.Entry(frame) 
      self.log_area = scrolledtext.ScrolledText(frame, width=60, height=10, state='disabled')
      self.btn_scan = tk.Button(frame,text="Scan", command=self.iniciar_scanner)
      self.lbl_ports = tk.Label(frame, text="Portas: ")
      self.inp_init_port = tk.Entry(frame)
      self.inp_end_port = tk.Entry(frame)


      self.lbl_host.grid(row=0, column=0)
      self.txt_host.grid(row=0, column=1)
      self.btn_scan.grid(row=0, column=2)
      self.log_area.grid(row=3, column=3)
      self.lbl_ports.grid(row=1, column=0)
      self.inp_init_port.grid(row=1, column=1)
      self.inp_end_port.grid(row=1, column=2)

      self.scanner = scanner.Scanner('0.0.0.0', 0, 0)

   """metodo que inicia os threads do scan"""
   def iniciar_scanner(self):
      target = self.txt_host.get().strip()
      init_port = self.inp_init_port.get().strip()
      end_port = self.inp_end_port.get().strip()

      if not target:
         self.log("Traget nao setado")
         return
      if (not init_port or not end_port):
         self.log("Portas não setadas")
         return
      init_port = int(init_port)
      end_port = int(end_port)


      print("testes dos inputs")
      self.scanner.set_target(target)
      self.scanner.set_initial_port(init_port)
      self.scanner.set_end_port(end_port)

      thread = threading.Thread(target=self.executar_scan)
      thread.start()

   def executar_scan(self):

      portas_abertas = self.scanner.scannear()
      if(portas_abertas == None):
         self.log("Nenhuma porta encontrada!")
         return
      for porta, servico in portas_abertas:
         self.log(f"Porta {porta} rodando {servico}\n")

   def log(self, mensagem):
      self.log_area.config(state='normal')
      self.log_area.insert(tk.END, mensagem + '\n')
      self.log_area.config(state='disabled')

def main():
   root = tk.Tk()
   logging.basicConfig(filename='myapp.log', level=logging.INFO)
   logging.info('Start')
   app = ScannApp(root)
   root.mainloop()
   logging.info('Finished')

if __name__ == '__main__':
   main()
