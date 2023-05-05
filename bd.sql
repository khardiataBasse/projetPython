DROP database if exists gestion_universite;
CREATE database gestion_universite;
USE gestion_universite;

CREATE table Classe(
    nomClasse varchar(100) not null,
    ecole varchar(250) not null,
    primary key(nomClasse)
);



CREATE table Personne(
PersonID integer auto_increment,
nom varchar(30) not null,
prenom varchar(250) not null,
date_naissance varchar(100) not null,
sexe varchar(30) not null,
statut varchar(30) not null,
mail varchar(100) not null,
adresse varchar(250) not null,
tel integer not null,
primary key(PersonID)
);

CREATE table Etudiant(
matricule varchar(30) not null,
classe varchar(100) not null,
domaine_etude varchar(100) not null,
PersonID integer,
primary key (matricule),
FOREIGN KEY (PersonID) REFERENCES Personne(PersonID)
);

CREATE table Professeur(
ProfId varchar(30) not null,
specialite varchar(100) not null,
PersonID integer,
primary key (ProfId),
FOREIGN KEY (PersonID) REFERENCES Personne(PersonID)
);

CREATE table Matiere(
    matriculeEtudiant varchar(30),
    nomMatiere varchar(100) not null,
    note integer not null,
    primary key(nomMatiere),
    FOREIGN KEY (matriculeEtudiant) REFERENCES Etudiant(matricule)
);


