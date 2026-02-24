# Proyecto: Recomendador de Películas, Series y Anime

**Autor:** Marco  
**Fecha:** Febrero 2026  
**Objetivo:** Construir un sistema de recomendación híbrido que combine filtrado colaborativo, basado en contenido y popularidad ponderada, utilizando datos reales de películas del dataset The Movies Dataset (Kaggle).

## Tecnologías utilizadas
- Python 3.13
- Librerías principales: pandas, numpy, scikit-learn, implicit (BPR), matplotlib, seaborn
- Despliegue interactivo: Streamlit

## Estructura del proyecto
Recomendador-de-películas-series-anime/
├── movies_metadata.csv           # Dataset principal (metadata de películas)
├── credits.csv                   # Cast y crew
├── links_small.csv               # Mapeo movieId ↔ tmdbId
├── ratings_small.csv             # Calificaciones de usuarios (MovieLens)
├── app.py                        # Aplicación interactiva en Streamlit
├── recomendacion_contenido.ipynb # Notebook completo (ETL → EDA → Modelado → Recomendadores)
├── df_content_final.pkl          # DataFrame procesado
├── bpr_model_final.pkl           # Modelo BPR entrenado
├── user_map.pkl                  # Mapas de índices para collaborative
├── item_map.pkl
├── inv_item_map.pkl
├── interactions.pkl
└── README.md
text## Flujo del proyecto

1. **ETL y limpieza**  
   - Carga y tratamiento de nulos (imputación por mediana/moda/placeholders)  
   - Conversión de tipos (fechas → datetime, categóricas → category, enteros nullable)  
   - Parseo de columnas JSON-like (genres → lista de nombres)  
   - Eliminación de duplicados por id y título+año  

2. **EDA**  
   - Univariado: distribuciones, outliers (runtime > 400 min eliminados)  
   - Bivariado: correlaciones Spearman, boxplots por género, tendencias temporales  

3. **Preparación**  
   - Filtro conservador: solo Released, runtime 10–400 min, ≥5 votos  
   - Score de popularidad ponderado (fórmula IMDb-like)  

4. **Modelado**  
   - **Popularidad ponderada** (baseline)  
   - **Content-based** (TF-IDF sobre overview + géneros ×3 + tagline + título + director + top 3 actores)  
   - **Híbrido content** (similitud coseno × score ponderado)  
   - **Collaborative filtering** (implicit BPR – Bayesian Personalized Ranking)  
     - Feedback implícito: rating ≥3.5 → confianza 1.0  
     - Métricas implícitas de ranking (top-N coherente con gusto del usuario)

5. **Despliegue**  
   - App interactiva en Streamlit:  
     - Popularidad ponderada  
     - Recomendaciones por título (content-based)  
     - Recomendaciones personalizadas por userId (collaborative)  
     - Híbrido (combinado)

## Resultados destacados
- Dataset final filtrado: ~29.8k películas (después de limpieza y filtros)  
- Subconjunto para content-based: ~9.1k películas con ≥50 votos  
- Cobertura de cruce ratings-movieId: ~63% (suficiente para collaborative)  
- Recomendaciones collaborative (BPR) para userId=1:  
  - Top: Pulp Fiction, Shawshank Redemption, Forrest Gump, Star Wars, Back to the Future  
  - Coherencia alta con películas ya calificadas por el usuario (clásicos 80s-90s, culto, aventura/sci-fi, crimen/thriller)

## Próximos pasos / mejoras posibles
- Incorporar keywords.csv para enriquecer content-based  
- Agregar evaluación offline (NDCG@10, Precision@K) en collaborative  
- Fine-tuning de hiperparámetros en BPR  
- Visualización de pósters (poster_path) en la app Streamlit  
- Deploy público (Streamlit Cloud o Hugging Face Spaces)

## Cómo ejecutar localmente
1. Clonar repositorio
2. Crear entorno virtual: `python -m venv .venv`
3. Activar: `.venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar app: `streamlit run app.py`

¡Contribuciones y feedback bienvenidos!