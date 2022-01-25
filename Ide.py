from tkinter import*
from tkinter import ttk
from tkinter.filedialog import *
import subprocess
import os.path
def loadingScreen():
    global photo1
    photo1=photo1.subsample(10,10)
    def titlePourcents():
            try:
                fen.title(str(int(pb["value"]))+" % loaded")
                fen.after(50,titlePourcents)
            except:
                pass
    b = Label(fen,image=photo1)
    b.grid(padx=5,pady=5)
    pb = ttk.Progressbar(fen, orient="horizontal",length = 400, mode="determinate")
    pb.grid(padx=5,pady=5)
    pb.start()
    fen.after(50,titlePourcents)
    fen.after(5000,pb.destroy)
    fen.after(5000,b.destroy)
    

def ecranIDE():
    nom="C:/Users/Geoffrey/Desktop/PYTHON/C++ idle/sansNom.c"
    text_file = open(nom, "w")
    non=""
    def entreeTexte(event):
        global nom,non
        x=entree.get(1.0,END)
        text_file = open(nom, "w")
        non=os.path.basename(text_file.name)
        text_file.write(x)
    def edit():
        global nom,non
        nom = askopenfilename()
        text_file = open(nom, "w")
        non=os.path.basename(text_file.name)
    def new():
        global nom,non
        nom=asksaveasfilename()
        text_file = open(nom, "w")
        non=os.path.basename(text_file.name)
    def compiler():
        global non,nom
        subprocess.call(("cd "+os.path.dirname(nom)),shell =True)
        subprocess.call(("gcc -o MyProgram "+non),shell =True)
        
        
        
    fen.title("C++ IDE")
    
    menubar = Menu(fen)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer",command=new)
    menu1.add_command(label="Editer",command=edit)
    menu1.add_command(label="Compiler",command=compiler)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fen.destroy)
    menubar.add_cascade(label="Fichier", menu=menu1)


    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu3)

    fen.config(menu=menubar)
    
    fen.geometry("550x550")
    entree=Text(fen)
    entree.grid(column=0,row=0,pady=5,padx=5)
    fen.bind("<Return>",entreeTexte)
    


fen=Tk()
fen.iconbitmap("C_.ico")
photo1=PhotoImage(file="C++.png")
loadingScreen()
fen.after(5000,ecranIDE)
fen.mainloop()
#

