from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Este proyecto de aprendizaje automático busca predecir el volumen sostenible de capturas de centolla (Lithodes santolla) por año en Tierra del Fuego, utilizando un modelo de regresión implementado en Python con scikit-learn. El dataset principal, “Pesca y Puertos Pesqueros” del Ministerio de Economía, contiene datos históricos que permiten identificar patrones para la predicción. El modelo no realiza un análisis estadístico, sino que aprende patrones de los datos para generar predicciones útiles para simulaciones y toma de decisiones en la gestión pesquera.',
    author='RafaelMamani',
    license='MIT',
)
