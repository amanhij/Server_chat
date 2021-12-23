#This program was written in French, you may translate it if you do not speak French.


from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients  = {}
addresses = {}
serveur={'1':'127.0.0.1','2':'127.0.0.2','3':'127.0.0.3','4':'127.0.0.3','5':'10.56.193.2','6':"10.56.193.3",'7':'10.56.193.4','8':input("ecrire votre ADDRESS IP personnaliser(Si vous n'avez pas un Adresse IP personnaliser veuiller sauter cette section en touchant entrer!) ? ")}
HOST = serveur[(input
                ("Choisisez des options presenter:  1) serveur_interieur_de_etude_nsi , 2) serveur_interieur_de_etude_svt   ,    3) serveur_interieur_de_etude_eps   ,     4) serveur_interieur_de_etude_philo   ,    5) serveur_aman_exterieur   ,    6) serveur_yosi_exterieur   ,   7) serveur_semir_exterieur   ,    8) adresse IP personnaliser? "))]
PORT = 5545
BUFFSIZE = 1024
ADDR = (HOST,PORT)
SERVER = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)


def acceptelesconnexionsvenant():
    while True:
        client, clientAddress = SERVER.accept()
        print("%s:%s est connecter." % clientAddress)
        client.send(bytes("Bienvenue au ChatRoom, ecrivez votre nom Ci dessous et clicker entrer", "utf8"))
        addresses[client] = clientAddress
        Thread(target=occupClient, args=(client,)).start()

def occupClient(client):
    name = client.recv(BUFFSIZE).decode("utf8")
    client.send(bytes("Bonjour %s, ecrit 'exit' pour quitter le chat" % name,'utf8'))
    msg = '%s nous a joint' % name
    envoyer(bytes(msg, 'utf8'))
    clients[client] = name
    while True:
        msg = client.recv(BUFFSIZE)
        if msg != bytes("'exit'", "utf8"):
            envoyer(msg, name+": ")
        else:
            client.send(bytes("'exit'", "utf8"))
            client.close()
            del clients[client]
            envoyer(bytes("%s a n'est plus dans le chat." % name, "utf8"))
            break

def envoyer(msg,prefix = ""):
    for client in clients:
        client.send(bytes(prefix,'utf8')+msg)


if __name__ == "__main__":
    SERVER.listen(5)  # Listens for 5 connections at max.
    print("Waiting for a new connection...")
    ACCEPT_THREAD = Thread(target=acceptelesconnexionsvenant)
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()
