#!/bin/python3
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
      """ configurações iniciais da janela"""
      self.root = root
      self.root.title("Simplescan")
      self.root.geometry('1000x400')
      frame = tk.Frame(root)
      frame.pack(pady=5)
      

      """criação de todos os componentes usados na aplicação como:
         input de alvo (txt_host)
         label do ip (lbl_host)
         area de informações das buscas (log_area)
         butão para escanear (btn_scan)
         input de portas (inp_int_port, inp_end_port)
         label das portas (lbl_ports)
         """
      self.lbl_host = tk.Label(frame, text="IP:")
      self.txt_host = tk.Entry(frame) 
      self.log_area = scrolledtext.ScrolledText(frame, width=60, height=10, state='disabled')
      self.btn_scan = tk.Button(frame,text="Scan", command=self.iniciar_scanner)
      self.lbl_ports = tk.Label(frame, text="Portas: ")
      self.inp_init_port = tk.Entry(frame)
      self.inp_end_port = tk.Entry(frame)
      self.lbl_threads = tk.Label(frame, text="Threads:")
      self.qts_threads = tk.Entry(frame)

      """ espaçamentos da interface grafica, estruturada usando grid, sendo cada linha e coluna um componten"""
      self.lbl_host.grid(row=0, column=0)
      self.txt_host.grid(row=0, column=1)
      self.btn_scan.grid(row=0, column=2)
      self.log_area.grid(row=3, column=3)
      self.lbl_ports.grid(row=1, column=0)
      self.inp_init_port.grid(row=1, column=1)
      self.inp_end_port.grid(row=1, column=2)
      self.lbl_threads.grid(row=2, column=0)
      self.qts_threads.grid(row=2, column=1)

      """ Inicializando o scanner como nulo"""
      self.scanner = scanner.Scanner('0.0.0.0', 0, 0, 50)


   """ =================Metodos=================
   metodo que inicia os threads do scan
   e testa se os inputs foram preenchidos
   """
   def iniciar_scanner(self):
      target = self.txt_host.get().strip()
      init_port = self.inp_init_port.get().strip()
      end_port = self.inp_end_port.get().strip()
      qts_threads = self.qts_threads.get().strip()
      if not target:
         self.log("Traget nao setado")
         return
      if (not init_port or not end_port):
         self.log("Portas não setadas")
         return
      if len(qts_threads) != 0:
         qts_threads = int(qts_threads)
      init_port = int(init_port)
      end_port = int(end_port)

      self.scanner.set_target(target)
      self.scanner.set_initial_port(init_port)
      self.scanner.set_end_port(end_port)
      self.scanner.set_qts_threads(qts_threads)

      thread = threading.Thread(target=self.executar_scan)
      thread.start()

   """executar_scan recebe as listas das portas do scan e printa os resultados formatados"""
   def executar_scan(self):

      self.scanner.scannear()
      self.log(f"alvo {self.scanner.get_target()}:")
      fila = self.scanner.getfila()
      while not fila.empty():
         self.log(fila.get())
         fila.task_done()


   """log(mensagem) mostra as informação no componente log_area"""
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
