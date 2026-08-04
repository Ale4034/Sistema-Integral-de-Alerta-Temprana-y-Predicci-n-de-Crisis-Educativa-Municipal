# 🎓 Educational Crisis AI

**Sistema Inteligente de Alerta Temprana para la Predicción de la Deserción Escolar en Colombia mediante Machine Learning**

---

# 📖 Descripción

La deserción escolar continúa siendo uno de los principales retos del sistema educativo colombiano. Este proyecto propone una solución basada en Inteligencia Artificial y Machine Learning que permite estimar la tasa de deserción escolar de los municipios colombianos, clasificar su nivel de riesgo y simular diferentes escenarios de intervención para apoyar la toma de decisiones.

El sistema integra información proveniente del Ministerio de Educación Nacional (MEN), indicadores del Programa de Alimentación Escolar (PAE) y datos de las Entidades Territoriales Certificadas (ETC), construyendo un modelo predictivo capaz de apoyar la priorización de estrategias orientadas a reducir el abandono escolar.

---

# 🎯 Objetivos

- Predecir la tasa de deserción escolar de los municipios colombianos.
- Clasificar los municipios en niveles de riesgo a partir de la deserción estimada.
- Agrupar municipios con características educativas similares mediante clusterización.
- Simular escenarios de intervención modificando indicadores educativos.
- Desarrollar una demo interactiva para apoyar la toma de decisiones.

---

# 🔄 Flujo del sistema

```text
Datos del Ministerio de Educación
                │
                ▼
Integración y preparación de datos
                │
                ▼
Ingeniería de variables
                │
                ▼
Clusterización (K-Means)
                │
                ▼
Predicción de la tasa de deserción (Random Forest)
                │
                ▼
Sistema de Alertas Tempranas
                │
                ▼
Simulación de escenarios
                │
                ▼
Demo interactiva
```

---

# 🧠 Modelos utilizados

Durante el desarrollo del proyecto se implementaron tres técnicas de Machine Learning.

| Modelo | Propósito |
|---------|-----------|
| 🌳 **Random Forest Regressor** | Predicción de la tasa de deserción escolar. |
| 🧠 **MLPRegressor** | Modelo de comparación para evaluar el desempeño del Random Forest. |
| 📊 **K-Means** | Agrupación de municipios con características educativas similares. |

Después de comparar los modelos predictivos, **Random Forest** fue seleccionado como modelo principal debido a que obtuvo un mayor coeficiente de determinación (**R²**) y un menor error cuadrático medio (**RMSE**), logrando el mejor equilibrio entre precisión, robustez e interpretabilidad.

---

# 📊 Resultados principales

El proyecto permitió desarrollar un Sistema Inteligente de Alerta Temprana capaz de:

- Estimar la tasa de deserción escolar para cada registro municipio-año del conjunto de datos.
- Clasificar automáticamente el riesgo en tres niveles (Bajo, Medio y Alto) a partir de la deserción estimada.
- Agrupar los municipios en cuatro clusters con características educativas similares.
- Simular el impacto de diferentes estrategias de intervención modificando indicadores educativos.
- Implementar una demo interactiva para explorar escenarios y apoyar la toma de decisiones.

---

# 📂 Documentación

La documentación completa del proyecto se encuentra disponible en Google Drive e incluye la explicación detallada de cada notebook, la metodología desarrollada y los principales resultados obtenidos.

## 📄 Documentación del proyecto

https://drive.google.com/drive/folders/13JqImwUKCeRk3Toc-lwoZToWGwIisvxA?usp=sharing

La carpeta incluye:

- Documentación de los 13 notebooks.
- Sistema de Alertas Tempranas.
- Simulación de escenarios.
- Listado de municipios clasificados por nivel de riesgo.
- Listado de municipios agrupados por clusters.

---

# 🚨 Sistema de Alertas Tempranas

A partir de la tasa de deserción estimada por el modelo Random Forest, se desarrolló un sistema que clasifica automáticamente cada registro municipio-año en un nivel de riesgo:

- 🟢 Bajo
- 🟡 Medio
- 🔴 Alto

Esta clasificación permite identificar de manera rápida los municipios que requieren una mayor atención y facilita la priorización de intervenciones por parte de las autoridades educativas.

---

# 🗺️ Clusterización de municipios

Además de la predicción, el proyecto implementa un modelo de clusterización mediante K-Means.

Los municipios fueron agrupados en cuatro clusters con características educativas similares. Es importante destacar que estos grupos **no representan municipios mejores o peores**, sino perfiles educativos semejantes que permiten diseñar estrategias diferenciadas según las necesidades de cada territorio.

El listado completo de municipios pertenecientes a cada cluster se encuentra disponible dentro de la documentación del proyecto.

---

# 💻 Demo interactiva

Como etapa final del proyecto se desarrolló una demo interactiva que permite:

- Seleccionar un municipio.
- Consultar sus principales indicadores educativos.
- Estimar su tasa de deserción mediante el modelo Random Forest.
- Modificar variables como cobertura, aprobación, reprobación y repitencia.
- Comparar el escenario original con un escenario intervenido para analizar el posible impacto de diferentes estrategias educativas.

Esta herramienta demuestra el potencial del sistema como apoyo para la toma de decisiones basada en datos.

---

# 🛠️ Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Jupyter Notebook
- ipywidgets
- Joblib

---

# 📁 Estructura del proyecto

```text
educational_crisis_ai/

├── app/
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│   ├── 01_Carga_Datos.ipynb
│   ├── ...
│   └── 13_Demo_Interactiva.ipynb
│
├── outputs/
│
├── src/
│
├── README.md
└── requirements.txt
```

---

# 👥 Autores

Proyecto desarrollado como trabajo académico para la asignatura de Inteligencia Artificial.

- Juan David Sanclemente Salazar
- Alejandra Arciniegas Marin
- Luz Dary Marin Henao
- Pedro Arciniegas Diaz

---

# ⭐ Conclusión

Este proyecto demuestra cómo las técnicas de Machine Learning pueden convertirse en herramientas de apoyo para la toma de decisiones en el ámbito educativo. Más allá de estimar la deserción escolar, el sistema integra predicción, clasificación del riesgo, segmentación territorial mediante clusterización y simulación de escenarios, proporcionando una solución integral que facilita la priorización de intervenciones y la planificación de estrategias orientadas a reducir el abandono escolar en Colombia.