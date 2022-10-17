#Importation des bibliothèques nécessaires
from tkinter import*
import tkinter as tk
import tkinter.font
from math import *


#Définition des fonctions qui seront associées aux pièces sur le plateau de jeu (les pièces étant codées en tant que boutons)

def piece1():
    bpiece[1].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=1
    etat[1]=False
    phase2()

def piece2():
    bpiece[2].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=2
    etat[2]=False
    phase2()

def piece3():
    bpiece[3].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=3
    etat[3]=False
    phase2()

def piece4():
    bpiece[4].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=4
    etat[4]=False
    phase2()

def piece5():
    bpiece[5].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=5
    etat[5]=False
    phase2()

def piece6():
    bpiece[6].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=6
    etat[6]=False
    phase2()

def piece7():
    bpiece[7].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=7
    etat[7]=False
    phase2()

def piece8():
    bpiece[8].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=8
    etat[8]=False
    phase2()

def piece9():
    bpiece[9].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=9
    etat[9]=False
    phase2()

def piece10():
    bpiece[10].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=10
    etat[10]=False
    phase2()

def piece11():
    bpiece[11].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=11
    etat[11]=False
    phase2()

def piece12():
    bpiece[12].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=12
    etat[12]=False
    phase2()

def piece13():
    bpiece[13].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=13
    etat[13]=False
    phase2()

def piece14():
    bpiece[14].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=14
    etat[14]=False
    phase2()

def piece15():
    bpiece[15].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=15
    etat[15]=False
    phase2()

def piece16():
    bpiece[16].place(x=280, y=390)
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="normal")
    global choix_piece
    choix_piece=16
    etat[16]=False
    phase2()


#Définition des fonctions qui seront associées aux cases sur le plateau de jeu (les cases étant codées en tant que boutons)

def case1():
    bcase[1].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=170, y=77)
            bpiece[i].configure(bg="white")
            etatcase[1]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case2():
    bcase[2].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=245, y=77)
            etatcase[2]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case3():
    bcase[3].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=320, y=77)
            bpiece[i].configure(bg="white")
            etatcase[3]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case4():
    bcase[4].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=395, y=77)
            etatcase[4]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case5():
    bcase[5].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=170, y=152)
            etatcase[5]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case6():
    bcase[6].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=245, y=152)
            bpiece[i].configure(bg="white")
            etatcase[6]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case7():
    bcase[7].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=320, y=152)
            etatcase[7]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case8():
    bcase[8].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=395, y=152)
            bpiece[i].configure(bg="white")
            etatcase[8]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case9():
    bcase[9].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=170, y=227)
            bpiece[i].configure(bg="white")
            etatcase[9]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case10():
    bcase[10].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=245, y=227)
            etatcase[10]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case11():
    bcase[11].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=320, y=227)
            bpiece[i].configure(bg="white")
            etatcase[11]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case12():
    bcase[12].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=395, y=227)
            etatcase[12]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case13():
    bcase[13].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=170, y=302)
            etatcase[13]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case14():
    bcase[14].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=245, y=302)
            bpiece[i].configure(bg="white")
            etatcase[14]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case15():
    bcase[15].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=320, y=302)
            etatcase[15]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()

def case16():
    bcase[16].place_forget()
    for i in range(1,17):
        bcase[i].configure(state="disabled")
        if (choix_piece==i) :
            bpiece[i].place(x=395, y=302)
            bpiece[i].configure(bg="white")
            etatcase[16]=i
        if (etat[i]):
            bpiece[i].configure(state="normal")
    checkwin()


#Définition de la fonction associée au bouton "Jouer" du menu
def play():
    canvas.destroy()
    jouer.destroy()
    support.destroy()
    game()


#Définition de la fonction associée au bouton "Menu" du plateau de jeu
def menu():
    canvas.destroy()
    restart.destroy()
    retour.destroy()
    quitter.destroy()
    main()


#Définition de la fonction associée au bouton "Recommencer" du plateau de jeu
def reset():
    canvas.destroy()
    retour.destroy()
    restart.destroy()
    game()


#Définition de la fonction qui affiche la fenêtre contenant les règles
def rules():
    global tutorial
    tutorial = tk.Toplevel(fenetre)
    tutorial.title('Notice Quarto')
    tutorial.iconbitmap("icon.ico")
    tutorial.resizable(0,0)
    can = Canvas(tutorial, height=618, width=400)
    can.create_image(200,309, image=regles)
    can.pack()
    tutorial.mainloop()


#Définition de la fonction qui crée la fenêtre du menu
def main():
    global canvas
    canvas = Canvas(fenetre, width=600, height=480, bg=bleu)
    canvas.create_image(300, 250, image=logo)
    canvas.pack()
    tour = canvas.create_text(300,100, fill="black",font="Helvetica", text="Bienvenue sur Quarto")
    global jouer
    jouer = Button(fenetre, text='Jouer', command = play)
    global quitter
    quitter = Button(fenetre, text='Quitter', command = quit)
    global support
    support = Button(fenetre, text='Comment jouer ?', command = rules)
    support.place(x=490, y=10)
    jouer.place(x=285, y=410)
    fenetre.mainloop()


