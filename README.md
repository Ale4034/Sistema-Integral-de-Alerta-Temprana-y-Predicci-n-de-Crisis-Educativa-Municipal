# 🎓 Educational Crisis AI

Sistema de Alertas Tempranas para la Predicción de la Deserción Escolar en Colombia mediante Machine Learning.

---

## 📖 Descripción

La deserción escolar continúa siendo uno de los principales retos del sistema educativo colombiano. Este proyecto propone una solución basada en **Inteligencia Artificial** y **Machine Learning** que permite estimar la tasa de deserción escolar de los municipios colombianos, identificar territorios con mayor riesgo y simular posibles estrategias de intervención.

El sistema integra información proveniente del Ministerio de Educación Nacional, indicadores del Programa de Alimentación Escolar (PAE) y datos de las Entidades Territoriales Certificadas (ETC), construyendo un modelo predictivo capaz de apoyar la toma de decisiones.

---

## 🎯 Objetivos

- Predecir la tasa de deserción escolar municipal.
- Identificar municipios con mayor riesgo de deserción.
- Agrupar municipios con características similares mediante clusterización.
- Simular escenarios de intervención modificando indicadores educativos.
- Desarrollar una demo interactiva para apoyar la toma de decisiones.

---

## 🧠 Modelos utilizados

Durante el desarrollo del proyecto se implementaron tres técnicas de Machine Learning:

| Modelo | Propósito |
|---------|-----------|
| 🌳 Random Forest Regressor | Predicción de la tasa de deserción escolar. |
| 🧠 MLPRegressor | Modelo de comparación para evaluar el desempeño del Random Forest. |
| 📊 K-Means | Agrupación de municipios con características educativas similares. |

Después de comparar los modelos predictivos, **Random Forest** fue seleccionado como modelo principal debido a que obtuvo un mayor coeficiente de determinación (R²) y un menor error cuadrático medio (RMSE).

---

## 📊 Resultados principales

El proyecto permitió desarrollar un Sistema de Alertas Tempranas capaz de:

- Estimar la tasa de deserción escolar para cada municipio.
- Clasificar el riesgo en tres niveles (Bajo, Medio y Alto).
- Agrupar municipios en cuatro clusters según sus características educativas.
- Simular el efecto de posibles intervenciones sobre la deserción estimada.
- Implementar una demo interactiva para explorar diferentes escenarios.

---

## 📂 Documentación

La documentación completa del proyecto se encuentra disponible en Google Drive e incluye la explicación detallada de cada notebook, el flujo metodológico y los principales resultados obtenidos.

📄 **Documentación del proyecto**

https://drive.google.com/drive/folders/13JqImwUKCeRk3Toc-lwoZToWGwIisvxA?usp=sharing

La carpeta incluye:

- Documentación de los 13 notebooks.
- Sistema de Alertas Tempranas.
- Simulación de escenarios.
- Listado de municipios clasificados por nivel de riesgo.
- Listado de municipios agrupados por clusters.

---

## 🚨 Municipios con mayor riesgo

Como resultado del modelo predictivo se generó un listado de municipios clasificados según su nivel de riesgo de deserción escolar.

Este listado puede servir como herramienta de apoyo para priorizar intervenciones educativas, permitiendo identificar aquellos municipios que requieren mayor atención de acuerdo con la predicción realizada por el modelo.

El archivo se encuentra disponible dentro de la carpeta de documentación.

---

## 🗺️ Clusterización de municipios

Además de la predicción, el proyecto implementa un modelo de clusterización mediante K-Means.

Los municipios fueron agrupados en cuatro clusters con características educativas similares. Es importante destacar que estos grupos **no representan una clasificación de municipios mejores o peores**, sino una segmentación que facilita el diseño de estrategias diferenciadas según el contexto de cada territorio.

El listado completo de municipios por cluster también se encuentra disponible dentro de la documentación.

---

## 🛠️ Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Jupyter Notebook
- ipywidgets

---

## 📁 Estructura del proyecto

```text
educational_crisis_ai/

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
├── src/
│
├── README.md
```

---

## 👥 Autores

Proyecto desarrollado como trabajo académico para la asignatura de Inteligencia Artificial.

- Juan David ...
- Alejandra ...

---

## ⭐ Conclusión

Este proyecto demuestra cómo las técnicas de Machine Learning pueden convertirse en herramientas de apoyo para la toma de decisiones en el ámbito educativo. Más allá de predecir la deserción escolar, el sistema integra predicción, clasificación del riesgo, segmentación territorial y simulación de escenarios, proporcionando una visión integral que puede contribuir a la planificación de estrategias orientadas a reducir el abandono escolar en Colombia.
