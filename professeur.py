from tkinter import ttk, Tk, messagebox
from tkinter import *
from tkcalendar import *
from pythonProject.bd import getProfesseur, connexionDB


modifier=False

def ajouter_professeur():
    if modifier==False:
        if ProfId.get()!="" and nom.get() != "" and prenom.get() != "" and sexe.get() != "" and statut.get() != "" and mail.get() != "" and adresse.get()!= "" and telephone.get()!= "":
            try:
                  mabase=connexionDB()
                  meconnecter=mabase.cursor()
                  sql = "SELECT * from Personne where mail=%s"
                  meconnecter.execute(sql, (mail.get(),))
                  row=meconnecter.fetchone()
                  if row!=None:
                      messagebox.showerror("Erreur", "ce mail exite deja.Essayer un autre mail")
                  else:
                       sql1 = "INSERT INTO Personne (nom,prenom,date_naissance,sexe,statut,mail,adresse,tel) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                       val1 = (nom.get(), prenom.get(), datenaissance.get(), sexe.get(), statut.get(), mail.get(), adresse.get(), telephone.get())
                       meconnecter.execute(sql1, val1)
                       meconnecter.execute("SELECT PersonID FROM Personne ORDER BY PersonID DESC LIMIT 1")

                       rows = meconnecter.fetchall()
                       for row in rows:
                         idpers= row[0]

                       sql2 = "INSERT INTO Professeur (ProfId,specialite, PersonID) VALUES(%s, %s, %s)"
                       val2 = (ProfId.get(), specialite.get(), idpers)
                       meconnecter.execute(sql2,val2)
                       mabase.commit()
                       messagebox.showinfo("information", "professur ajouter", parent=root)

            except Exception as ex:
                  print("erreur")
                  print(ex)
                  mabase.rollback()
                  mabase.close()
        else:
           messagebox.showerror("Erreur","Remplir les champs",parent=root,)
    else:
        modifierFalse()
def modifier_professeur():


    if modifier==True:
        if nom.get() != "" and prenom.get() != "" and sexe.get() != "" and statut.get() != "" and mail.get()!= "" and adresse.get() != "" and telephone.get() != "":
            try:
                  mabase=connexionDB()
                  meconnecter=mabase.cursor()
                  sql="update Personne p, Professeur pr set p.nom=%s,p.prenom=%s, p.date_naissance=%s," \
                        "p.sexe=%s,p.statut=%s,p.mail=%s,p.adresse=%s,p.tel=%s, pr.specilaite=%s"
                  val=(nom.get(),prenom.get(),datenaissance.get(),sexe.get(),statut.get(),mail.get(),adresse.get(),telephone.get(),specialite.get())
                  meconnecter.execute(sql,val)
                  mabase.commit()
                  messagebox.showinfo("information", "Modification reussi", parent=root)
                  #root.mainloop()
            except Exception as ex:
                  print("erreur")
                  print(ex)
                  mabase.rollback()
                  mabase.close()
        else:
           messagebox.showerror("Erreur","Remplir les champs",parent=root)
    else:
        modifierTrue()

def supprimerProfesseur():
    id=table.selection()[0]
    if int(id)>0:
      mabase=connexionDB()
      meconnecter=mabase.cursor()
      sql = "delete from Personne where PersonID=%s"
      meconnecter.execute(sql, (id,))
      mabase.commit()
      table.delete(id)
      messagebox.showinfo("Info", "Supression reussi")
      root.mainloop()
    else:
        messagebox.showerror("erreur", "clique sur la ligne a supprimer", parent=root)


def selectionner(event):
    id = table.selection()[0]
    if int(id)>0:
        ProfId.set(table.item(id, "values")[1])
        nom.set(table.item(id, "values")[2])
        prenom.set(table.item(id, "values")[3])
        datenaissance.set(table.item(id, "values")[4])
        sexe.set(table.item(id, "values")[5])
        statut.set(table.item(id, "values")[6])
        mail.set(table.item(id, "values")[7])
        adresse.set(table.item(id, "values")[8])
        telephone.set(table.item(id, "values")[9])
        specialite.set(table.item(id, "values")[10])
def modifierFalse():
    global modifier
    modifier=False
    table.config(selectmode=NONE)
    btnenregistrer.config(text="Sauvegarder")
    btnmodifier.config(text="Selectionner")
    btnsupprimer.config(state=DISABLED)
def modifierTrue():
    global modifier
    modifier=True
    table.config(selectmode=BROWSE)
    btnenregistrer.config(text="ajouter")
    btnmodifier.config(text="modifier")
    btnmodifier.config(state=NORMAL)
root=Tk()
root.title("Menu Principale")
root.geometry("1350x700+0+0")
root.resizable(False,False)
root.configure(background="#091821")

#ajouter le titre
lbltitre=Label(root,borderwidth=3,relief=SUNKEN, text="Ajouter un Professeur",
               font=('Sans serif',25), background="#091821", fg="white")
lbltitre.place(x=0,y=0,width=1350,height=50)

ProfId=StringVar()
nom=StringVar()
prenom=StringVar()
datenaissance=StringVar()
sexe=StringVar()
statut=StringVar()
mail=StringVar()
adresse=StringVar()
telephone=StringVar()
specialite=StringVar()


