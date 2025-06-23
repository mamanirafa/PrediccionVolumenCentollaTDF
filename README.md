<!-- Portada -->
<p align="center">
  <p align="center">
    <img src="img/portadaA4.png"         alt="Portada A4"            width="1200"/>
  </p>
</p>

<!-- Badges -->
<p align="center">
  <a href="https://github.com/mamanirafa/Testing/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/mamanirafa/Testing/ci.yml" alt="Build Status"/>
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/mamanirafa/Testing" alt="License"/>
  </a>
</p>

---
---

**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial  
**Institución:** Politécnico Malvinas Argentinas  
**Materia:** Aprendizaje Automático

**Proyecto:** Predicción del volumen sostenible de captura de Centolla en Tierra del Fuego

- **Alumno:** MAMANI, Rafael
- **Profesor:** Martín Mirabete

---
##  Indice
### Accesos rápidos:
- [Resumen](#resumen)
- [Objetivo General](#objetivo-general)
- [Objetivos Específicos](#objetivos-específicos)
- [Contexto y Relevancia](#contexto-y-relevancia)
- [Origen y Descripción de los Datos](#origen-y-descripción-de-los-datos)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Licencia](#licencia)
---
Predicción de Producción Sostenible de Trucha en TDF mediante Modelos de Aprendizaje Automático
==============================
# Descripción del Proyecto
##  Resumen

Este proyecto de aprendizaje automático busca predecir el volumen sostenible de capturas de centolla (Lithodes
santolla) por año en Tierra del Fuego, utilizando un modelo de regresión implementado en Python con scikitlearn. El dataset principal, “Pesca y Puertos Pesqueros” del Ministerio de Economía, contiene datos históricos
que permiten identificar patrones para la predicción. El proyecto utiliza la plantilla Cookiecutter Data Science y
un repositorio Git para garantizar reproducibilidad, con resultados documentados. El
modelo no realiza un análisis estadístico, sino que aprende patrones de los datos para generar predicciones
útiles para simulaciones y toma de decisiones en la gestión pesquera.

---

##  Objetivo General
Desarrollar un modelo de regresión que prediga el volumen sostenible de capturas de centolla (en toneladas)
por año en Tierra del Fuego, basado en variables como esfuerzo pesquero, condiciones ambientales y
regulaciones, para apoyar la gestión pesquera sostenible.

![Ejemplo de uso](img/objetivofin.png)

---

##  Objetivos Específicos
1. Preprocesar el dataset para filtrar datos de Tierra del Fuego y centolla, asegurando patrones claros para
el aprendizaje del modelo.
2. Implementar un modelo de regresión (Random Forest Regressor o Linear Regression) para predecir el
volumen sostenible.
3. Modelo con métricas como MSE, MAE y R², validando su capacidad para aprender patrones predictivos.
4. Generar simulaciones de volúmenes sostenibles para recomendar cuotas de pesca optimizadas.

---

##  Contexto y Relevancia
Tierra del Fuego,depende de la pesca de centolla como pilar económico en puertos como Ushuaia y Río Grande.
La sobreexplotación y el cambio climático amenazan este recurso, mientras que el aislamiento geográfico
complica la logística. La certificación MSC de la pesquería de centolla resalta la importancia de la sostenibilidad
por lo que predecir volúmenes sostenibles es relevante para: (1) proteger la biodiversidad marina, (2) sostener
la economía local, (3) informar cuotas de pesca, y (4) adaptarse a cambios ambientales. La originalidad radica
en aplicar regresión a datos específicos de centolla en una región remota, generando simulaciones prácticas.

---

##  Origen y Descripción de los datos

### Origen del Dataset

*   **Instituto Nacional de Estadísticas (INE) Chile**, Global Fishing Watch, y fuentes oficiales de regulación pesquera.
*   **Fecha de Adquisición:** Junio de 2025.
*   **Recopilación:** Datos recolectados y consolidados a partir de informes oficiales de desembarques, registros satelitales de esfuerzo pesquero, datos oceanográficos y normativas vigentes.
*   **Política de Datos:** Información pública y gratuita, sujeta a procesos de validación y depuración para garantizar calidad y consistencia.

### Descripción del Dataset

*   **Cantidad de Instancias:** Datos mensuales correspondientes a capturas, esfuerzo pesquero, temperatura superficial y regulación de veda.
*   **Período Cubierto:** Desde enero de 2019 hasta diciembre de 2024, totalizando 72 meses.
*   **Frecuencia:** Datos agrupados a nivel mensual por puerto (principalmente Punta Arenas).
*   **Total de Registros:** Aproximadamente 784 instancias, integrando múltiples variables para análisis y modelado.

### Características (Columnas) y Tipos de Datos

*   **Año:** Año de registro (tipo: entero).
*   **Mes:** Mes de registro (tipo: entero o texto abreviado).
*   **Especie:** Nombre común o científico de la especie (tipo: texto).
*   **Volumen de Captura (toneladas):** Cantidad de centolla desembarcada (tipo: float).
*   **Esfuerzo Pesquero (horas):** Horas de pesca reportadas en la zona (tipo: float).
*   **Número de Embarcaciones:** Cantidad de embarcaciones activas en la pesca (tipo: entero).
*   **Tipo de Arte:** Método o equipo de pesca utilizado (tipo: texto).
*   **Temperatura Superficial del Mar (°C):** Temperatura promedio mensual registrada en la zona de pesca (tipo: float).
*   **Estado de Veda:** Indicador binario o categórico que señala si hay veda vigente en el mes (tipo: booleano o texto).
*   **Variables adicionales:** Variables calculadas o derivadas para el análisis (tipo: varios).

### Información Relevante Adicional

*   **Datos Preliminares:** Los datos se encuentran sujetos a posibles actualizaciones y correcciones posteriores a procesos de limpieza y validación.
*   **Valores Faltantes:** Existen registros con datos ausentes o nulos en algunas variables, particularmente en el esfuerzo pesquero y temperatura, que fueron tratados durante la limpieza.
*   **Consistencia:** Se aplicaron procesos de depuración para homogeneizar nombres de especies, formatos de fecha y codificación de variables categóricas.

---
---

## Análisis exploratorio de datos

Se realizaron análisis gráficos y estadísticos, incluyendo:

- Captura total anual y promedio mensual de centolla.  
- Relación entre esfuerzo pesquero, temperatura y volumen capturado.  
- Impacto de la veda en los volúmenes de pesca.

![graficos](img/graficofin.png)

---

## Conclusiones del análisis exploratorio
🔬 ANÁLISIS EXPLORATORIO DE DATOS | CONCLUSIONES EJECUTIVAS
🔬 Análisis Predictivo de Volumen de Captura | Lithodes santolla | Tierra del Fuego
bash═══════════════════════════════════════════════════════════════
 DATASET: Registro de Capturas Pesqueras  
 PERÍODO: 2020-2024 | REGIÓN: Punta Arenas
 ESTADO: ████████████████████████████ 100% COMPLETADO
═══════════════════════════════════════════════════════════════

🎯 MÓDULO 01 → ANÁLISIS TEMPORAL: CAPTURA ANUAL
📊 PATRÓN DETECTADO: Discontinuidad temporal significativa
python# Años de máxima actividad pesquera
años_pico = [2020, 2021]     # Volúmenes superiores al promedio base
brecha_datos = [2022, 2023]  # Ausencia de datos críticos  
estado_actual = 2024         # Captura marginal detectada

⚠️ VARIABLES EXPLICATIVAS IDENTIFICADAS
diff+ Modificaciones en marco regulatorio pesquero
+ Extensión de períodos de veda biológica
+ Fluctuaciones naturales en biomasa poblacional
! Inconsistencias en sistema de registro de datos
- Factores socio-económicos externos (COVID-19)


🎯 MÓDULO 02 → ANÁLISIS ESTACIONAL: DISTRIBUCIÓN MENSUAL
📈 PATRÓN DETECTADO: Estacionalidad pronunciada
sql-- Consulta de distribución estacional
SELECT mes, PROMEDIO(volumen_captura) 
FROM datos_pesca 
WHERE mes IN ('Octubre', 'Noviembre', 'Diciembre')
ORDER BY volumen_captura DESC;

-- RESULTADO: Noviembre > Diciembre > Octubre
🔥 INSIGHT CLAVE: Concentración en Q4
MESVOLUMEN RELATIVOSIGNIFICANCIANoviembre████████████████████ 100%PICO ABSOLUTODiciembre████████████████░░░░ 85%ALTAOctubre██████████████░░░░░░ 70%MODERADA
CORRELACIÓN IDENTIFICADA: Sincronización perfecta con ventanas regulatorias post-veda

🎯 MÓDULO 03 → ANÁLISIS DE CORRELACIÓN: ESFUERZO vs RENDIMIENTO
⚡ MODELO: Análisis de Relación Esfuerzo-Rendimiento
r# Análisis de correlación avanzado
coeficiente_correlacion <- cor(horas_pesca, volumen_captura)
modelo_regresion <- lm(volumen ~ esfuerzo + factores_ambientales)

# R² moderado con alta dispersión residual detectada
📐 HALLAZGOS ESTADÍSTICOS
yamlCORRELACIÓN_POSITIVA: 
  tendencia: "esfuerzo_mayor → captura_mayor"
  intensidad: "moderada"
  
ALTA_VARIANZA:
  dispersión: "significativa"
  outliers: "detectados"
  
CASOS_ATÍPICOS:
  - alto_esfuerzo_baja_captura: "identificados"
  - bajo_esfuerzo_alta_captura: "documentados"
🔍 FACTORES DE VARIABILIDAD IDENTIFICADOS
mermaidgraph TD
    A[Esfuerzo Pesquero] --> B{Volumen Capturado}
    C[Abundancia Espacial] --> B
    D[Condiciones Oceanográficas] --> B
    E[Eficiencia de Flota] --> B
    F[Factores Estocásticos] --> B

🎯 MÓDULO 04 → ANÁLISIS MULTIVARIADO: TEMPERATURA vs CAPTURA
🌡️ RESULTADO: Relación estadísticamente no significativa
python# Test de significancia estadística
import scipy.stats as stats

p_valor = stats.pearsonr(temperatura_superficial, volumen_captura)[1]
resultado = "No significativa" if p_valor > 0.05 else "Significativa"

# OUTPUT: p > 0.05 → No rechazar H₀ (independencia)
🧮 INTERPRETACIONES ALGORÍTMICAS
TIPODESCRIPCIÓNPROBABILIDADDIRECTATemperatura como predictor primarioBAJAINDIRECTAEfectos mediados por variables latentesALTATEMPORALEfectos con lag temporal no capturadosMEDIA

⚡ SÍNTESIS EJECUTIVA: HALLAZGOS CLAVE
🎯 RANKING DE IMPORTANCIA DE VARIABLES
VARIABLEPODER PREDICTIVOSIGNIFICANCIAIMPACTOPRIORIDADEstacionalidad Temporal████████████ ALTOp < 0.001🔴 CRÍTICO#1Variabilidad Interanual██████████░░ ALTOp < 0.01🟠 ALTO#2Esfuerzo Pesquero██████░░░░░░ MEDIOp < 0.05🟡 MEDIO#3Temperatura Superficial███░░░░░░░░░ BAJOp > 0.05🟢 BAJO#4
🚀 RECOMENDACIONES ALGORÍTMICAS
pythondef siguiente_pipeline_analisis():
    modelos_recomendados = [
        'regresion_multivariada()',
        'series_temporales_predictivas()', 
        'evaluacion_impacto_politicas()',
        'modelado_sostenibilidad()'
    ]
    return execute_pipeline(modelos_recomendados)

🎯 CONCLUSIÓN FINAL
diff+ PATRÓN ESTACIONAL: Robustez estadística confirmada en Q4
+ VARIABILIDAD INTERANUAL: Alta significancia como driver principal  
+ FACTORES REGULATORIOS: Emergen como variables de control críticas
- VARIABLES AMBIENTALES: Requieren análisis más profundo para causalidad
! GAPS DE DATOS: Críticos para robustez del modelo (2022-2023)
STATUS: ANÁLISIS COMPLETADO ████████████████████ 100%

Estos resultados sugieren que la captura de centolla en Punta Arenas tiene una marcada estacionalidad y una fuerte variabilidad interanual. El esfuerzo pesquero tiene cierta relación con el volumen capturado, pero otros factores (regulaciones, clima, dinámica poblacional) probablemente también juegan un papel relevante.
Será útil profundizar en análisis de regresión o modelos predictivos para comprender mejor las relaciones entre las variables y evaluar el impacto de la veda y las regulaciones sobre la sostenibilidad de la pesquería.

---

## Modelo de Aprendizaje Automático

- Algoritmos utilizados: Regresión Lineal y Random Forest Regressor.  
- Variables predictoras: Esfuerzo pesquero, temperatura, indicadores de veda, y datos temporales.  
- Se aplicaron técnicas de limpieza, normalización y validación cruzada para garantizar robustez.

---

## Evaluación del modelo

| Métrica               | Regresión Lineal | Random Forest |
|-----------------------|------------------|---------------|
| MAE (Error absoluto)   | 7.90             | 0.14          |
| MSE (Error cuadrático) | 102.44           | 0.18          |
| R² (Determinación)     | 0.11             | 1.00          |

*(Incluir gráficos de predicción vs real para ambos modelos)*

---

## Interpretación y conclusiones finales

- El modelo Random Forest mostró un desempeño superior, capturando con precisión la variabilidad en los datos.  
- El modelo puede servir como herramienta predictiva para apoyar la toma de decisiones en la gestión pesquera.  
- Limitaciones incluyen la cantidad y calidad de datos, así como posibles variables no consideradas.

---

## Recomendaciones

- Ampliar el dataset con más variables ambientales y biológicas.  
- Probar otros modelos y técnicas avanzadas de machine learning.  
- Implementar monitoreo continuo para actualizar el modelo periódicamente.

---

## Entregables en el repositorio

- Notebooks: Exploración, análisis, modelado y depuración.  
- Dataset procesado (`dataset_modelado_final.csv`).  
- Gráficos y reportes generados.  
- Documentos descriptivos y presentación ejecutiva.

---

---
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