#This program was written in French, you may translate it if you do not speak French.


from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter.constants import DISABLED, END, FALSE


def receive():
    stop = False
    while True and not stop:
        try:
            msg = clientSocket.recv(BUFFSIZE).decode('utf8')
            msgList.insert(tkinter.END,msg)
        except OSError:
            fermer()
            break

def envoyer(event=None):
    msg = myMsg.get()
    myMsg.set("")
    clientSocket.send(bytes(msg,'utf8'))
    if msg == "exit":
        clientSocket.close()
        fermer()
        top.quit()

def fermer(event=None):
    myMsg.set("'exit'")
    envoyer()
    top.destroy()


def blocage_entrer(event):
	entryField.config(state=DISABLED)

if __name__ == '__main__':
    top = tkinter.Tk()
    top.configure(bg="lightgray")
    top.title('ChatRoom')
    top.geometry("400x500")
    top.resizable(width=FALSE, height=FALSE)
    messageFrame = tkinter.Frame(top)
    scrollbar = tkinter.Scrollbar(messageFrame)

    msgList = tkinter.Listbox(top,bd=0, bg="white", height="8", width="55", font="Arial",)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y,)
    msgList['yscrollcommand'] = scrollbar.set
    msgList.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msgList.pack(fill = tkinter.X)
    msgList.configure(bg="lightblue")
    messageFrame.pack()

    myMsg = tkinter.StringVar()
    myMsg.set("")

    entryField = tkinter.Entry(top,textvariable = myMsg)
    entryField.bind("<Return>", envoyer)
    entryField.pack()
    entryField.configure(bg="gray")
    sendButton= tkinter.Button(top,font=30, text="Send", width="12", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=envoyer)
    # sendButton= tkinter.Button(top,font=30, text="Send", width="12", height=5,  bd=0, bg="#FFBF00", activebackground="#FACC2E", command=send)
    
    
    scrollbar.place(x=376,y=6,height=386)
    entryField.place(x=128, y=401, height=90, width=265)
    sendButton.place(x=6, y=401, height=90)
    msgList.place(x=6,y=6, height=386, width=370)

    top.protocol("WM_DELETE_WINDOW", fermer)
    client={'1':'127.0.0.1','2':'127.0.0.2','3':'127.0.0.3','4':'127.0.0.3','5':'10.56.193.2','6':"10.56.193.3",'7':'10.56.193.4','8':input("ecrire votre ADDRESS IP personnaliser(Si vous n'avez pas un Adresse IP personnaliser veuiller sauter cette section en touchant entrer!) ? ")}
    HOST = client[(input
                ("Choisisez des options presenter:  1) serveur_interieur_de_etude_nsi , 2) serveur_interieur_de_etude_svt   ,    3) serveur_interieur_de_etude_eps   ,     4) serveur_interieur_de_etude_philo   ,    5) serveur_aman_exterieur   ,    6) serveur_yosi_exterieur   ,   7) serveur_semir_exterieur   ,    8) adresse IP personnaliser? "))]
    PORT = 5545

    BUFFSIZE = 1024
    ADDR = (HOST, PORT)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(ADDR)

    
    receiveThread = Thread(target=receive)
    receiveThread.start()
    tkinter.mainloop()  
    receiveThread.join()
