# proyecto
## Problema
Prediccion de cultivos de cafe para tener un estimado para el momento de la postcosecha
## Diagrama 

## Solucion 
El programa proporciona una herramienta para preveer los rendimientos de las cosechas de cafe basandose en variables historicas 

Esto se hizo recopilando los datos sobre los rendmientos de las cosechas de los años anteriores y las variables relacionadas o influyentes e el rendimiento de la cosecha tales como temperatura, precipitaciones, tipo de suelo, Ph de suelo.

## Modelo de regresion lineal 
se aplica para entender cómo las variables climáticas, prácticas agrícolas y otros factores influyen en los rendimientos de cosechas de café.

El modelo resultante busca capturar la tendencia general y proporciona a los agricultores una herramienta para anticipar los posibles rendimientos de sus cultivos, lo que facilita la toma de decisiones informada en la gestión agrícola.

````pseudocode
y=mx+b
````
+ y es la variable dependiente que queremos predecir.
+ x es la variable independiente.
+ m es la pendiente de la línea, que representa el cambio en y por cada unidad de cambio en x.
+ b es la ordenada al origen o la intersección de la línea con el eje y cuando x es igual a cero.
## Error cuadratico medio
el método del error cuadratico medio que este funciona para evaluar la precisión del modelo e regresión lineal, un valor mas cercano a 0 es una prediccion mas precisa 
## CVS
Para guardar las variables usadas se guardaron los datos en un archivo CVS, este representa los datos en forma de tabla, las columnas se separan por comas y las filas por saltos en linea
````python
"Año": 2020, "PH": 5.8, "Temperatura": 15.6, "Precipitacion": 2870, "Rendimientos": 18.5, "Humedad": 85
"Año": 2021, "PH": 5.2, "Temperatura": 15.2, "Precipitacion": 2800, "Rendimientos": 17.3, "Humedad": 80
"Año": 2022, "PH": 5.4, "Temperatura": 15.8, "Precipitacion": 2859, "Rendimientos": 18.0, "Humedad": 83