#Définition de la fonction qui crée l'interface de jeu
def game():
    global jtour, etat, etatcase,nbrpiece, canvas, restart, retour
    for i in range(1,17):
        etat[i] = True
        etatcase[i] = 0
        nbrpiece=0
    jtour=not(jtour)
    canvas = Canvas(fenetre, width=600, height=480, bg="black")
    if (jtour):
        tour = canvas.create_text(300,30, fill="white",font="Helvetica", text="Joueur 2, choissisez une pièce.")
    else:
        tour = canvas.create_text(300,30, fill="white",font="Helvetica", text="Joueur 1, choissisez une pièce.")
    restart = Button(fenetre, text='Recommencer', command = reset)
    retour = Button(fenetre, text='Menu', command = menu)
    #Création des pièces sous forme de boutons
    for i in range (1,17):
        bpiece[i] = Button(fenetre, image=ppiece[i], height=70, width=33, overrelief="sunken", activebackground="black", bg="black", bd=0, command=piece[i])
    #Création des cases sous forme de boutons
    for i in range (1,17):
        if ((i==1)|(i==3)|(i==6)|(i==8)|(i==9)|(i==11)|(i==14)|(i==16)):
            bcase[i] = Button(fenetre, image=white, bg="white", overrelief="sunken", height=70, width=70, command=case[i], state="disabled")
        else:
            bcase[i] = Button(fenetre, image=black, bg="black", overrelief="sunken", height=70, width=70, command=case[i], state="disabled")
    retour.place(x=550, y=10)
    restart.place(x=10, y=10)
    #Placement des pièces à jouer autour du plateau de jeu
    bpiece[1].place(x=30, y=70)
    bpiece[2].place(x=30, y=150)
    bpiece[3].place(x=30, y=230)
    bpiece[4].place(x=30, y=310)
    bpiece[5].place(x=80, y=70)
    bpiece[6].place(x=80, y=150)
    bpiece[7].place(x=80, y=230)
    bpiece[8].place(x=80, y=310)
    bpiece[9].place(x=535, y=70)
    bpiece[10].place(x=535, y=150)
    bpiece[11].place(x=535, y=230)
    bpiece[12].place(x=535, y=310)
    bpiece[13].place(x=485, y=70)
    bpiece[14].place(x=485, y=150)
    bpiece[15].place(x=485, y=230)
    bpiece[16].place(x=485, y=310)
    bcase[1].place(x=150, y=75)
    bcase[2].place(x=225, y=75)
    bcase[3].place(x=300, y=75)
    bcase[4].place(x=375, y=75)
    bcase[5].place(x=150, y=150)
    bcase[6].place(x=225, y=150)
    bcase[7].place(x=300, y=150)
    bcase[8].place(x=375, y=150)
    bcase[9].place(x=150, y=225)
    bcase[10].place(x=225, y=225)
    bcase[11].place(x=300, y=225)
    bcase[12].place(x=375, y=225)
    bcase[13].place(x=150, y=300)
    bcase[14].place(x=225, y=300)
    bcase[15].place(x=300, y=300)
    bcase[16].place(x=375, y=300)

    #Création du plateau de jeu sous forme de damier
    canvas.create_rectangle(150, 75, 450, 375,outline="blue", width=5)
    for i in range (0,4):
        for j in range (0,4):
            if ((i%2)==(j%2)):
                canvas.create_rectangle(i*75+150, j*75+75, i*75+225, j*75+150, outline="black",fill="white")
            else:
                canvas.create_rectangle(i*75+150, j*75+75, i*75+225, j*75+150, outline="white",fill="black")
    canvas.pack()


#Définition de la fonction qui altèrne l'ordre des joueurs
def phase2():
    if (jtour):
        canvas.create_rectangle(0, 0, 650, 60,fill="black", width=5)
        canvas.create_text(300,30, fill="white",font="Helvetica", text="Joueur 1, placez la pièce.")
    else:
        canvas.create_rectangle(0, 0, 650, 60,fill="black", width=5)
        canvas.create_text(300,30, fill="white",font="Helvetica", text="Joueur 2, placez la pièce.")


#Définitions de la fonction qui affiche lorsqu'une des fins de jeu est trouvée (victoire ou égalité)
def win():
    for i in range(1,17):
        bpiece[i].configure(state="disabled")
        bcase[i].configure(state="disabled")
    if (nbrpiece>15):
        canvas.create_rectangle(0, 0, 650, 60,fill="black", width=5)
        canvas.create_text(300,30, fill=jaune,font="Helvetica", text="Egalité ! Le plateau est plein.")
    elif (jtour):
        canvas.create_rectangle(0, 0, 650, 60,fill="black", width=5)
        canvas.create_text(300,30, fill=rouge,font="Helvetica", text="Le Joueur 2 remporte la partie !")
    else:
        canvas.create_rectangle(0, 0, 650, 60,fill="black", width=5)
        canvas.create_text(300,30, fill=rouge,font="Helvetica", text="Le Joueur 1 remporte la partie !")


