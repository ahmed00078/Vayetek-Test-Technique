# Vayetek-Test-Technique(Calculateur de Valeurs d'Étalonnage)

Ce projet contient un script Python qui calcule la somme des valeurs d'étalonnage à partir d'un fichier texte contenant des lignes de caractères. Chaque valeur d'étalonnage est formée en combinant le premier et le dernier chiffre de chaque ligne.

## Description

Le script analyse un fichier texte ligne par ligne et :
1. Extrait tous les chiffres de chaque ligne
2. Combine le premier et le dernier chiffre pour former un nombre à deux chiffres
3. Additionne tous ces nombres pour obtenir la somme totale

## Prérequis

- Python 3

## Structure des Fichiers

```
.
├── calibration.py    # Script principal
├── document.txt      # Fichier d'entrée contenant les lignes à analyser
└── README.md         # Ce fichier
```

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/ahmed00078/Vayetek-Test-Technique.git
cd Vayetek-Test-Technique
```

2. Assurez-vous que votre fichier d'entrée `document.txt` est présent dans le même dossier que le script.

## Utilisation

1. Placez votre fichier de données dans le même dossier que le script sous le nom `document.txt`
2. Exécutez le script :
```bash
python main.py
```

## Format du Fichier d'Entrée

Le fichier d'entrée (`document.txt`) doit contenir une ligne par valeur à analyser. Exemple :
```
ckmb52fldxkseven3fkjgcbzmnr7
gckhqpb6twoqnjxqplthree2fourkspnsnzxlz1
2onetwocrgbqm7
```

## Exemple de Résultat

Pour l'entrée suivante :
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```
Le script calculera :
- Ligne 1 : 12
- Ligne 2 : 38
- Ligne 3 : 15
- Ligne 4 : 77
Somme totale : 142

## Gestion des Erreurs

Le script gère les cas suivants :
- Fichier non trouvé
- Lignes sans chiffres
- Erreurs générales de lecture de fichier

## Auteur

Ahmed Sidi Mohamed

---

**Note :** Ce projet a été créé dans le cadre d'un test technique pour Vayetek.