import pandas as pd
import pywhatkit as pwk

# Read the CSV file
stagiaires = pd.read_csv('Stagiaires.csv')

# Print column names to see what we're working with
print("Column names in the Excel file:", stagiaires.columns.tolist())

# Select columns and convert phone numbers to string format
stagiaires = stagiaires[["Nom", "Numéro"]].copy()
stagiaires["Numéro"] = stagiaires["Numéro"].astype(str).apply(lambda x: f"+{x}" if not x.startswith('+') else x)

# Shuffle the DataFrame randomly
stagiaires = stagiaires.sample(frac=1).reset_index(drop=True)

# Get the first and last person
premier = stagiaires.iloc[0]
dernier = stagiaires.iloc[-1]

# Loop through participants
for i in range(stagiaires.shape[0] - 1):
    current_person = stagiaires.iloc[i]
    next_person = stagiaires.iloc[i + 1]

    message = f'🚨CONFIDENTIEL🚨\nHello {current_person["Nom"]}, pendant l\'allumage des premieres bougies,tu vas devoir offrir ton cadeau à {next_person["Nom"]} !\nGarde ca pour toi ne le partage a personne, on compte sur toi !\nHanoukah Sameah et bon stage !'
    pwk.sendwhatmsg_instantly(current_person["Numéro"], message)
    print(message)
    print("\n")

# Last person gives to first person
message = f'🚨CONFIDENTIEL🚨\nHello {dernier["Nom"]}, pendant l\'allumage des premieres bougies,tu vas devoir offrir ton cadeau à {premier["Nom"]} !\nGarde ca pour toi ne le partage a personne, on compte sur toi !\nHanoukah Sameah et bon stage !'

pwk.sendwhatmsg_instantly(dernier["Numéro"], message)
print(message)
