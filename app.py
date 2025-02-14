from tkinter import *
import pyautogui
import time
from datetime import datetime

#Cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

# Configurando janela --------------------------------
janela = Tk()
janela.title('')

photo = 'Keyboard.ico'
janela.iconbitmap(photo)

janela.geometry('300x190')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

# Definindo variaveis globais
global tempo
global intervalo
global contador
global rodar

# Define o intervalo de tempo (em segundos) entre cada batimento de tecla
tempo = ''
intervalo = 30000   # tempo em milissegundos
contador = 1
rodar = True

#Inciar a contagem
def iniciar():
    def contar():
        if rodar:
            global tempo
            global contador

            DataHoraAgora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            # Simula o batimento da tecla Shift
            pyautogui.press('shift')
            print(f"Tecla 'Shift' pressionada.({contador}) - ({DataHoraAgora})")
            label_app['text'] = f"Tecla 'Shift' pressionada.({contador})"
            label_tempo['text'] = f"{DataHoraAgora}"
            contador += 1
            label_tempo.after(intervalo, contar)
    contar()

# Funcao para iniciar o app
def start():
    global rodar
    rodar = True
    iniciar()

# Funacao para parar app
def stop():
    global rodar
    rodar = False
    label_app['text'] = "tecle Start para iniciar"
    label_tempo['text'] = ""



# Criando labels --------------------------------
label_app = Label(janela, text='tecle Start para iniciar',  font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, fon=('Times 18 bold'), bg=cor1, fg=cor6)
label_tempo.grid(row=0, column=0, sticky=NSEW, padx=20, pady=38)
#label_tempo.place(x=55, y=35)

# Criando Botões --------------------------------
bt_Start = Button(janela, command=start, text='Start', width=10, height=2, bg=cor1, fg=cor2, fon=('Ivy 8 bold'), relief='raised', overrelief='ridge')
bt_Start.place(x=20, y=130)

bt_Stop = Button(janela, command=stop, text='Stop', width=10, height=2, bg=cor1, fg=cor2, fon=('Ivy 8 bold'), relief='raised', overrelief='ridge')
bt_Stop.place(x=190, y=130)

janela.mainloop()
