def extraire_valeur_etalonnage(ligne):
    """Extraire le premier et le dernier chiffre d’une ligne et les combiner en un nombre à deux chiffres."""
    # Trouver tous les chiffres de la ligne
    vals = [char for char in ligne if char.isdigit()]
    
    if not vals:
        return 0
        
    return int(vals[0] + vals[-1])

def calculer_etalonnage_total(input_text):
    """Calculer la somme des valeurs d'étalonnage pour toutes les lignes."""
    # Diviser l'entrée en lignes
    lines = input_text.strip().split('\n')
    
    # Calculer la somme des valeurs d'étalonnage
    total = sum(extraire_valeur_etalonnage(line) for line in lines)
    
    return total

# Lire le fichier et calculer le résultat
try:
    # Ouvrir et lire le fichier 'document.txt'
    with open('document.txt', 'r') as fichier:
        contenu = fichier.read()
        resultat = calculer_etalonnage_total(contenu)
        print(f"La somme totale des valeurs d'étalonnage est : {resultat}")
except FileNotFoundError:
    print("Erreur : Le fichier 'document.txt' n'a pas été trouvé")
except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")
    