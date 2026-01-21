# Guide de Configuration Git et GitHub

Ce guide vous accompagne pour initialiser Git et pousser votre projet sur GitHub.

## Prérequis

1. Git installé sur votre machine
2. Compte GitHub créé
3. Terminal/Command Prompt ouvert dans le dossier du projet

## Étape 1 : Initialiser Git (si pas déjà fait)

```bash
# Vérifier si Git est déjà initialisé
git status

# Si erreur "not a git repository", initialiser :
git init
```

## Étape 2 : Configuration Git (première fois uniquement)

```bash
# Configurer votre nom et email
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"

# Vérifier la configuration
git config --list
```

## Étape 3 : Ajouter les fichiers au suivi Git

```bash
# Ajouter tous les fichiers (le .gitignore exclura automatiquement les fichiers non désirés)
git add .

# Vérifier les fichiers ajoutés
git status
```

## Étape 4 : Créer le premier commit

```bash
git commit -m "Initial commit - Projet prédiction émissions CO2 Seattle

- Structure BMAD appliquée
- README complet et professionnel
- Notebooks organisés et renommés
- Documentation complète (ROADMAP.md)
- Configuration projet (requirements.txt, .gitignore)"
```

## Étape 5 : Créer un repository sur GitHub

1. Aller sur https://github.com
2. Cliquer sur le bouton "+" en haut à droite → "New repository"
3. Remplir les informations :
   - **Repository name** : `seattle-co2-emissions-prediction` (ou autre nom)
   - **Description** : "Prédiction des émissions de CO2 et consommation énergétique des bâtiments de Seattle avec Machine Learning"
   - **Public** ou **Private** (recommandé: Public pour portfolio)
   - **NE PAS** cocher "Initialize with README" (on a déjà le nôtre)
4. Cliquer sur "Create repository"

## Étape 6 : Lier le repository local au repository GitHub

```bash
# Remplacer YOUR-USERNAME et REPO-NAME par vos valeurs
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git

# Vérifier que le remote est bien ajouté
git remote -v
```

**Exemple** :
```bash
git remote add origin https://github.com/thomasmebarki/seattle-co2-emissions-prediction.git
```

## Étape 7 : Renommer la branche principale en "main"

```bash
# Renommer master en main (convention moderne)
git branch -M main
```

## Étape 8 : Pousser le code vers GitHub

```bash
# Premier push (avec -u pour définir la branche upstream)
git push -u origin main
```

**Note** : Si vous êtes invité à vous authentifier :
- **Option 1** : Utiliser votre nom d'utilisateur et mot de passe GitHub
- **Option 2** (recommandé) : Utiliser un Personal Access Token (PAT)
  - Aller dans GitHub → Settings → Developer settings → Personal access tokens → Generate new token
  - Cocher "repo" pour accès complet aux repositories
  - Copier le token et l'utiliser comme mot de passe

## Étape 9 : Vérifier sur GitHub

1. Rafraîchir la page de votre repository sur GitHub
2. Vérifier que tous les fichiers sont bien présents
3. Le README.md devrait s'afficher automatiquement en bas de page

## Commandes Git Utiles pour la Suite

### Ajouter des modifications

```bash
# Vérifier les fichiers modifiés
git status

# Ajouter tous les fichiers modifiés
git add .

# Ou ajouter un fichier spécifique
git add README.md

# Commiter avec un message descriptif
git commit -m "docs: mise à jour du README avec badges"

# Pousser vers GitHub
git push
```

### Types de commits conventionnels

```bash
git commit -m "feat: ajout du notebook de synthèse des résultats"
git commit -m "fix: correction du chemin vers les données"
git commit -m "docs: amélioration de la documentation"
git commit -m "refactor: nettoyage du code de preprocessing"
git commit -m "style: amélioration du formatage des notebooks"
```

### Annuler des modifications (avant commit)

```bash
# Annuler les modifications d'un fichier
git checkout -- nom_du_fichier

# Annuler toutes les modifications
git reset --hard
```

### Voir l'historique

```bash
# Voir l'historique des commits
git log

# Version courte
git log --oneline

# Version graphique
git log --oneline --graph --all
```

## Améliorer votre Repository GitHub

### Ajouter des badges au README

En haut de votre README.md, ajoutez :

```markdown
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-completed-success.svg)
```

### Ajouter une License

1. Sur GitHub, cliquez sur "Add file" → "Create new file"
2. Nommez le fichier "LICENSE"
3. Cliquez sur "Choose a license template"
4. Sélectionnez "MIT License" (recommandé pour projets éducatifs)
5. Commit le fichier

### Ajouter des Topics

Sur la page de votre repository GitHub :
1. Cliquer sur l'icône d'engrenage à côté de "About"
2. Ajouter des topics : `machine-learning`, `data-science`, `python`, `scikit-learn`, `seattle`, `carbon-emissions`, `energy-prediction`

## Workflow Recommandé

```bash
# Chaque fois que vous travaillez sur le projet :

# 1. Récupérer les dernières modifications (si vous travaillez sur plusieurs machines)
git pull

# 2. Faire vos modifications dans les fichiers

# 3. Vérifier ce qui a changé
git status
git diff

# 4. Ajouter les modifications
git add .

# 5. Commiter avec un message descriptif
git commit -m "type: description claire de la modification"

# 6. Pousser vers GitHub
git push
```

## Troubleshooting

### Erreur : "fatal: not a git repository"
→ Vous n'êtes pas dans le bon dossier ou Git n'est pas initialisé
```bash
git init
```

### Erreur : "failed to push some refs"
→ Le repository distant a des changements que vous n'avez pas localement
```bash
git pull --rebase origin main
git push
```

### Erreur d'authentification
→ Utilisez un Personal Access Token au lieu du mot de passe

### Fichiers sensibles ajoutés par erreur
```bash
# Retirer du suivi Git sans supprimer le fichier
git rm --cached nom_du_fichier

# Ajouter au .gitignore
echo "nom_du_fichier" >> .gitignore

# Commiter la modification
git commit -m "fix: retrait fichier sensible du suivi Git"
git push
```

## Ressources

- [Documentation Git officielle](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Markdown Guide](https://www.markdownguide.org/)

---

**Bon courage avec votre projet ! 🚀**
