# Secret Santa & Office Groups Manager 🎅🎁

Ce projet contient deux scripts Python pour gérer un Secret Santa et la répartition de stagiaires en groupes équilibrés.

## Prérequis

- Python 3.x
- pandas
- pywhatkit

Installation des dépendances :

    pip install pandas pywhatkit

## Structure des fichiers

- `secretSanta.py` : Script pour organiser un Secret Santa avec envoi de messages WhatsApp
- `liste_office.py` : Script pour répartir les stagiaires en groupes équilibrés
- `Stagiaires.csv` : Fichier contenant les informations des participants

## Format du fichier Stagiaires.csv

Pour le Secret Santa :

    Nom,Numéro
    John Doe,+33612345678

Pour la répartition en groupes :

    Nom,Sexe,Stage
    John Doe,M,Type1

## Utilisation

### Secret Santa

    python secretSanta.py

Le script va :
1. Lire la liste des participants
2. Attribuer aléatoirement les binômes
3. Envoyer un message WhatsApp à chaque participant

### Répartition en groupes

    python liste_office.py

Le script va :
1. Diviser les stagiaires en 3 groupes équilibrés
2. Équilibrer les groupes selon le sexe et le type de stage
3. Générer des fichiers CSV pour chaque groupe

## Notes importantes

- Les numéros de téléphone doivent être au format international (ex: +33612345678)
- WhatsApp Web doit être connecté pour l'envoi des messages
- Le fichier CSV doit être encodé en UTF-8

## Contribution

N'hésitez pas à contribuer au projet en soumettant des pull requests ou en signalant des bugs.

## Licence

Ce projet est sous licence MIT. 