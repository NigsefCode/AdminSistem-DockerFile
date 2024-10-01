import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Función para procesar y graficar datos
def procesar_datos():
    try:
        # Leer el archivo entrada.csv
        df = pd.read_csv('input/entrada.csv', parse_dates=['dia'])

        # Generar el gráfico de la UF en el tiempo
        plt.plot(df['dia'], df['valor_uf'], marker='o', linestyle='-')
        plt.xlabel('Día')
        plt.ylabel('Valor UF')
        plt.title('Variación de la UF en el tiempo')

        # Crear el nombre del archivo de salida con timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        output_filename = f'output/salida_{timestamp}.jpg'

        # Guardar el gráfico
        plt.savefig(output_filename)
        print(f'Gráfico guardado en: {output_filename}')

        # Agregar los datos al archivo entrada.csv.store
        with open('input/entrada.csv.store', 'a') as f_store:
            df.to_csv(f_store, header=False, index=False)

    except Exception as e:
        # Si ocurre algún error, registrar en error.log
        error_msg = f"Error: {str(e)}"
        with open('error.log', 'w') as f_error:
            f_error.write(error_msg)
        print('Se ha producido un error. Revisa el archivo error.log.')

if __name__ == "__main__":
    procesar_datos()
