"""Banner usado para printar"""
from colors import *
VERSION=0.2
def banner():
    print(RED + " \
    .s5SSSs. "+ GREEN + " .s5SSSs.  \n"+RED+"\
          SS. "+GREEN +"      SS. \n"+RED +"\
    sS    `:; "+GREEN +" sS    `:; \n"+ RED +"\
    SS        "+GREEN +"SS        \n"+ RED +"\
    `:;;;;.   "+GREEN +"`:;;;;.   \n"+ RED +"\
          ;;.   "+GREEN +"    ;;. \n"+ RED +"\
          `:;    "+GREEN +"   `:; \n"+ RED +"\
    .,;   ;,. "+GREEN +".,;   ;,. \n"+ RED +"\
    `:;;;;;:' "+GREEN +"`:;;;;;:' " + END, VERSION)