#Donnees
#Matricule
lblprofid= Label (root, text="ProfId :", font=("Arial,18"), bg="#091821",
                        fg="white")
lblprofid.place(x=100,y=100,width=150)
textprofid=Entry(root, bd=4,font=("Arial",14), textvariable=ProfId)
textprofid.place(x=230,y=100,width=150)

#Nom
lblnom= Label (root, text="nom :", font=("Arial,18"), bg="#091821",
                        fg="white")
lblnom.place(x=100,y=150,width=150)
textnom=Entry(root, bd=4,font=("Arial",14), textvariable=nom)
textnom.place(x=230,y=150,width=300)
#Prenom
lblprenom= Label (root, text="prenom :", font=("Arial,18"), bg="#091821",
                        fg="white")
lblprenom.place(x=100,y=200,width=150)
textprenom=Entry(root, bd=4,font=("Arial",14), textvariable=prenom)
textprenom.place(x=230,y=200,width=300)

#date naissance
lbldateNaissance= Label (root, text="Naissance :", font=("Arial,18"), bg="#091821",
                        fg="white")
lbldateNaissance.place(x=100,y=250,width=150)
textdatenaissance=DateEntry(root, bd=4,font=("Arial",14),state="readonly", textvariable=datenaissance, date_pattern="yyyy-mm-dd")
textdatenaissance.place(x=230,y=250,width=300)

#Genre
lblsexe=Label(root, text="SEXE:", font=("Arial,18"), bg="#091821",fg="white")
lblsexe.place(x=100,y=300,width=150)
listesexe=ttk.Combobox(root, font=("Arial",14), textvariable=sexe)
listesexe['values']=["M", "F"]
listesexe.place(x=230,y=300,width=130)

#statut
lblstatut=Label(root, text="STATUT:", font=("Arial,18"), bg="#091821",fg="white")
lblstatut.place(x=630,y=100,width=150)
listestatut=ttk.Combobox(root, font=("Arial",14), textvariable=statut)
listestatut['values']=["celibataire", "Marie", "Divorce"]
listestatut.place(x=760,y=100,width=130)

#mail
lblmail= Label (root, text="Mail :", font=("Arial,18"), bg="#091821",
                        fg="white")
lblmail.place(x=630,y=150,width=150)
textmail=Entry(root, bd=4,font=("Arial",14), textvariable=mail)
textmail.place(x=760,y=150,width=200)

#adresse

lbladresse=Label(root, text="Adresse", font=("Arial,18"), bg="#091821",fg="white")
lbladresse.place(x=630,y=200,width=150)
textadresse=Entry(root, bd=4,font=("Arial",14), textvariable=adresse)
textadresse.place(x=760,y=200,width=200)

#telephone
lbltelephone=Label(root, text="Telephone", font=("Arial,18"), bg="#091821",fg="white")
lbltelephone.place(x=630,y=250,width=150)
texttelephone=Entry(root, bd=4,font=("Arial",14), textvariable=telephone)
texttelephone.place(x=760,y=250,width=200)

#specialite
lblspecialite=Label(root, text="Specialite", font=("Arial,18"), bg="#091821",fg="white")
lblspecialite.place(x=630,y=300,width=150)
textspecialite=Entry(root, bd=4,font=("Arial",14), textvariable=specialite)
textspecialite.place(x=760,y=300,width=200)


#enregistrer
btnenregistrer=Button(root, text="Sauvegarder", font=("Arial",16), bg="#D2691E", fg="white",command=ajouter_professeur)
btnenregistrer.place(x=500,y=350,width=200)
#modifier
btnmodifier=Button(root, text="selectionner", font=("Arial",16), bg="#D2691E", fg="white",command=modifier_professeur)
btnmodifier.place(x=800,y=350,width=200)
#supprimer
btnsupprimer=Button(root, text="Supprimer", font=("Arial",16), bg="#D2691E", fg="white",command=supprimerProfesseur)
btnsupprimer.place(x=1100,y=350,width=200)


table=ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7,8,9,10,11),
                   show="headings", selectmode=NONE)
table.place(x=70,y=400,width=1200, height=450)
table.heading(1,text="ID")
table.heading(2,text="ProfID")
table.heading(3,text="NOM")
table.heading(4,text="PRENOM")
table.heading(5,text="Date Naissance")
table.heading(6,text="SEXE")
table.heading(7,text="Statut")
table.heading(8,text="Mail")
table.heading(9,text="Adresse")
table.heading(10,text="Telephone")
table.heading(11,text="Specialite")

table.column(1,width=20)
table.column(2,width=100)
table.column(3,width=50)
table.column(4,width=150)
table.column(5,width=100)
table.column(6,width=50)
table.column(7,width=100)
table.column(8,width=50)
table.column(9,width=100)
table.column(10,width=150)
table.column(11,width=150)
table.bind("<<TreeviewSelect>>", selectionner)

rows=getProfesseur()
for row in rows:
    id=row[0]
    print(id)
    table.insert('',END, id, text=id,value=row)



#execution
root.mainloop()