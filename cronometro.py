from tkinter import*

bg1="black"
bg2="white"
bg3="red"
bg4="green"
bg5="gray"
bg6="blue"

janela = Tk()

janela.title("Cronometro")
janela.geometry("600x480")
janela.config(bg=bg1)
janela.iconphoto(False,PhotoImage(file="cronometro.png"))
janela.resizable(width=False,height=False)

#definindo variaveis globais

global tempo
global rodar
global contador
global limitador

limitador = 59

tempo = "00:00:00"
rodar = False
contador = -5


def iniciar():
    global tempo
    global contador
    global limitador
    
    if(rodar):
        #antes do cronometro começar
        if(contador<=-1):
            inicio = "Começando em " + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] ="Arial 10"
        #rodando cronometro
        else:
            label_tempo['font'] = "Times 50 bold"

            temp = str(tempo)
            h,m,s = map(int,temp.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if(s>=limitador):
                contador = 0
                m+=1

            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            #Atualizando os valores atuais
            temp = str(h[-2:])+":"+str(m[-2:])+":"+str(s[-2:])
            label_tempo['text'] = temp
            tempo = temp
             
        label_tempo.after(1000,iniciar)    
        contador +=1

#função iniciar
def start():
    global rodar
    rodar = True
    iniciar()

#função pausar
def pausar():
    global rodar
    rodar = False

#função reiniciar
def reiniciar():
    global contador
    global tempo

    #reiniciando tempo e o contador
    
    contador = 0
    tempo = "00:00:00"
    label_tempo['text'] = tempo

#Labels

label_app = Label(janela, text="Cronometro" ,font = ("Arial 10"), bg = bg1, fg = bg2)
label_app.place(x=20,y=10)

label_tempo = Label(janela, text = tempo ,font = ("Times 50 bold"), bg = bg1, fg = bg2)
label_tempo.place(x=20,y=30)

#Criando botões

botao_iniciar = Button(janela,command = start,text="Iniciar",width=10,height=2,bg=bg1,fg=bg2,font = ("Ivy 8 bold"),relief = "raised")
botao_iniciar.place(x = 20,y = 130)

botao_pausar = Button(janela,command = pausar,text="Pausar",width=10,height=2,bg=bg1,fg=bg2,font = ("Ivy 8 bold"),relief = "raised")
botao_pausar.place(x = 105,y = 130)

botao_reiniciar = Button(janela,command = reiniciar,text="Reiniciar",width=10,height=2,bg=bg1,fg=bg2,font = ("Ivy 8 bold"),relief = "raised")
botao_reiniciar.place(x = 190,y = 130)

janela.mainloop()
