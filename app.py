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
import joblib
import shap

# Configuration de la page
st.set_page_config(
    page_title="Seattle CO2 Predictor",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CHARGEMENT DES MODÈLES ML
# =============================================================================

@st.cache_resource
def load_models():
    """Charge les modèles ML pré-entraînés."""
    models = {}

    # Modèle énergie
    energy_model_path = Path("models/energy_model.joblib")
    energy_scaler_path = Path("models/energy_scaler.joblib")
    energy_features_path = Path("models/energy_features.joblib")

    if energy_model_path.exists():
        models['energy_model'] = joblib.load(energy_model_path)
        models['energy_scaler'] = joblib.load(energy_scaler_path)
        models['energy_features'] = joblib.load(energy_features_path)

    # Modèle CO2
    co2_model_path = Path("models/co2_model.joblib")
    co2_scaler_path = Path("models/co2_scaler.joblib")

    if co2_model_path.exists():
        models['co2_model'] = joblib.load(co2_model_path)
        models['co2_scaler'] = joblib.load(co2_scaler_path)

    return models if models else None

def prepare_features(property_gfa, floors, age, energy_star, building_type, feature_names):
    """Prépare les features pour la prédiction."""
    # Features structurelles de base
    features = {
        'Age': age,
        'NumberofBuildings': 1,
        'NumberofFloors': floors,
        'PropertyGFATotal': property_gfa,
        'PropertyGFAParking_Pct': 5.0,  # Valeur moyenne
        'PropertyGFABuilding_Pct': 95.0,  # Valeur moyenne
        'LargestPropertyUseTypeGFA': property_gfa * 0.8,  # 80% de la surface totale
        'ENERGYSTARScore': energy_star
    }

    # Mapping des types de bâtiments vers les colonnes one-hot
    type_mapping = {
        "Office (Small/Mid)": "PropType_Small- and Mid-Sized Office",
        "Office (Large)": "PropType_Large Office",
        "Hotel": "PropType_Hotel",
        "Retail Store": "PropType_Retail Store",
        "Warehouse": "PropType_Warehouse",
        "K-12 School": "PropType_K-12 School",
        "University": "PropType_University",
        "Hospital": "PropType_Other",
        "Other": "PropType_Other"
    }

    # Initialiser toutes les features à 0
    all_features = {name: 0 for name in feature_names}

    # Remplir les features structurelles
    for key, value in features.items():
        if key in all_features:
            all_features[key] = value

    # Activer le type de bâtiment approprié
    prop_type_col = type_mapping.get(building_type, "PropType_Other")
    if prop_type_col in all_features:
        all_features[prop_type_col] = 1

    # Créer le DataFrame dans l'ordre correct
    df = pd.DataFrame([all_features])[feature_names]
    return df

@st.cache_resource
def get_shap_explainer(_model):
    """Crée l'explainer SHAP pour le modèle (caché pour performance)."""
    return shap.TreeExplainer(_model)

def compute_shap_values(explainer, X_scaled, feature_names):
    """Calcule les valeurs SHAP pour une prédiction."""
    shap_values = explainer.shap_values(X_scaled)

    # Créer un DataFrame avec les valeurs SHAP
    shap_df = pd.DataFrame({
        'Feature': feature_names,
        'SHAP Value': shap_values[0],
        'Abs SHAP': np.abs(shap_values[0])
    }).sort_values('Abs SHAP', ascending=False)

    return shap_df, explainer.expected_value

def create_shap_waterfall_plot(shap_df, expected_value, predicted_value):
    """Crée un waterfall plot SHAP avec Plotly."""
    # Top 10 features
    top_features = shap_df.head(10).copy()
    top_features = top_features.iloc[::-1]  # Inverser pour affichage

    colors = ['#ff6b6b' if v > 0 else '#4ecdc4' for v in top_features['SHAP Value']]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=top_features['SHAP Value'],
        y=top_features['Feature'],
        orientation='h',
        marker_color=colors,
        text=[f"{v:+.2f}" for v in top_features['SHAP Value']],
        textposition='outside'
    ))

    # Gérer le cas où expected_value est un array
    base_value = expected_value[0] if hasattr(expected_value, '__len__') else expected_value

    fig.update_layout(
        title=f"Impact des features sur la prédiction (base: {base_value/1e6:.2f}M)",
        xaxis_title="Impact SHAP (kBtu)",
        yaxis_title="",
        height=400,
        showlegend=False
    )

    return fig

def get_recommendations(energy_star, age, property_gfa, building_type):
    """Génère des recommandations basées sur les caractéristiques du bâtiment."""
    recommendations = []

    if energy_star < 50:
        recommendations.append(
            "⚠️ **Score ENERGY STAR faible** : Envisagez un audit énergétique et des rénovations."
        )

    if age > 50:
        recommendations.append(
            "🏗️ **Bâtiment ancien** : La modernisation des systèmes HVAC pourrait réduire la consommation de 20-30%."
        )

    if property_gfa > 100000:
        recommendations.append(
            "📊 **Grand bâtiment** : Implémentez un système de gestion de l'énergie (BMS) pour optimiser la consommation."
        )

    if building_type in ["Hotel", "Hospital"]:
        recommendations.append(
            "🔄 **Usage intensif** : Considérez la cogénération ou les panneaux solaires pour réduire l'empreinte carbone."
        )

    if not recommendations:
        recommendations.append(
            "✅ **Bon profil énergétique** : Continuez à monitorer et optimiser votre consommation."
        )

    return recommendations


