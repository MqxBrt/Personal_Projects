#Initialisation
from tkinter import*
import tkinter as tk
import time
import random
import pygame
import pyglet
from pyglet import font
pygame.mixer.init()

#Définition des valeurs de score et de records
s=0
F=5810 #Par Maxime
N=7325 #Par Maxime
D=1480 #Par Maxime


#Définition du bouton aide:
    #Cette fonction permet d'ouvrir la fenêtre sur laquelle est écrite la notice de jeu.
    #Elle est associée au bouton "Comment jouer ?"
def tutoriel():
    global aide
    aide = tk.Tk()
    aide.title("Notice Tap Dance")
    aide.iconbitmap("Ressources\Images\icon.ico")
    ligne1 = Label(aide, text="-Bienvenue sur Tap Dance-")
    ligne2 = Label(aide, text="")
    ligne3 = Label(aide, text="Lors d'une partie, une musique se mettra en route et des flèches descendront à l'écran.")
    ligne4 = Label(aide, text="Le but du jeu sera  d'appuyer sur la touche correspondante :")
    ligne5 = Label(aide, text="Flèche de droite, Flèche de gauche, Flèche du haut et Flèche du bas sur votre clavier, selon le sens de la flèche affichée sur le jeu.")
    ligne6 = Label(aide, text="Appuyer sur la bonne touche vous fera gagner des points, appuyer sur la mauvaise vous en fera perdre.")
    ligne7 = Label(aide, text="Le nombre de points gagnés et perdus dépend de la difficulté choisie :")
    ligne8 = Label(aide, text="En mode Facile, vous gagnerez 10 points et en perdrez 15.")
    ligne9 = Label(aide, text="En mode Normal, vous gagnerez 15 points et en perdrez 10.")
    ligne10 = Label(aide, text="En mode Difficile, vous gagnerez 20 points et en perdrez 5.")
    ligne11 = Label(aide, text="")
    ligne12 = Label(aide, text="Remarque : Vous pouvez appuyer plusieurs fois sur la bonne touche pour améliorer votre score tant que la flèche correspondante est affichée à l'écran")
    ligne13 = Label(aide, text="Restez attentif, car en cas de changement de flèche, vous perdrez des points si vous continuez à appuyer sur la mauvaise.")
    ligne14 = Label(aide, text="")
    ligne15 = Label(aide, text="Le jeu s'arrête à la fin de la musique, votre score comptabilisé sera alors affiché.")
    ligne1.pack()
    ligne2.pack()
    ligne3.pack()
    ligne3.pack()
    ligne4.pack()
    ligne5.pack()
    ligne6.pack()
    ligne7.pack()
    ligne8.pack()
    ligne9.pack()
    ligne10.pack()
    ligne11.pack()
    ligne12.pack()
    ligne13.pack()
    ligne14.pack()
    ligne15.pack()
    aide.mainloop()

#Définition du bouton jouer
    #Cette fonction est associée au bouton qui permet de lancer la fenêtre jeu depuis le menu
def play():
    pygame.mixer.music.stop()
    fenetre.destroy()
    jeu()

#Définition du bouton quitter
    #Cette fonction est associée au bouton qui permet de quitter le programme depuis le menu
def quit():
    pygame.mixer.music.stop()
    fenetre.destroy()

#Définition du boutton menu
    #Cette fonction est associée au bouton qui permet de revenir au menu depuis l'interface de jeu
def main():
    jeux.destroy()
    menu()

#Définition du bouton de sortie
    #Cette fonction est associée au bouton qui permet de quitter le jeu depuis l'interface de jeu
def exit():
    pygame.mixer.music.stop()
    jeux.destroy()

#Définition du menu
    #Cette fonction est celle qui se lance dès le début du programme
def menu():
    global fenetre
    fenetre = tk.Tk()
    fenetre.title("Tap Dance")
    #Ressoucres du menu
    fenetre.iconbitmap("Ressources\Images\icon.ico")
    can = Canvas(fenetre, height=800, width=1400)
    menu = PhotoImage(file="Ressources\Images\menu.png")
    pygame.mixer.music.load("Ressources\Musiques\Intro.wav")
    #font.add_file('Ressources\Polices\Pixel Digivolve.otf')
    #Création du canevas du menu
    can.create_image(0,0, anchor=NW, image=menu)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    #fenetre.attributes("-fullscreen",True)
    #Boutons du menu
    quitter = Button(fenetre, text='Quitter', command = quit)
    quitter.pack(side=BOTTOM)
    notice = Button(fenetre, text='Comment jouer ?', command = tutoriel)
    notice.pack(side=BOTTOM)
    jouer = Button(fenetre, text='Jouer: "On Our Way to the Oasis", Zazonx', command = play)
    jouer.pack(side=BOTTOM)
    #Exécution du menu
    can.pack()
    fenetre.mainloop()

