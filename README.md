# Sistema Inteligente de Alerta Temprana para la Deserción Escolar en Colombia

## Descripción

Este proyecto desarrolla un sistema inteligente de alerta temprana para estimar la tasa de deserción escolar en los municipios de Colombia mediante técnicas de aprendizaje automático y análisis de datos.

A partir de información del Ministerio de Educación Nacional y del Programa de Alimentación Escolar (PAE), se construyó un modelo predictivo basado en Random Forest capaz de estimar la deserción escolar y evaluar el impacto de diferentes escenarios de intervención sobre variables educativas clave.

Además del modelo predictivo, el proyecto incorpora un proceso de clusterización de municipios para identificar perfiles educativos similares y facilitar el diseño de estrategias diferenciadas según las características de cada territorio.

---

## Objetivos

- Integrar múltiples fuentes oficiales de información educativa.
- Analizar los principales factores asociados a la deserción escolar.
- Entrenar un modelo de Machine Learning para estimar la tasa de deserción.
- Identificar grupos de municipios con características similares mediante K-Means.
- Implementar una demo interactiva para simular intervenciones educativas.

---

## Estructura del proyecto

```text
educational_crisis_ai/

├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── docs/
│
├── requirements.txt
└── README.md
```

---

## Flujo de trabajo

| Notebook | Descripción |
|----------|-------------|
| Notebook 01 | Carga e inspección del dataset PAE |
| Notebook 02 | Carga e inspección del dataset principal |
| Notebook 03 | Carga e inspección del dataset ETC |
| Notebook 04 | Integración de los tres conjuntos de datos |
| Notebook 05 | Ingeniería de variables |
| Notebook 06 | Análisis exploratorio de datos |
| Notebook 07 | Entrenamiento del modelo Random Forest |
| Notebook 08 | Evaluación del modelo |
| Notebook 09 | Comparación con MLPRegressor |
| Notebook 10 | Clusterización de municipios |
| Notebook 11 | Análisis de resultados |
| Notebook 12 | Simulación de escenarios |
| Notebook 13 | Demo interactiva del sistema |

---

## Tecnologías utilizadas

- Python 3
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Plotly
- Jupyter Notebook
- ipywidgets

---

## Modelos implementados

### Random Forest Regressor

Modelo principal utilizado para estimar la tasa de deserción escolar municipal.

### MLPRegressor

Modelo desarrollado para comparar el desempeño predictivo con el Random Forest.

### K-Means

Modelo de aprendizaje no supervisado utilizado para identificar grupos de municipios con características educativas similares.

---

## Resultados principales

- Construcción de un modelo predictivo para estimar la tasa de deserción escolar.
- Identificación de cuatro perfiles de municipios mediante clusterización.
- Desarrollo de una demo interactiva para evaluar escenarios de intervención educativa.

---

## Documentación

La documentación técnica detallada de cada notebook se encuentra disponible en la carpeta **docs/** del proyecto.

---

## Autores

- Juan David Sanclemente Salazar
- Alejandra ...
- Luz ...