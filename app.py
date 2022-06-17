from tkinter import *
import webbrowser

def open_graven_youtube():
    webbrowser.open_new("https://www.youtube.com/watch?v=N4M4W7JPOL4&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=9")

#creer une nouvelle fenetre
window = Tk()
#modifier le titre
window.title("Mapuchio")# titre sur la fenetre

#modifier la taille d'affichage
window.geometry("480x360")#taille de la fenetre au debut
window.minsize(480,360)
window.iconbitmap("logoApp.ico")#insere le logo
window.config(background ='#113C36')# couleur de fond

#creer une frame
frame = Frame(window,bg="#113C36")#,bd=1,relief=SUNKEN)

#ajouter du texte a ma fenetre
label_title = Label(frame,text="jeu MAPUCHIO", font=("algerian", 30), bg="#113C36",fg="#F5C2C2")
label_title.pack()# responsable de l'affichage du texte

#ajouter un autre texte
label_subtitle = Label(frame,text="bienvenu dans le monde de mapuchio ame sensible s'abstenir", font=("algerian", 20), bg="#113C36",fg="#F5C2C2")
label_subtitle.pack()

#centret mon cadre
frame.pack(expand=YES)

#ajouter un nouveau bouton
yt_button = Button(frame, text="ouvrir youtube",font=("calibri,20"),bg="#CCB9B9",fg="#F50004",command= open_graven_youtube)
yt_button.pack(pady=25,fill=X)

#afficher
window.mainloop()