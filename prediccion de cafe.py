
import csv

# Datos a guardar en el archivo CSV
datos = [
    {"Año": 2020, "PH": 5.8, "Temperatura": 15.6, "Precipitacion": 2870, "Rendimientos": 18.5, "Humedad": 85},
    {"Año": 2021, "PH": 5.2, "Temperatura": 15.2, "Precipitacion": 2800, "Rendimientos": 17.3, "Humedad": 80},
    {"Año": 2022, "PH": 5.4, "Temperatura": 15.8, "Precipitacion": 2859, "Rendimientos": 18.0, "Humedad": 83},
]

# Nombre del archivo CSV
nombreArchivo = 'datosCafeGuardados.csv'

# Nombre de las variables elegidas 
campos = ["Año", "PH", "Temperatura", "Precipitacion", "Rendimientos", "Humedad"]

# Escribir datos en el archivo CSV
with open(nombreArchivo, 'w', newline='') as csvfile:
    # Configurar el escritor CSV
    escritor = csv.DictWriter(csvfile, fieldnames=campos)

    # Escribir el encabezado
    escritor.writeheader()

    # Escribir filas de datos
    escritor.writerows(datos)

print(f"Datos guardados en {nombreArchivo}")

def cargarDatosDesdeArchivo(nombreArchivo):
    datos = []
    with open(nombreArchivo, 'r') as file:
        lineas = file.readlines()
        columnas = lineas[0].strip().split(',')

        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            registro = dict(zip(columnas, valores))
            datos.append(registro)

    return datos

# Función para preprocesar datos
def preprocesarDatos(datos):
    return datos

# Función para dividir datos en conjuntos de entrenamiento y prueba
def dividirDatos(datos):
    indexSplit = int(0.8 * sum(1 for _ in datos))
    dataTrain = datos[:indexSplit]
    dataTest = datos[indexSplit:]
    return dataTrain, dataTest

# Función para entrenar modelo de regresión
def entrenarModelo(dataTrain):
    promedioRendimientos = sum(float(registro['Rendimientos']) for registro in dataTrain) / sum(1 for _ in dataTrain)
    return {'promedioRendimientos': promedioRendimientos}

# Función para evaluar modelo
def evaluarModelo(modelo, dataTest):
    promedioRendimientosModelo = modelo['promedioRendimientos']
    rendimientosReales = [float(registro['Rendimientos']) for registro in dataTest]
    mse = sum((real - promedioRendimientosModelo) ** 2 for real in rendimientosReales) / sum(1 for _ in rendimientosReales)

    print("Rendimientos reales:", rendimientosReales)
    print("Predicciones del modelo:", [promedioRendimientosModelo] * sum(1 for _ in rendimientosReales))
    print(f"Error Cuadrático Medio (MSE): {mse}")

# Función para predecir rendimientos de café
def predecirRendimientos(modelo, característicasTerreno):

    # Parámetros de la fórmula 
    pesoPH = 0.5
    pesoTemperatura = 1.2
    pesoPrecipitacion = 0.8

    # Intercepto
    intercepto = 10.0

    rendimientoPredicho = (
        intercepto +
        pesoPH * característicasTerreno['PH'] +
        pesoTemperatura * característicasTerreno['Temperatura'] +
        pesoPrecipitacion * característicasTerreno['Precipitacion']
    )

    return rendimientoPredicho

# Función para predecir cultivo de café en base a las características del terreno
def predecirCultivoCafe(modelo, característicasTerreno):
    promedioRendimientosModelo = modelo['promedioRendimientos']
    
    #Condición para el tipo de cultivo
    if (5.5 < característicasTerreno['PH'] < 6.5 and
        18 < característicasTerreno['Temperatura'] < 21 and
        70 < característicasTerreno['Humedad'] < 95):
        return "Café Borbon"
    elif (5.5 < característicasTerreno['PH'] < 6.5 and
        18 < característicasTerreno['Temperatura'] < 24 and
        75 < característicasTerreno['Humedad'] < 85):
        return "Café Robusta"
    
    else:
        return "Cultivo de café no determinado"

def ejecutarPrograma():
    datos = cargarDatosDesdeArchivo('datosCafeGuardados.csv')
    datosPreprocesados = preprocesarDatos(datos)
    dataTrain, dataTest = dividirDatos(datosPreprocesados)
    modeloEntrenado = entrenarModelo(dataTrain)
    evaluarModelo(modeloEntrenado, dataTest)

    print("Ingrese las características del terreno que se va a predeci:")
    caracteristicasTerreno = {
        'PH': float(input("Valor de pH del suelo: ")),
        'Temperatura': float(input("Temperatura promedio del terreno en grados centígrados: ")),
        'Precipitacion': float(input("Precipitación anual en milímetros: ")),
        'Humedad': float(input("Humedad del suelo en porcentaje: ")),  # Nueva línea para ingresar la humedad
    }

    # Pregunta al usuario el número de hectáreas
    numeroHectareas = float(input("Ingrese el número de hectáreas del terreno: "))

    # Realizar la predicción de rendimientos y bultos de café
    rendimientoPredicho = predecirRendimientos(modeloEntrenado, caracteristicasTerreno)
    bultosPorHectarea = 18.8  
    bultosPredichos =  numeroHectareas * bultosPorHectarea

    print(f"Según las características del terreno proporcionadas, se predicen aproximadamente {bultosPredichos} bultos de café.")

    # Predecir el cultivo de café
    cultivoPredicho = predecirCultivoCafe(modeloEntrenado, caracteristicasTerreno)
    print(f"Según las características del terreno proporcionadas, el cultivo de café predicho es: {cultivoPredicho}")

if __name__ == "__main__":
    ejecutarPrograma()
