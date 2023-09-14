**PROYECTO AIRLINES EQUIPO 2**

El presente proyecto busca proporcionar un modelo de inteligencia artificial para predecir si los clientes de una aerolínea están satisfechos o no según los datos proporcionados.

**ESTRUCTURA DE ARCHIVOS**

El proyecto contiene las siguientes carpetas:

**app:** contiene la aplicación de Streamlit donde se ingresan los datos que proporcionaría el cliente y se muestra la predicción del modelo IA(satisfecho o insatisfecho).

**config:** en esta carpeta se encuentra la configuración/conexión a la base de datos y la creación de la tabla donde se guardará la información de los clientes.

**experimental_pipelines:** en esta carpeta se encuentra el código que permite hacer "experimentos" para probar diferentes transformaciones que se puede hacer a los datos antes de entrenar el modelo.

**functions_methods:** contiene las transformaciones personalizadas (custom_transformers) que se puede hacer a la data y distintas funciones para cargarlos y manipularlos.

**models_metrics:** en esta carpeta se realiza el testeo de distintos modelos de IA y se evalúan las métricas con validación cruzada. También se realiza el ajuste de hiperparámetros del modelo seleccionado.

**archivo main:** este archivo contiene el paso a paso de las funciones alojadas en los demás archivos para realizar el proceso entero de obtención de un modelo de ML.

Al crear el pipeline de transformaciones de la data y al entrenar el modelo de IA se crean automáticamente los archivos .pkl que se cargan para tener la app funcional.


INTEGRANTES EQUIPO 2**
- Ana Gomez
- Carolina Gomez
- Maikol Garrido
- Tania Monteiro

**![Captura de pantalla (116)](https://github.com/AI-School-F5-P2/proyecto_airlines_equipo_2/assets/104582495/57d1d28d-f817-493c-be71-ef5d26ac03a6)
