import mysql.connector


def connexionDB():
    mabase = mysql.connector.connect(host="localhost", user="diary", password="passer", database="gestion_universite")
    return mabase


# listes etudiants
def getEtudiant():
    mabase = connexionDB()
    meconnecter = mabase.cursor()
    meconnecter.execute("select p.PersonID,e.matricule,p.nom, p.prenom, p.date_naissance,"
                        " p.sexe, p.statut, p.mail,p.adresse, p.tel,"
                        "e.classe from Personne p, Etudiant e where p.PersonID=e.PersonID")
    liste = []
    for row in meconnecter:
        liste.append(row)
    return liste
    mabase.close()


# afficher la liste des Personnes
def getEtudiant():
    mabase = connexionDB()
    meconnecter = mabase.cursor()
    meconnecter.execute("select p.PersonID,e.matricule,p.nom, p.prenom, p.date_naissance,"
                        " p.sexe, p.statut, p.mail,p.adresse, p.tel,"
                        "e.classe from Personne p, Etudiant e where p.PersonID=e.PersonID")
    liste = []
    for row in meconnecter:
        liste.append(row)
    return liste
    mabase.close()


def liste_classe():
    mabase = connexionDB()
    meconnecter = mabase.cursor()
    meconnecter.execute("select nomClasse from Classe")
    liste = []

    for row in meconnecter:
        liste.append(row)
    return liste
    mabase.close()


# listes des professurs
def getProfesseur():
    mabase = connexionDB()
    meconnecter = mabase.cursor()
    meconnecter.execute("select pr.PersonID,pr.ProfId,p.nom, p.prenom, p.date_naissance,"
                        "p.sexe, p.statut,p.mail,p.adresse, p.tel,"
                        " pr.specialite from Personne p, Professeur pr where p.PersonID=pr.PersonID")
    liste = []
    for row in meconnecter:
        liste.append(row)
    return liste
    mabase.close()