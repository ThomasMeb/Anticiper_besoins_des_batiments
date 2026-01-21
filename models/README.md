# 📦 Modèles Sauvegardés

Ce dossier contient les modèles ML entraînés et sauvegardés.

## Génération des Modèles

Pour générer le modèle Random Forest, exécutez le notebook `02_prediction_energy.ipynb` ou utilisez le script suivant :

```python
import joblib
from sklearn.ensemble import RandomForestRegressor

# Après entraînement du modèle rf...
joblib.dump({
    'model': rf,
    'scaler': scaler,
    'feature_names': list(X.columns),
    'target': 'SiteEnergyUseWN(kBtu)'
}, 'models/random_forest_best.pkl')
```

## Chargement des Modèles

```python
import joblib

# Charger le modèle
model_data = joblib.load('models/random_forest_best.pkl')
rf = model_data['model']
scaler = model_data['scaler']
feature_names = model_data['feature_names']

# Faire une prédiction
X_new_scaled = scaler.transform(X_new)
prediction = rf.predict(X_new_scaled)
```

## Fichiers

| Fichier | Description | Taille |
|---------|-------------|--------|
| `random_forest_best.pkl` | Meilleur modèle RF + scaler | ~5 MB |

---

*Note: Les fichiers .pkl sont ignorés par git pour éviter les fichiers volumineux.*