def predict_with_fallback(models, property_gfa, floors, age, energy_star, building_type):
    """
    Effectue une prédiction avec le modèle ML ou utilise un fallback heuristique.

    Returns:
        tuple: (predicted_energy, predicted_co2, using_ml, X, X_scaled, feature_names)
    """
    if models and 'energy_model' in models:
        feature_names = models['energy_features']
        X = prepare_features(property_gfa, floors, age, energy_star, building_type, feature_names)
        X_scaled = models['energy_scaler'].transform(X)
        predicted_energy = models['energy_model'].predict(X_scaled)[0]
        predicted_co2 = models['co2_model'].predict(models['co2_scaler'].transform(X))[0]
        return predicted_energy, predicted_co2, True, X, X_scaled, feature_names

    # Fallback heuristique si modèles non disponibles
    base_consumption = property_gfa * 50
    floor_factor = 1 + (floors - 1) * 0.02
    age_factor = 1 + (age / 100) * 0.3
    energy_star_factor = 2 - (energy_star / 100)
    type_factors = {
        "Office (Small/Mid)": 0.9, "Office (Large)": 1.1, "Hotel": 1.3,
        "Retail Store": 0.85, "Warehouse": 0.6, "K-12 School": 0.8,
        "University": 1.0, "Hospital": 1.5, "Other": 1.0
    }
    type_factor = type_factors.get(building_type, 1.0)
    predicted_energy = base_consumption * floor_factor * age_factor * energy_star_factor * type_factor
    predicted_co2 = predicted_energy * 0.0001
    return predicted_energy, predicted_co2, False, None, None, None


def create_feature_importance_plot(model, feature_names):
    """Crée un graphique d'importance des features basé sur le modèle."""
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False).head(10)

    # Renommer les features pour plus de clarté
    name_mapping = {
        'PropertyGFATotal': 'Surface totale',
        'LargestPropertyUseTypeGFA': 'Surface usage principal',
        'ENERGYSTARScore': 'Score ENERGY STAR',
        'Age': 'Âge du bâtiment',
        'NumberofFloors': "Nombre d'étages",
        'PropertyGFABuilding_Pct': '% Surface bâtiment',
        'PropertyGFAParking_Pct': '% Surface parking',
        'NumberofBuildings': 'Nombre de bâtiments'
    }

    importance_df['Feature_Display'] = importance_df['Feature'].map(
        lambda x: name_mapping.get(x, x.replace('PropType_', '').replace('District_', ''))
    )

    fig = px.bar(
        importance_df,
        x='Importance',
        y='Feature_Display',
        orientation='h',
        title="🔍 Importance des Features (Random Forest)",
        color='Importance',
        color_continuous_scale='Viridis'
    )
    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        showlegend=False,
        height=400
    )

    return fig

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

    # Charger les modèles
    models = load_models()

    # Prédiction avec les vrais modèles ML ou fallback heuristique
    predicted_energy, predicted_co2, using_ml, X, X_scaled, feature_names = predict_with_fallback(
        models, property_gfa, floors, age, energy_star, building_type
    )

    # Colonnes principales
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔋 Prédiction de Consommation")

        # Affichage avec métrique
        st.metric(
            label="Consommation Énergétique Estimée",
            value=f"{predicted_energy/1e6:.2f} M kBtu/an",
            delta="🤖 ML Model" if using_ml else "📊 Heuristique"
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

        st.metric(
            label="Émissions CO2 Estimées",
            value=f"{predicted_co2:.1f} tonnes/an",
            delta="🤖 ML Model" if using_ml else "📊 Heuristique"
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

    # Facteurs d'impact par type de bâtiment
    type_impact = {"Office (Small/Mid)": 0.9, "Office (Large)": 1.1, "Hotel": 1.3,
                   "Retail Store": 0.85, "Warehouse": 0.6, "K-12 School": 0.8,
                   "University": 1.0, "Hospital": 1.5, "Other": 1.0}

    # Graphique d'impact des features
    factors = {
        'Surface (GFA)': property_gfa / 50000,
        'Étages': floors / 10,
        'Âge': age / 50,
        'Score ENERGY STAR': (100 - energy_star) / 50,
        'Type de bâtiment': type_impact.get(building_type, 1.0)
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

    # Section SHAP - Interprétabilité ML
    if using_ml:
        st.markdown("---")
        st.subheader("🔬 Interprétabilité du Modèle (SHAP)")

        st.markdown("""
        > **SHAP** (SHapley Additive exPlanations) permet de comprendre comment chaque caractéristique
        influence la prédiction du modèle de Machine Learning.
        """)

        shap_col1, shap_col2 = st.columns(2)

        with shap_col1:
            # Feature Importance globale
            fig_importance = create_feature_importance_plot(
                models['energy_model'],
                feature_names
            )
            st.plotly_chart(fig_importance, use_container_width=True)

        with shap_col2:
            # SHAP values pour cette prédiction
            try:
                explainer = get_shap_explainer(models['energy_model'])
                shap_df, expected_value = compute_shap_values(
                    explainer, X_scaled, feature_names
                )
                fig_shap = create_shap_waterfall_plot(
                    shap_df, expected_value, predicted_energy
                )
                st.plotly_chart(fig_shap, use_container_width=True)
            except Exception as e:
                st.info("📊 Analyse SHAP individuelle non disponible")

        # Insights SHAP
        st.markdown("##### 💡 Insights clés du modèle")
        st.markdown("""
        - **Surface totale (GFA)** : Principal prédicteur (~40% d'importance)
        - **Score ENERGY STAR** : Impact significatif sur l'efficacité
        - **Âge du bâtiment** : Les bâtiments anciens consomment plus
        - **Type de bâtiment** : Hôpitaux et hôtels ont les plus fortes consommations
        """)

    # Recommandations
    st.markdown("---")
    st.subheader("💡 Recommandations")

    recommendations = get_recommendations(energy_star, age, property_gfa, building_type)
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
