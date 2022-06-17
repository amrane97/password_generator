from random import randint, choice
from tkinter import *
import string

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.ascii_uppercase + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)

# creer la fenetre
window = Tk()
window.title("generateur de mot de passes")
window.geometry("720x380")
window.iconbitmap("logoApp.ico")
window.config(background="#4065A4")

#creer un cadre
frame = Frame(window, bg="#4065A4")
# sous cadre
right_frame = Frame(frame,bg="#4065A4")

#creation d'image
width = 300
height = 300
image = PhotoImage(file="password.png",).zoom(35).subsample(32)
canvas = Canvas(frame,width=width,height=height,bg="#4065A4",bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row=0,column=0,sticky=W) #la fonction grid (ligne=row, column=colonne,sticky=po

#creer un titre
label_titre = Label(right_frame,text="mot de passe",font=("helvetica",20),bg="#4065A4",fg="white")
label_titre.pack()

#creer un champs/entrée/input
password_entry = Entry(right_frame,font=("helvetica",20),bg="white",fg="Black")
password_entry.pack(padx=25)

#creer un bouton
generate_password_button = Button(right_frame,text="Generate",font=("helvetica",20),bg="#D2D2D2",fg="Black",bd=0, command=generate_password)
generate_password_button.pack(padx=25,pady=25,fill=X) # fill=remplir

#on place la sous boite a droite de la frame principale
right_frame.grid(row=0,column=1,sticky=W)

#afficher la frame
frame.pack(expand=YES)
#creation d'une barre de menu
menu_barre = Menu(window)
#creer un premier menu
file_menu = Menu(menu_barre, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_barre.add_cascade(label="Fichier", menu=file_menu)
#configurer notre fenetre pour ajouter cette barre de menu
window.config(menu=menu_barre)

#afficher fenetre
window.mainloop()