#Définition de la fonction Jeu
    #Cette fonction est associée au bouton qui permet de lancer l'interface du jeu depuis le menu
def jeu():

    #Définition de l'interface du jeu
    global jeux
    jeux = tk.Tk()
    jeux.title("Tap Dance")
    jeux.iconbitmap("Ressources\Images\icon.ico")
    jeux.attributes("-fullscreen",True)
    pygame.mixer.music.load("Ressources\Musiques\On Our Way to the Oasis.wav")
    pygame.mixer.music.set_volume(0.05)
    canvas = Canvas(jeux, height=800, width=1400)
    fond = PhotoImage(file="Ressources\Images\jeu.png")
    canvas.create_image(0,0, anchor=NW, image=fond)

    #Cette fonction est associée au bouton qui permet de lancer le mode Facile
    def lvl1() :
        niveau1.destroy()
        niveau2.destroy()
        niveau3.destroy()
        retour.destroy()
        Facile()

    #Cette fonction est associée au bouton qui permet de lancer le mode Normal
    def lvl2():
        niveau1.destroy()
        niveau2.destroy()
        niveau3.destroy()
        retour.destroy()
        Normal()

    #Cette fonction est associée au bouton qui permet de lancer le mode Difficile
    def lvl3():
        niveau1.destroy()
        niveau2.destroy()
        niveau3.destroy()
        retour.destroy()
        Difficile()

    #Boutons de sélections de niveau
    niveau1 = Button(jeux, text='Facile (recommandé pour les joueurs débutants)', command=lvl1)
    niveau2 = Button(jeux, text='Normal (recommandé pour les joueurs aguéris, faisant plus de 4000 en mode Facile)', command=lvl2)
    niveau3 = Button(jeux, text='Difficile (recommandé pour les joueurs expérimentés, faisant plus de 8000 en mode Normal)', command=lvl3)
    retour = Button(jeux, text='Menu', command = main)
    sortie = Button(jeux, text='Quitter', command = exit)
    sortie.pack(side=BOTTOM)
    retour.pack(side=BOTTOM)
    niveau3.pack(side=BOTTOM)
    niveau2.pack(side=BOTTOM)
    niveau1.pack(side=BOTTOM)
    canvas.pack()

    #Mode de jeu Facile
        #Cette fonction correspond à ce qui va se lancer lors du mode Facile
    def Facile():

        pygame.mixer.music.play(loops=1)

        #Couleurs du jeu
        jaune=["#F9C41E"]
        vert=["#22F91B"]
        rouge=["#ED1717"]
        bleu=["#1A49D8"]

        #Creation des 4 types de flèches
        d = canvas.create_polygon(1050  ,-100, 1050, 0, 1150,-50, fill=jaune)
        g = canvas.create_polygon(350,-100, 350, 0, 250,-50, fill=jaune)
        h = canvas.create_polygon(700, -100, 750, 0,  650, 0, fill=jaune)
        b = canvas.create_polygon(700, 0, 650 ,-100, 750, -100, fill=jaune)

        liste = list(range(2,6))

        #Boucle choisissant la flèche qui descend
        for j in range (0, 145) :
            polygone_choisi = random.choice(liste)
            try :
                canvas.itemconfig(polygone_choisi, fill=jaune)
            except:
                pass

            #Définition de la fonction flèche du haut
            def up(event):
                global s
                if polygone_choisi==h:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=10

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=15


            #Définition de la fonction flèche du bas
            def down(event):
                global s
                if polygone_choisi==b:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=10

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=15


            #Définition de la fonction flèche gauche
            def left(event):
                global s
                if polygone_choisi==g:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=10

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=15


            #Définition de la fonction flèche droite
            def right(event):
                global s
                if polygone_choisi==d:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=10

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=15

            #Assignation des touches
            try:
                jeux.bind("<KeyPress-Up>", up)
                jeux.bind("<KeyPress-Down>", down)
                jeux.bind("<KeyPress-Right>", right)
                jeux.bind("<KeyPress-Left>", left)
            except:
                pass

            #Boucle faisant descendre la flèche
            for i in range (0, 90):
                try :
                    canvas.move(polygone_choisi,0,10)
                    jeux.update()
                    time.sleep(0.01)
                except:
                    break

            #Boucle faisant remonter la flèche
            for k in range (0,1):
                try:
                    canvas.move(polygone_choisi, 0, -900)
                    canvas.itemconfig(polygone_choisi, fill=jaune)
                    jeux.update()
                except:
                    break

        try:
            score = Label(canvas, text= "Votre score en mode Facile = " + str(s), font=("Helvetica", 38), bg=bleu, height = 100, width = 100)
            #score = Label(canvas, text= "Votre score en mode Facile = " + str(s), font=("Pixel Digivolve", 50), bg=bleu, height = 100, width = 100)
            score.pack()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Ressources\Musiques\Outro.wav")
            pygame.mixer.music.set_volume(0.35)
            pygame.mixer.music.play(loops=1)
            if s > F :
                print ("")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Nouveau Record pour le mode Facile !")
                print ("Remplacez la variable F par :", s)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else :
                G=F-s
                print ("")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Meilleur Score du mode Facile :", F)
                print ("Différence :", G)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except:
            pass

    #Mode de jeu Normal
        #Cette fonction correspond à ce qui va se lancer lors du mode Normal
    def Normal():

        pygame.mixer.music.play(loops=1)

        #Couleurs des flèches
        jaune=["#F9C41E"]
        vert=["#22F91B"]
        rouge=["#ED1717"]
        bleu=["#1A49D8"]

        #Creation des 4 types de flèches
        g = canvas.create_polygon(1150 ,-100, 1150,0, 1050,-50, fill=jaune)
        d = canvas.create_polygon(250,-100, 250, 0, 350,-50, fill=jaune)
        h = canvas.create_polygon(700, -100, 750, 0,  650, 0, fill=jaune)
        b = canvas.create_polygon(700, 0, 650 ,-100 ,750, -100, fill=jaune)

        liste = list(range(2,6))

        #Boucle choisissant la flèche qui descend
        for j in range (0, 174) :
            polygone_choisi = random.choice(liste)
            try :
                canvas.itemconfig(polygone_choisi, fill=jaune)
            except:
                pass

            #Définition de la fonction flèche du haut
            def up(event):
                global s
                if polygone_choisi==h:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=15

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=10


            #Définition de la fonction flèche du bas
            def down(event):
                global s
                if polygone_choisi==b:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=15

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=10


            #Définition de la fonction flèche gauche
            def left(event):
                global s
                if polygone_choisi==g:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=15

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=10


            #Définition de la fonction flèche droite
            def right(event):
                global s
                if polygone_choisi==d:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=15

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=10


            #Assignation des touches
            try:
                jeux.bind("<KeyPress-Up>", up)
                jeux.bind("<KeyPress-Down>", down)
                jeux.bind("<KeyPress-Right>", right)
                jeux.bind("<KeyPress-Left>", left)
            except:
                pass

            #Boucle faisant descendre la flèche
            for i in range (0, 90):
                try :
                    canvas.move(polygone_choisi,0,10)
                    jeux.update()
                    time.sleep(0.0075)
                except:
                    break

            #Boucle faisant remonter la flèche
            for k in range (0,1):
                try:
                    canvas.move(polygone_choisi, 0, -900)
                    canvas.itemconfig(polygone_choisi, fill=jaune)
                    jeux.update()
                except:
                    break

        try:
            score = Label(canvas, text= "Votre score en mode Normal = " + str(s), font=("Helvetica", 38), bg=bleu, height = 100, width = 100)
            #score = Label(canvas, text= "Votre score en mode Normal = " + str(s), font=("Pixel Digivolve", 50), bg=bleu, height = 100, width = 100)
            score.pack()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Ressources\Musiques\Outro.wav")
            pygame.mixer.music.set_volume(0.35)
            pygame.mixer.music.play(loops=1)
            if s > N :
                print ("")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Nouveau Record pour le mode Normal !")
                print ("Remplacez la variable N par :", s)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else :
                G=N-s
                print ("")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Meilleur Score :", N)
                print ("Différence :", G)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except:
            pass


    #Mode de jeu Difficile
        #Cette fonction correspond à ce qui va se lancer lors du mode Difficile
    def Difficile():

        pygame.mixer.music.play(loops=1)

        #Couleurs des flèches
        jaune=["#F9C41E"]
        vert=["#22F91B"]
        rouge=["#ED1717"]
        bleu=["#1A49D8"]

        #Creation des 4 types de flèches
        d1 = canvas.create_polygon(1050  ,-100, 1050, 0, 1150,-50, fill=jaune)
        h1 = canvas.create_polygon(1100, -100, 1150, 0, 1050, 0, fill=jaune)
        b1 = canvas.create_polygon(1100, 0, 1050, -100, 1150, -100, fill=jaune)
        g1 = canvas.create_polygon(1150, -100, 1150, 0, 1050, -50, fill=jaune)
        d2 = canvas.create_polygon(635, -100, 635, 0, 735, -50, fill=jaune)
        h2 = canvas.create_polygon(700, -100, 750, 0,  650, 0, fill=jaune)
        b2 = canvas.create_polygon(700, 0, 650 ,-100 ,750, -100, fill=jaune)
        g2 = canvas.create_polygon(735, -100, 735, 0, 635, -50, fill=jaune)
        d3 = canvas.create_polygon(250, -100, 250, 0, 350, -50, fill=jaune)
        h3 = canvas.create_polygon(300, -100, 350, 0, 250, 0, fill=jaune)
        b3 = canvas.create_polygon(300, 0, 250, -100, 350, -100, fill=jaune)
        g3 = canvas.create_polygon(350,-100, 350, 0, 250,-50, fill=jaune)


        liste = list(range(2,14))

        #Boucle choisissant la flèche qui descend
        for j in range (0, 261) :
            polygone_choisi = random.choice(liste)
            try :
                canvas.itemconfig(polygone_choisi, fill=jaune)
            except:
                pass

            #Définition de la fonction flèche du haut
            def up(event):
                global s
                if polygone_choisi==h1 or polygone_choisi==h2 or polygone_choisi==h3:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=20

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=5


            #Définition de la fonction flèche du bas
            def down(event):
                global s
                if polygone_choisi==b1 or polygone_choisi==b2 or polygone_choisi==b3:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=20

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=5


            #Définition de la fonction flèche gauche
            def left(event):
                global s
                if polygone_choisi==g1 or polygone_choisi==g2 or polygone_choisi==g3:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=20

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=5


            #Définition de la fonction flèche droite
            def right(event):
                global s
                if polygone_choisi==d1 or polygone_choisi==d2 or polygone_choisi==d3:
                    canvas.itemconfig(polygone_choisi, fill=vert)
                    s+=20

                else :
                    canvas.itemconfig(polygone_choisi, fill=rouge)
                    s-=5


            #Assignation des touches
            try:
                jeux.bind("<KeyPress-Up>", up)
                jeux.bind("<KeyPress-Down>", down)
                jeux.bind("<KeyPress-Right>", right)
                jeux.bind("<KeyPress-Left>", left)
            except:
                pass

            #Boucle faisant descendre la flèche
            for i in range (0, 90):
                try :
                    canvas.move(polygone_choisi,0,10)
                    jeux.update()
                    time.sleep(0.005)
                except:
                    break

            #Boucle faisant remonter la flèche
            for k in range (0,1):
                try:
                    canvas.move(polygone_choisi, 0, -900)
                    canvas.itemconfig(polygone_choisi, fill=jaune)
                    jeux.update()
                except:
                    break

        try:
            score = Label(canvas, text= "Votre score en mode Difficile = " + str(s), font=("Helvetica", 38), bg=bleu, height = 100, width = 100)
            #score = Label(canvas, text= "Votre score en mode Difficile = " + str(s), font=("Pixel Digivolve", 50), bg=bleu, height = 100, width = 100)
            score.pack()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Ressources\Musiques\Outro.wav")
            pygame.mixer.music.set_volume(0.35)
            pygame.mixer.music.play(loops=1)
            if s > D :
                print ("")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Nouveau Record pour le mdoe Difficile !")
                print ("Remplacez la variable D par :", s)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else :
                G=D-s
                print ("")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Meilleur Score :", D)
                print ("Différence :", G)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except:
            pass

    while True :
        try:
            jeux.update_idletasks()
            jeux.update()
        except:
            break

menu()