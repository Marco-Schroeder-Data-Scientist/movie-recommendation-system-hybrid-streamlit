RESUMEN EJECUTIVO
Sistema de Recomendacion Hibrido de Peliculas
=============================================

DESCRIPCION
-----------
Proyecto end-to-end de recomendacion de peliculas que cubre todo el flujo de
trabajo en ciencia de datos: ETL sobre datos reales complejos, EDA completo,
feature engineering, modelado con multiples enfoques (popularidad, content-based,
collaborative filtering y hibrido) y despliegue de una aplicacion interactiva
en Streamlit.

Dataset utilizado: The Movies Dataset (TMDB + MovieLens, Kaggle)
Dataset original: ~45k peliculas


METODOLOGIA
-----------
ETL y Limpieza:
  - Tratamiento de nulos (imputacion por mediana/moda/placeholders)
  - Conversion de tipos (fechas, categoricas, enteros nullable)
  - Parseo de columnas JSON-like (genres → lista de nombres)
  - Eliminacion de duplicados por id y por titulo+año
  - Filtro conservador: solo Released, runtime 10-400 min, >= 5 votos

EDA:
  - Analisis univariado: distribuciones y deteccion de outliers
  - Analisis bivariado: correlaciones Spearman, boxplots por genero
  - Tendencias temporales de produccion y popularidad

Feature Engineering:
  - Score de popularidad ponderado (formula IMDb-like)
  - Texto combinado para TF-IDF:
    overview + generos x3 + tagline + titulo + director + top 3 actores

Modelado:
  Modelo                    Descripcion
  ------------------------  -----------------------------------------------
  Popularidad ponderada     Baseline — formula IMDb-like
  Content-based             TF-IDF + similitud coseno
  Hibrido content           Similitud coseno x score ponderado
  Collaborative (BPR)       implicit BPR — factors=100, iterations=30

  Feedback implicito en BPR: rating >= 3.5 → confianza 1.0

Despliegue:
  - Aplicacion interactiva en Streamlit con 4 modos de recomendacion
  - Deploy publico en Streamlit Cloud (disponible en vivo)


RESULTADOS
----------
- Dataset final filtrado:      ~29.8k peliculas (post-limpieza y filtros)
- Subconjunto content-based:   ~9.1k peliculas con >= 50 votos
- Cobertura cruce ratings:     ~63% (suficiente para collaborative filtering)

Validacion colaborativa — ejemplo userId=1:
  Recomendaciones recibidas: Pulp Fiction, Shawshank Redemption, Forrest Gump,
  Star Wars, Back to the Future.
  Alta coherencia con historial del usuario (clasicos 80s-90s, aventura/sci-fi,
  crimen/thriller) — validacion cualitativa positiva.

Mejora observada al enriquecer content-based con director y actores:
  Reduccion de ruido en recomendaciones respecto a TF-IDF solo sobre overview.


HABILIDADES DEMOSTRADAS
-----------------------
- Procesamiento y limpieza de datasets reales complejos (JSON, nulos, duplicados)
- EDA completo y accionable
- Implementacion de recomendadores hibridos (content + collaborative)
- Uso de algoritmos de ranking implicito (BPR) en feedback no explicito
- Despliegue de soluciones interactivas con Streamlit


PROXIMOS PASOS
--------------
- Incorporar keywords.csv para enriquecer content-based
- Agregar evaluacion offline formal (NDCG@10, Precision@K)
- Fine-tuning de hiperparametros en BPR
- Visualizacion de posters en la app Streamlit


TECNOLOGIAS UTILIZADAS
----------------------
Python 3.13 · pandas · numpy · scikit-learn · implicit (BPR) ·
matplotlib · seaborn · Streamlit · Jupyter Notebook
