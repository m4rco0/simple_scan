#!/bin/python3
import tkinter as tk
from PIL import Image, ImageTk 
import logging
""" Classe ScannApp é oque engloba interface e o scanner e printa os resultados
   root = é a interface root do tkinter
   lbl_host = a lable para inserir o alvo do scan
   log_area = area onde vai sair o resultado
    __________
   |__tittle__|
   |    |     |
   |  l |  r  |
   |____|_____|
   |__bottom__|

"""
class ScannApp:
   def __init__(self, root):
      """ configurações iniciais da janela"""
      self.root = root
      self.root.title("Simplescan")
      self.root.geometry('942x801')

      self.BG_IMG = ImageTk.PhotoImage(Image.open("./src/ui/background.png"))
      #------- cores utilizadas --------
      self.BG_COLOR = "#232C25"
      self.INPUT_BORDER = "#575454"
      self.FG_COLOR = "#FFFFFF"
      self.FONT_LABEL = ("Consolas", 15)
      self.FONT_TITLE = ("Consolas", 22, "bold")
      self.WAVE_COLOR = "#011207"

      background_label  = tk.Label(root, image=self.BG_IMG)
      background_label.place(x=0, y=0, relwidth=1, relheight=1)
      self.root.configure()

def main():
   root = tk.Tk()
   logging.basicConfig(filename='myapp.log', level=logging.INFO)
   logging.info('Start')
   app = ScannApp(root)
   root.mainloop()
   logging.info('Finished')

if __name__ == '__main__':
   main()
