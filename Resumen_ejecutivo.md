Resumen Ejecutivo –  Sistema de Recomendación Híbrido de Películas, Series y Anime
Contexto
El objetivo fue desarrollar un recomendador híbrido que combine filtrado colaborativo (usuario-ítem), basado en contenido (metadata de películas) y popularidad ponderada, utilizando datos reales de The Movies Dataset (TMDB + MovieLens).
Metodología

ETL: Limpieza de ~45k películas (nulos, tipos, duplicados, parseo JSON). Filtro conservador: solo estrenadas, duración razonable, ≥5 votos.
EDA: Análisis univariado/bivariado (distribuciones, outliers, correlaciones Spearman, tendencias temporales).
Feature engineering: Texto combinado (overview + géneros ×3 + tagline + título + director + top 3 actores) para TF-IDF. Score de popularidad ponderado (fórmula IMDb-like).
Modelado:
Popularidad ponderada (baseline).
Content-based + híbrido (similitud coseno × score).
Collaborative filtering con implicit BPR (Bayesian Personalized Ranking, factors=100, iterations=30).

Despliegue: App interactiva en Streamlit con 4 modos (popularidad, por título, por usuario, híbrido).

Resultados clave

Dataset procesado: ~29.8k películas (post-filtros).
Cobertura cruce ratings: ~63% (suficiente para CF).
Recomendaciones collaborative (BPR) para usuarios reales: alta coherencia (ej: userId=1 recibió Pulp Fiction, Shawshank Redemption, Star Wars, Back to the Future – alineado con su historial de clásicos 80s-90s).
Mejora significativa al enriquecer content-based con director/actores (reducción de ruido en recomendaciones).
App funcional: interfaz limpia, interactiva, reproducible.

Valor y habilidades demostradas
Este proyecto muestra capacidad para:

Procesar y limpiar datasets reales complejos (JSON, nulos, duplicados).
Realizar EDA completo y actionable.
Implementar recomendadores híbridos (content + collaborative).
Usar algoritmos avanzados de ranking (BPR) en feedback implícito.
Desplegar soluciones interactivas (Streamlit).