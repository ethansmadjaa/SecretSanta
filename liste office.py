import pandas as pd

# Lire le fichier CSV
stagiaires = pd.read_csv('Stagiaires.csv')


def split_into_balanced_groups(df, n_groups=3):
    # Créer une copie du DataFrame
    df = df.copy()

    # Mélanger aléatoirement le DataFrame
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Créer des groupes vides
    groups = [[] for _ in range(n_groups)]

    # Obtenir les distributions actuelles par sexe et type de stage
    sex_counts = df['Genre'].value_counts()
    stage_counts = df['Stage'].value_counts()

    # Calculer les objectifs par groupe
    target_sex = {sex: count // n_groups for sex, count in sex_counts.items()}
    target_stage = {stage: count // n_groups for stage, count in stage_counts.items()}

    # Compteurs pour chaque groupe
    group_counts = [{
        'Genre': {sex: 0 for sex in sex_counts.index},
        'Stage': {stage: 0 for stage in stage_counts.index}
    } for _ in range(n_groups)]

    # Assigner chaque personne à un groupe
    for _, person in df.iterrows():
        # Trouver le meilleur groupe pour cette personne
        best_group = 0
        min_score = float('inf')

        for i in range(n_groups):
            # Calculer un score basé sur l'équilibre du groupe
            score = 0
            if group_counts[i]['Genre'][person['Genre']] < target_sex[person['Genre']]:
                score += group_counts[i]['Genre'][person['Genre']]
            else:
                score += 999

            if group_counts[i]['Stage'][person['Stage']] < target_stage[person['Stage']]:
                score += group_counts[i]['Stage'][person['Stage']]
            else:
                score += 999

            if score < min_score:
                min_score = score
                best_group = i

        # Ajouter la personne au meilleur groupe
        groups[best_group].append(person)
        group_counts[best_group]['Genre'][person['Genre']] += 1
        group_counts[best_group]['Stage'][person['Stage']] += 1

    # Convertir les groupes en DataFrames
    group_dfs = [pd.DataFrame(group) for group in groups]

    return group_dfs


# Diviser en trois groupes
groups = split_into_balanced_groups(stagiaires)

# Afficher les statistiques pour chaque groupe
for i, group in enumerate(groups, 1):
    print(f"\nGroupe {i}:")
    print(f"Nombre total de personnes: {len(group)}")
    print("\nDistribution par sexe:")
    print(group['Genre'].value_counts())
    print("\nDistribution par type de stage:")
    print(group['Stage'].value_counts())
    print("\nListe des personnes:")
    print(group[['Nom', 'Genre', 'Stage']])
    print("\n" + "=" * 50)

# Optionnel : sauvegarder les groupes dans des fichiers CSV séparés
for i, group in enumerate(groups, 1):
    group.to_csv(f'groupe_{i}.csv', index=False)
