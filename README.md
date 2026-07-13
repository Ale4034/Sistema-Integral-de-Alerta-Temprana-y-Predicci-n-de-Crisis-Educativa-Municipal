# 🎓 EduPredict Colombia
### Sistema Inteligente para la Predicción de la Deserción Escolar y el Apoyo a la Toma de Decisiones Educativas

Proyecto desarrollado para el concurso **Datos al Ecosistema 2026 – IA para Colombia**, organizado por el **Ministerio de Tecnologías de la Información y las Comunicaciones (MinTIC)**.

---

## 📌 Descripción

EduPredict Colombia es un sistema de analítica predictiva basado en Inteligencia Artificial que integra información pública del Ministerio de Educación Nacional para identificar municipios con mayor riesgo de deserción escolar.

El proyecto combina técnicas de Ciencia de Datos, Aprendizaje Automático y Análisis Exploratorio para apoyar la toma de decisiones mediante predicciones, alertas tempranas, segmentación de municipios y simulación de escenarios de intervención.

---

## 🎯 Objetivos

- Integrar múltiples fuentes oficiales de información educativa.
- Analizar el comportamiento de los principales indicadores educativos en Colombia.
- Desarrollar modelos predictivos para estimar la tasa de deserción escolar municipal.
- Implementar un sistema de alertas tempranas para identificar municipios en riesgo.
- Agrupar municipios con características similares mediante técnicas de clustering.
- Simular escenarios de intervención para evaluar el posible impacto de políticas educativas.

---

## 📊 Datos utilizados

El proyecto integra información oficial correspondiente al periodo **2011–2024**, incluyendo:

- Base Principal del Ministerio de Educación Nacional.
- Indicadores de las Entidades Territoriales Certificadas (ETC).
- Programa de Alimentación Escolar (PAE).

El conjunto de datos final contiene aproximadamente:

- **15 707 registros**
- **85 variables**
- **1 122 municipios**

---

## 🤖 Modelos implementados

Durante el proyecto se desarrollaron y evaluaron diferentes modelos de aprendizaje automático, entre ellos:

- 🌲 Random Forest Regressor
- 🧠 Red Neuronal Multicapa (MLPRegressor)

El modelo principal alcanzó un desempeño de:

| Métrica | Resultado |
|---------|-----------:|
| MAE | **0.126** |
| RMSE | **0.372** |
| R² | **0.970** |

---

## 🚨 Funcionalidades desarrolladas

- ✅ Integración y limpieza de datos.
- ✅ Ingeniería de variables.
- ✅ Análisis Exploratorio de Datos (EDA).
- ✅ Predicción de la deserción escolar.
- ✅ Sistema de alertas tempranas.
- ✅ Clustering de municipios.
- ✅ Simulación de escenarios de intervención.

---

## 🛠 Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- TensorFlow
- Matplotlib
- Plotly
- Streamlit
- Folium
- SHAP
- Joblib

---

## 📂 Estructura del proyecto

```
educational_crisis_ai/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│
├── src/
│
├── models/
│
├── outputs/
│
├── app/
│
├── requirements.txt
└── README.md
```

---

## 🚀 Principales resultados

- Integración de tres bases oficiales del Ministerio de Educación Nacional.
- Construcción de un dataset consolidado con 85 variables.
- Desarrollo de variables derivadas para enriquecer el análisis.
- Modelo predictivo con un coeficiente de determinación (R²) de 0.97.
- Identificación de municipios con mayor riesgo mediante alertas tempranas.
- Agrupación automática de municipios según su perfil educativo.
- Simulación del impacto potencial de intervenciones educativas.

---

## 📄 Licencia

Este proyecto fue desarrollado con fines académicos y de investigación en el marco del concurso **Datos al Ecosistema 2026 – IA para Colombia**.

---

## Descarga del Modelo Entrenado
Debido a las restricciones de tamaño de archivo de GitHub (>100 MB), el modelo entrenado no se encuentra directamente en este repositorio. Puedes descargarlo desde el siguiente enlace:

* [Descargar random_forest_desercion.pkl]([PEGA_AQUÍ_TU_ENLACE_DE_GOOGLE_DRIVE](https://drive.google.com/drive/folders/1qsXUIMlK3A-4rwB3y3FNqNXe01McqSxU?usp=drive_link))

Debes guardar este archivo dentro de la carpeta `models/` en tu entorno local para que el sistema funcione correctamente.
