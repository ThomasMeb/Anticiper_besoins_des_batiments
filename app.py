"""
🏢 Seattle Building Energy & CO2 Predictor
Application Streamlit pour prédire la consommation énergétique et les émissions CO2
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="Seattle CO2 Predictor",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CHARGEMENT DES DONNÉES ET MODÈLE
# =============================================================================

@st.cache_data
def load_data():
    """Charge les données pour les statistiques et références."""
    data_path = Path("data/data.csv")
    if data_path.exists():
        return pd.read_csv(data_path, index_col=0)

    # Fallback sur données brutes
    raw_path = Path("data/2016_Building_Energy_Benchmarking.csv")
    if raw_path.exists():
        return pd.read_csv(raw_path)

    return None

@st.cache_resource
def load_model():
    """Charge le modèle pré-entraîné ou crée un modèle simple."""
    import joblib
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler

    model_path = Path("models/random_forest_best.pkl")

    if model_path.exists():
        return joblib.load(model_path)

    # Créer un modèle simple si pas de modèle sauvegardé
    data = load_data()
    if data is not None:
        # Préparation simplifiée
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()

        # Identifier la target
        target_candidates = ['SiteEnergyUseWN(kBtu)', 'SiteEnergyUse(kBtu)']
        target = None
        for t in target_candidates:
            if t in numeric_cols:
                target = t
                break

        if target:
            feature_cols = [c for c in numeric_cols if c != target and 'GHG' not in c and 'EUI' not in c]
            X = data[feature_cols].dropna()
            y = data.loc[X.index, target]

            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            rf = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
            rf.fit(X_scaled, y)

            return {
                'model': rf,
                'scaler': scaler,
                'feature_names': feature_cols,
                'target': target
            }

    return None

# =============================================================================
# INTERFACE UTILISATEUR
# =============================================================================

def main():
    # Header
    st.title("🏢 Prédiction Énergétique des Bâtiments de Seattle")
    st.markdown("""
    > **Objectif** : Prédire la consommation énergétique et les émissions CO2 des bâtiments
    non résidentiels pour aider Seattle à atteindre la neutralité carbone d'ici 2050.
    """)

    # Sidebar - Inputs
    st.sidebar.header("📊 Caractéristiques du Bâtiment")

    # Inputs principaux
    property_gfa = st.sidebar.number_input(
        "Surface totale (sq ft)",
        min_value=1000,
        max_value=2000000,
        value=50000,
        step=1000,
        help="Surface totale du bâtiment en pieds carrés"
    )

    floors = st.sidebar.slider(
        "Nombre d'étages",
        min_value=1,
        max_value=100,
        value=5,
        help="Nombre d'étages du bâtiment"
    )

    age = st.sidebar.slider(
        "Âge du bâtiment (années)",
        min_value=0,
        max_value=150,
        value=30,
        help="Âge du bâtiment depuis sa construction"
    )

    energy_star = st.sidebar.slider(
        "Score ENERGY STAR",
        min_value=1,
        max_value=100,
        value=50,
        help="Score de performance énergétique (1-100)"
    )

    building_type = st.sidebar.selectbox(
        "Type de bâtiment",
        options=[
            "Office (Small/Mid)",
            "Office (Large)",
            "Hotel",
            "Retail Store",
            "Warehouse",
            "K-12 School",
            "University",
            "Hospital",
            "Other"
        ]
    )

    # Colonnes principales
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔋 Prédiction de Consommation")

        # Calcul simplifié basé sur des heuristiques
        # (En production, on utiliserait le vrai modèle)
        base_consumption = property_gfa * 50  # kBtu/sqft moyen

        # Ajustements
        floor_factor = 1 + (floors - 1) * 0.02
        age_factor = 1 + (age / 100) * 0.3
        energy_star_factor = 2 - (energy_star / 100)

        # Type de bâtiment
        type_factors = {
            "Office (Small/Mid)": 0.9,
            "Office (Large)": 1.1,
            "Hotel": 1.3,
            "Retail Store": 0.85,
            "Warehouse": 0.6,
            "K-12 School": 0.8,
            "University": 1.0,
            "Hospital": 1.5,
            "Other": 1.0
        }
        type_factor = type_factors.get(building_type, 1.0)

        predicted_energy = base_consumption * floor_factor * age_factor * energy_star_factor * type_factor

        # Affichage avec métrique
        st.metric(
            label="Consommation Énergétique Estimée",
            value=f"{predicted_energy/1e6:.2f} M kBtu/an",
            delta=f"{(energy_star_factor - 1) * 100:.1f}% vs moyenne" if energy_star != 50 else None,
            delta_color="inverse"
        )

        # Gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=predicted_energy / 1e6,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Consommation (M kBtu)"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 20], 'color': "lightgreen"},
                    {'range': [20, 50], 'color': "yellow"},
                    {'range': [50, 100], 'color': "salmon"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 70
                }
            }
        ))
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col2:
        st.subheader("🌿 Estimation des Émissions CO2")

        # Estimation CO2 basée sur consommation
        # Facteur d'émission moyen pour mix énergétique Seattle
        emission_factor = 0.0001  # tonnes CO2 / kBtu (approximatif)
        predicted_co2 = predicted_energy * emission_factor

        st.metric(
            label="Émissions CO2 Estimées",
            value=f"{predicted_co2:.1f} tonnes/an",
            delta=f"{(1 - energy_star/100) * 50:.1f}% économisable" if energy_star < 75 else "Excellent!",
            delta_color="inverse" if energy_star < 75 else "normal"
        )

        # Comparaison avec équivalents
        st.markdown("##### 🌳 Équivalents environnementaux")

        trees_equivalent = predicted_co2 * 45  # ~45 arbres par tonne CO2/an
        cars_equivalent = predicted_co2 / 4.6  # ~4.6 tonnes CO2/voiture/an

        equiv_col1, equiv_col2 = st.columns(2)
        with equiv_col1:
            st.metric("🌲 Arbres nécessaires", f"{trees_equivalent:.0f}")
        with equiv_col2:
            st.metric("🚗 Équivalent voitures", f"{cars_equivalent:.1f}")

    # Section analyse
    st.markdown("---")
    st.subheader("📈 Analyse des Facteurs d'Impact")

    # Graphique d'impact des features
    factors = {
        'Surface (GFA)': property_gfa / 50000,
        'Étages': floors / 10,
        'Âge': age / 50,
        'Score ENERGY STAR': (100 - energy_star) / 50,
        'Type de bâtiment': type_factor
    }

    fig_factors = px.bar(
        x=list(factors.keys()),
        y=list(factors.values()),
        labels={'x': 'Facteur', 'y': 'Impact relatif'},
        title="Impact relatif des caractéristiques sur la consommation",
        color=list(factors.values()),
        color_continuous_scale='RdYlGn_r'
    )
    fig_factors.update_layout(showlegend=False)
    st.plotly_chart(fig_factors, use_container_width=True)

    # Recommandations
    st.markdown("---")
    st.subheader("💡 Recommandations")

    recommendations = []

    if energy_star < 50:
        recommendations.append("⚠️ **Score ENERGY STAR faible** : Envisagez un audit énergétique et des rénovations.")

    if age > 50:
        recommendations.append("🏗️ **Bâtiment ancien** : La modernisation des systèmes HVAC pourrait réduire la consommation de 20-30%.")

    if property_gfa > 100000:
        recommendations.append("📊 **Grand bâtiment** : Implémentez un système de gestion de l'énergie (BMS) pour optimiser la consommation.")

    if building_type in ["Hotel", "Hospital"]:
        recommendations.append("🔄 **Usage intensif** : Considérez la cogénération ou les panneaux solaires pour réduire l'empreinte carbone.")

    if not recommendations:
        recommendations.append("✅ **Bon profil énergétique** : Continuez à monitorer et optimiser votre consommation.")

    for rec in recommendations:
        st.markdown(rec)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>🏢 Seattle Building Energy Predictor |
        <a href='https://github.com/ThomasMeb/Anticiper_besoins_des_batiments'>GitHub</a> |
        Données: Seattle Open Data 2016</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
