# app.py - Recomendador completo (versión autónoma)
import streamlit as st
import pandas as pd
import pickle

# =============================================
# Cargar todos los componentes necesarios
# =============================================
try:
    df_content = pd.read_pickle('df_content_final.pkl')
    model = pickle.load(open('bpr_model_final.pkl', 'rb'))
    user_map = pickle.load(open('user_map.pkl', 'rb'))
    item_map = pickle.load(open('item_map.pkl', 'rb'))
    inv_item_map = pickle.load(open('inv_item_map.pkl', 'rb'))
    interactions = pickle.load(open('interactions.pkl', 'rb'))
    st.success("Todos los datos y modelo cargados correctamente.")
except Exception as e:
    st.error(f"Error al cargar archivos: {e}")
    st.stop()

# Calcular C y m para popularidad ponderada (independiente del notebook)
C = df_content['vote_count'].quantile(0.90)   # mínimo votos para entrar al top
m = df_content['vote_count'].median()         # mediana de votos

# Asegurar que 'score' exista (recalcular si falta)
if 'score' not in df_content.columns:
    def weighted_rating(x):
        v = x['vote_count']
        R = x['vote_average']
        return (v / (v + m) * R) + (m / (v + m) * C)
    df_content['score'] = df_content.apply(weighted_rating, axis=1)
    st.info("Columna 'score' recalculada para popularidad ponderada.")

# =============================================
# Funciones del recomendador
# =============================================
def top_populares(n=10, min_votes=C):
    top = df_content[df_content['vote_count'] >= min_votes]\
          .sort_values('score', ascending=False)\
          .head(n)
    return top[['title', 'release_year', 'vote_average', 'vote_count', 'popularity', 'score']]

def recommend(user_id=None, top_n=10):
    if user_id and user_id in user_map:
        user_internal = user_map[user_id]
        rec = model.recommend(
            userid=user_internal,
            user_items=interactions[user_internal],
            N=top_n,
            filter_already_liked_items=True
        )
        top_movie_ids = [inv_item_map[iid] for iid in rec[0]]
        top_scores = rec[1]
        rec_df = df_content[df_content['movieId'].isin(top_movie_ids)].copy()
        rec_df['score'] = top_scores
        return rec_df.sort_values('score', ascending=False)[['title', 'release_year', 'vote_average', 'genres_list', 'score']].head(top_n)
    else:
        # Fallback a popularidad si no hay user_id válido
        return top_populares(n=top_n)

# =============================================
# Interfaz de usuario
# =============================================
st.title("Recomendador de Películas / Series / Anime")
st.write("Proyecto 3 - Recomendaciones basadas en popularidad y preferencias de usuarios")

option = st.selectbox(
    "Tipo de recomendación",
    ("Popularidad ponderada", "Personalizada por usuario (collaborative)")
)

top_n = st.slider("Número de recomendaciones", min_value=5, max_value=20, value=10)

if option == "Popularidad ponderada":
    st.subheader("Top películas por popularidad ponderada")
    st.dataframe(top_populares(n=top_n))

elif option == "Personalizada por usuario (collaborative)":
    user_id = st.number_input("Ingresa userId", min_value=1, max_value=671, value=1)
    if st.button("Generar recomendaciones"):
        rec = recommend(user_id=user_id, top_n=top_n)
        st.subheader(f"Recomendaciones personalizadas para userId {user_id}")
        st.dataframe(rec)

st.markdown("**Proyecto 3** - Recomendador de películas / series / anime por Marco")