#Définition de la fonction qui convertit le numéro d'une pièce en binaire afin d'obtenir ses caractéristiques (0 ou1)
def conv(a):
    a-=1
    b=0
    if ((a//8)==1):
        b+=1000
        a=a%8
    if ((a//4)==1):
        b+=100
        a=a%4
    if ((a//2)==1):
        b+=10
        a=a%2
    if ((a//1)==1):
        b+=1
    return b


#Définition de la fonction qui regarde les caractéristiques d'une pièce
def cara(a,b,c,d):
    if ((a==0)|(b==0)|(c==0)|(d==0)):
        return False
    a=conv(a)
    b=conv(b)
    c=conv(c)
    d=conv(d)
    for i in range(0,4):
        if ((a%2)==(b%2)==(c%2)==(d%2)):
            return True
        a=a//10
        b=b//10
        c=c//10
        d=d//10
    return False



#Définition de la fonction qui vérifie si une condition de victoire est présente sur le plateau
def row():
    #Lignes
    if (cara(etatcase[1],etatcase[2],etatcase[3],etatcase[4])):
        return True
    if (cara(etatcase[5],etatcase[6],etatcase[7],etatcase[8])):
        return True
    if (cara(etatcase[9],etatcase[10],etatcase[11],etatcase[12])):
        return True
    if (cara(etatcase[13],etatcase[14],etatcase[15],etatcase[16])):
        return True
    #Colonnes
    if (cara(etatcase[1],etatcase[5],etatcase[9],etatcase[13])):
        return True
    if (cara(etatcase[2],etatcase[6],etatcase[10],etatcase[14])):
        return True
    if (cara(etatcase[3],etatcase[7],etatcase[11],etatcase[15])):
        return True
    if (cara(etatcase[4],etatcase[8],etatcase[12],etatcase[16])):
        return True
    #Diagonales
    if (cara(etatcase[1],etatcase[6],etatcase[11],etatcase[16])):
        return True
    if (cara(etatcase[13],etatcase[10],etatcase[7],etatcase[4])):
        return True
    return False


#Définition de la fonction qui vérifie le passage au tour suivant
def checkwin():
    global nbrpiece, jtour
    jtour=not(jtour)
    nbrpiece+=1
    if ((nbrpiece==16)|(row())):
        win()
    else:
        if (jtour):
            canvas.create_rectangle(0, 0, 650, 60,fill="black", width=5)
            canvas.create_text(300,30, fill="white",font="Helvetica", text="Joueur 2, choissisez une pièce.")
        else:
            canvas.create_rectangle(0, 0, 650, 60,fill="black", width=5)
            canvas.create_text(300,30, fill="white",font="Helvetica", text="Joueur 1, choissisez une pièce.")




#Attributs de la fenêtre principale (apparaît au mileu de votre écran, pas redimentionable)
fenetre = tk.Tk()
fenetre.title('Quarto')
canvas = Canvas(fenetre, width=600, height=480, bg="black")
fenetre.iconbitmap("icon.ico")
fenetre.resizable(0,0)
windowHeight = 480
windowWidth = 600
locX = int(fenetre.winfo_screenwidth() / 2 - windowWidth / 2)
locY = int(fenetre.winfo_screenheight() / 2 - windowHeight / 2)
fenetre.geometry("%sx%s+%s+%s" %(windowWidth, windowHeight, locX, locY))

#Définition des variables utilisées
jtour = True
choix_piece=0

#Création des dictionnaires pour compacter les fonctions
bpiece={}
piece= {1:piece1,2:piece2,3:piece3,4:piece4,5:piece5,6:piece6,7:piece7,8: piece8,9:piece9,10:piece10,11:piece11,12:piece12,13:piece13,14:piece14,15:piece15,16:piece16}
ppiece={}
case= {1:case1,2:case2,3:case3,4:case4,5:case5,6:case6,7:case7,8: case8,9:case9,10:case10,11:case11,12:case12,13:case13,14:case14,15:case15,16:case16}
bcase={}
etat = {}
etatcase = {}
nbrpiece=0

#Initialisation des images des pièces
for i in range(1, 17):
    ppiece[i]=PhotoImage(file='piece%s.png' %i)

black = PhotoImage(file='black.png')
white = PhotoImage(file='white.png')
regles = PhotoImage(file='regles.png')
logo = PhotoImage(file='menu.png')

#Définition des couleurs utilisées
global bleu
bleu=["#DEFFFB"]
global rouge
rouge=["#EC0700"]
global jaune
jaune=["#F4DF0B"]


#Début du programme
main()
fenetre.mainloop()
