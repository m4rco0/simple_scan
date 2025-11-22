#!/bin/python3
import tkinter as tk
import tkinter.font as tkFont
from tkinter import scrolledtext
import threading
import src.core.scanner as scanner
from src.core.banner_grapping import pegar_banner
from PIL import Image, ImageTk
class ScannApp:
   def __init__(self, root):
      self.root = root
      self.root.title("Simplescan")
      self.root.geometry('942x801')
      self.root.resizable(False,False)
      
      self._setup_colors()
      self._create_background()
      self.root.configure()
      self._create_widgets()
      self.main_painel.pack()
      self.scanner = scanner.Scanner('0.0.0.0', 0, 0, 50) 

   def _setup_colors(self):
      """ Define as cores e fontes e tamanhos utilizado na applicação"""
      self.BG_COLOR = "#232C25"
      self.INPUT_BORDER = "#575454"
      self.FG_COLOR = "#FFFFFF"
      self.FONT_LABEL = tkFont.Font(family="Jaini", size= 16)
      self.FONT_TITLE = tkFont.Font(family="Jaini", size= 22) 
      self.WAVE_COLOR = "#011207"
      self.WINDOW_WIDTH = 942
      self.WINDOW_HEIGHT = 801 

   def _create_background(self):
      """ cria que vai carregar a foto de fundo e colocar em uma label, caso não consiga, iniciará com apenas a cor de fundo"""
      try:
         self.BG_IMG = ImageTk.PhotoImage(Image.open("./src/assets/images/background.png"))
         self.background_label  = tk.Label(self.root, image=self.BG_IMG)
         self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
      except Exception as e:
         print(f"Erro ao carregar imagem de fundo: {e}")
         self.root.configure(bg=self.BG_COLOR)

   def _create_widgets(self):
      """ cria e organiza os widgets utilizados na tela principal"""
      self.tittle_lbl = tk.Label(self.root, text="Simplescan", font=self.FONT_TITLE, bg=self.BG_COLOR, fg=self.FG_COLOR)
      self.tittle_lbl.pack()

      # ------- Painel principal
      self.main_painel = tk.Frame(self.root, bg=self.BG_COLOR, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
      self.main_painel.columnconfigure(0, weight=1)
      self.main_painel.columnconfigure(1, weight=1)
      self.main_painel.rowconfigure(0, weight=1)
      self.main_painel.rowconfigure(1, weight=1)

      # --------- Paineis internos ------------
      self._setup_inputsPainel()
      self._setup_resultsPainel()

   def _setup_inputsPainel(self):
      """ Cria o painel que vai armazenar os campos a serem inseridos, que vai ficar a esquerda"""

      #criação do painel
      inputs_panel = tk.Frame(self.main_painel, width=443, height=469, bg=self.BG_COLOR)
      inputs_panel.grid(row=0, column=0, padx=10, sticky=tk.NSEW)
      inputs_panel.grid_columnconfigure(1, weight=1)

      # criação das labels
      inputs_labels = ["ip:" , "Porta inicial:", "Porta final:", "Threads:"]
      self.campos = {}
      for i, text in enumerate(inputs_labels):
         lbl = tk.Label(inputs_panel, text=text, bg=self.BG_COLOR, fg= self.FG_COLOR, font=self.FONT_LABEL)
         lbl.grid(row=i, column=0, sticky=tk.EW)

         # Cria campos para receber valores
         campo = tk.Entry(inputs_panel, font=self.FONT_LABEL, bg=self.FG_COLOR, fg=self.WAVE_COLOR, relief="flat")
         campo.grid(row=i, column=1, sticky=tk.EW, padx=5, pady=10)
         self.campos[text] = campo

      # Atribui as entradas a variáveis de instância para acesso futuro 
      self.txt_host = self.campos["ip:"]
      self.init_port = self.campos["Porta inicial:"]
      self.final_port = self.campos["Porta final:"]
      self.qts_threads = self.campos["Threads:"]

   def _setup_resultsPainel(self):
      """ Cria o painel dos resultados do scan."""
      resultado_panel = tk.Frame(self.main_painel, width=425, height=482, bg="red")
      resultado_panel.grid(row=0, column=1, sticky=tk.NSEW, padx=(20, 20))
      resultado_panel.grid_rowconfigure(1, weight=1)
      resultado_panel.grid_columnconfigure(0, weight=1)

      self.logArea = scrolledtext.ScrolledText(resultado_panel, width=60, height=30, state='disabled')
      self.logArea.grid(row=1,column=0)
      self._create_scan_btn()


   def _create_scan_btn(self):
      """ cria o botão de scan"""
      button_scan = tk.Button(self.main_painel, font=self.FONT_LABEL,  text="Scannear!", command=self.iniciar_scan)
      button_scan.grid(row=1, column=0, columnspan=2, pady=10)

   def iniciar_scan(self):
      alvo = self.txt_host.get().strip()
      init_port = int(self.init_port.get())
      final_port = int(self.final_port.get())
      qts_threads = int(self.qts_threads.get().strip())

      if not alvo:
         self.log("Alvo do scan não foi inserido!")
         return 
      
      if not (init_port or final_port):
         self.log("Portas não foram setadas")
         init_port = 0 
         final_port = 100

      if qts_threads <= 0:
         self.log("Não pode threads negativo")
         return 

      self.log(f" [+] Iniciando scan {alvo} [{init_port}-{final_port}]")

      self.scanner.set_target(alvo)
      self.scanner.set_initial_port(init_port)
      self.scanner.set_end_port(final_port)
      self.scanner.set_qts_threads(qts_threads)

      thread = threading.Thread(target=self.executar_scan)
      thread.start()

   def executar_scan(self):
      self.scanner.scannear()
      self.log(f"alvo {self.scanner.get_target()}:")
      fila = self.scanner.getfila()
      while not fila.empty():
         self.log(fila.get())
         fila.task_done()



     


   def log(self, mensagem):
      self.logArea.config(state='normal')
      self.logArea.insert(tk.END, mensagem + '\n')
      self.logArea.config(state='disabled')
def main():
   root = tk.Tk()
   app = ScannApp(root)
   root.mainloop()
