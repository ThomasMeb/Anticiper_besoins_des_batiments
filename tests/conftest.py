"""
Fixtures partagées pour les tests.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Ajouter le dossier parent au path pour importer app
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def sample_features():
    """Features de test pour un bâtiment."""
    return {
        'property_gfa': 50000,
        'floors': 5,
        'age': 30,
        'energy_star': 50,
        'building_type': 'Office (Small/Mid)'
    }


@pytest.fixture
def feature_names():
    """Liste des noms de features attendues par le modèle."""
    return [
        'Age', 'NumberofBuildings', 'NumberofFloors',
        'PropertyGFATotal', 'PropertyGFAParking_Pct', 'PropertyGFABuilding_Pct',
        'LargestPropertyUseTypeGFA', 'ENERGYSTARScore',
        'PropType_Small- and Mid-Sized Office', 'PropType_Large Office',
        'PropType_Hotel', 'PropType_Retail Store', 'PropType_Warehouse',
        'PropType_K-12 School', 'PropType_University', 'PropType_Other'
    ]


@pytest.fixture
def models_path():
    """Chemin vers le dossier des modèles."""
    return Path(__file__).parent.parent / "models"
