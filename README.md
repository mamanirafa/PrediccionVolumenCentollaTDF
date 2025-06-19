Predicion del volumen sostenible de captura de centolla en TDF
==============================

Este proyecto de aprendizaje automático busca predecir el volumen sostenible de capturas de centolla (Lithodes santolla) por año en Tierra del Fuego, utilizando un modelo de regresión implementado en Python con scikit-learn. El dataset principal, “Pesca y Puertos Pesqueros” del Ministerio de Economía, contiene datos históricos que permiten identificar patrones para la predicción. El modelo no realiza un análisis estadístico, sino que aprende patrones de los datos para generar predicciones útiles para simulaciones y toma de decisiones en la gestión pesquera.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

2. Origen y descripción de los datos
Se integraron múltiples fuentes de datos principalmente del puerto de punta arenas, abarcando el periodo 2019–2024:
•	Datos de desembarque:
o	Captura mensual por especie y puerto, proporcionados por el Instituto Nacional de Estadísticas de Chile (INE).
•	Esfuerzo pesquero:
o	Horas de pesca y cantidad de embarcaciones, extraídos de reportes sectoriales y Global Fishing Watch.
•	Condiciones ambientales:
o	Temperatura superficial del mar, obtenida de registros oceanográficos oficiales.
•	Regulación:
o	Períodos de veda biológica, construidos a partir de normativas del Ministerio de Economía y documentación de Seafood Watch y MSC.
________________________________________
3. Análisis exploratorio de datos
Se realizó una limpieza y estandarización de todos los datasets, integrándolos en un único archivo (dataset_modelado_final.csv).
El análisis exploratorio permitió observar:
•	Variabilidad interanual y estacional:
o	Picos de captura en los meses de noviembre y diciembre.
o	Años con mayores volúmenes (2020, 2021) y años con caídas o sin datos (2022, 2023).
•	Relaciones entre variables:
o	Relación positiva entre esfuerzo (horas de pesca) y volumen capturado.
o	Influencia limitada de la temperatura superficial en la variabilidad de las capturas.
o	La veda restringe el esfuerzo y la captura, aunque se detectaron registros residuales durante meses de veda.
Principales gráficos generados:
•	Captura total anual y mensual
•	Esfuerzo pesquero vs. volumen capturado
•	Captura vs. temperatura superficial
•	Captura en meses con/sin veda (boxplot)
________________________________________
4. Conclusiones del análisis exploratorio
•	La captura de centolla presenta marcada estacionalidad, con mayor actividad al finalizar la veda.
•	La relación entre esfuerzo y volumen es positiva pero con alta dispersión, reflejando la influencia de factores biológicos y regulatorios.
•	No se observaron patrones claros asociados a la temperatura superficial del mar.
•	La veda biológica es efectiva, aunque se recomienda seguir monitoreando el cumplimiento.
________________________________________
5. Modelo de Aprendizaje Automático
Arquitectura y algoritmos utilizados
•	Regresión Lineal:
o	Usada como línea base para predecir el volumen mensual de captura.
•	Random Forest Regressor:
o	Algoritmo de ensamble no lineal con 100 árboles (n_estimators=100), random state 42.
o	Variables predictoras: horas de pesca, embarcaciones activas, temperatura superficial, veda.
Ajuste de hiperparámetros
•	Se usaron los valores por defecto de scikit-learn para Random Forest, considerando el tamaño del dataset.
•	No se aplicó ajuste fino de hiperparámetros por limitaciones en la cantidad de datos.
________________________________________
6. Evaluación del modelo
Métricas utilizadas
•	MAE (Error Absoluto Medio):
o	Lineal: ~7.90
o	Random Forest: 0.14
•	MSE (Error Cuadrático Medio):
o	Lineal: 102.44
o	Random Forest: 0.18
•	R² (Coeficiente de determinación):
o	Lineal: 0.11
o	Random Forest: 1.00 (en test), -11.8 (validación cruzada)
•	(Nota: Dado que la tarea es regresión, métricas como precisión, recall o F1 no aplican; se usan métricas estándar para regresión.)
Validación cruzada
•	Random Forest mostró sobreajuste severo: desempeño perfecto en test, pero R² negativo en validación cruzada.
________________________________________
7. Interpretación y conclusiones finales
•	El modelo Random Forest se ajusta perfectamente a los datos de entrenamiento/test, pero no generaliza bien a datos nuevos (sobreajuste confirmado por validación cruzada).
•	La regresión lineal mostró bajo poder explicativo, sugiriendo la necesidad de incorporar más variables o datos.
•	El análisis de importancia de variables indicó que el esfuerzo pesquero y la temperatura son las variables predictoras más relevantes.
Conclusiones clave:
•	El modelado automático tiene potencial, pero requiere datasets más amplios y variados para ser fiable.
•	La validación cruzada es esencial para evitar falsas sensaciones de precisión.
•	Este trabajo sienta una base metodológica para futuros desarrollos en la gestión pesquera con IA.
________________________________________
8. Recomendaciones
•	Ampliar la recolección de datos (más años, zonas y variables).
•	Probar técnicas de regularización o modelos más simples en datasets pequeños.
•	Mantener la validación cruzada como estándar en proyectos de predicción pesquera.
•	Documentar y reportar siempre las limitaciones junto con los logros.
________________________________________
