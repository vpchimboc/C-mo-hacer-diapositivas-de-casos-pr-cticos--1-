import pandas as pd
import os

# Directorio donde se encuentran los archivos
data_dir = "academic_data"
files = [f for f in os.listdir(data_dir) if f.endswith('.xls')]
files.sort()

all_data = []
new_column_names = [
    "Periodo", "Paralelo", "Identificacion_Estudiante", "Estudiante", "Carrera", 
    "Nivel", "Asignatura", "Num_matricula", "Asistencia", "Nota_final", 
    "Estado_Asignatura", "Estado_Matricula", "Tipo_Ingreso", "Cedula_docente", 
    "Nombre_docente"
]

print(f"Iniciando la carga y procesamiento de {len(files)} archivos...")

for file_name in files:
    file_path = os.path.join(data_dir, file_name)
    try:
        # Leer el archivo, usando la fila 3 (índice 2) como encabezado
        df = pd.read_excel(file_path, header=2, engine='xlrd')
        
        # Eliminar las primeras dos filas que contienen metadatos y encabezados duplicados
        df = df.iloc[2:].copy()
        
        # Renombrar las columnas para mayor claridad y consistencia
        # Se asume que las columnas relevantes comienzan en la columna 1 (índice 1)
        # y que las columnas 'Unnamed' son las que se deben descartar o renombrar
        
        # Seleccionar las columnas relevantes y renombrarlas
        # Se asume que las columnas de interés son de la 'Unnamed: 1' a la 'Unnamed: 17'
        # y que corresponden a los nombres definidos en new_column_names
        
        # El script anterior mostró que las columnas relevantes son:
        # Unnamed: 1 (Periodo)
        # Unnamed: 2 (Paralelo)
        # Unnamed: 3 (Identificacion)
        # Unnamed: 4 (Estudiante)
        # Unnamed: 5 (Carrera)
        # Unnamed: 6 (Nivel)
        # Unnamed: 7 (Asignatura)
        # Unnamed: 8 (Num_matricula)
        # Unnamed: 10 (Asistencia)
        # Unnamed: 11 (Nota final) - Este es el valor que falta en la fila 3, pero aparece en la fila 4
        # Unnamed: 12 (Estado)
        # Unnamed: 14 (Estado Matrícula)
        # Unnamed: 15 (Tipo Ingreso)
        # Unnamed: 16 (Cédula docente)
        # Unnamed: 17 (Nombre docente)
        
        # Vamos a usar los nombres de columna de la fila 3 (índice 2) y luego corregir
        # Las columnas que nos interesan son:
        # Periodo, Paralelo, Identificacion, Estudiante, Carrera, Nivel, Asignatura, Num_matricula, Asistencia, Nota final, Estado, Estado Matrícula, Tipo Ingreso, Cédula docente, Nombre docente
        
        # El problema es que el encabezado real está en la fila 3, pero la lectura con header=2 lo toma como la fila 3.
        # La forma más segura es leer sin encabezado y asignar los nombres manualmente.
        
        df_raw = pd.read_excel(file_path, header=None, engine='xlrd')
        
        # Identificar la fila de encabezado (fila 3, índice 2)
        header_row = df_raw.iloc[2]
        
        # Las columnas de interés son:
        # Columna 1: Periodo
        # Columna 2: Paralelo
        # Columna 3: Identificacion
        # Columna 4: Estudiante
        # Columna 5: Carrera
        # Columna 6: Nivel
        # Columna 7: Asignatura
        # Columna 8: Num_matricula
        # Columna 10: Asistencia
        # Columna 11: Nota final (Esta columna tiene NaN en el encabezado, pero es la nota)
        # Columna 12: Estado
        # Columna 14: Estado Matrícula
        # Columna 15: Tipo Ingreso
        # Columna 16: Cédula docente
        # Columna 17: Nombre docente
        
        # Seleccionar las columnas por índice (0-based)
        # Indices: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17
        df_clean = df_raw.iloc[3:, [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17]].copy()
        df_clean.columns = new_column_names
        
        # Limpieza de datos: convertir Nota_final a numérico, forzando errores a NaN
        df_clean['Nota_final'] = pd.to_numeric(df_clean['Nota_final'], errors='coerce')
        
        # Eliminar filas donde la Nota_final es NaN (probablemente filas de encabezado o pie de página)
        df_clean.dropna(subset=['Nota_final'], inplace=True)
        
        all_data.append(df_clean)
        print(f"Archivo {file_name} cargado con {len(df_clean)} registros.")
        
    except Exception as e:
        print(f"Error al procesar el archivo {file_name}: {e}")

if all_data:
    # Concatenar todos los DataFrames
    df_master = pd.concat(all_data, ignore_index=True)
    
    # Guardar el DataFrame consolidado en un archivo CSV para el análisis
    output_path = "academic_performance_master.csv"
    df_master.to_csv(output_path, index=False)
    
    print(f"\nDatos consolidados exitosamente en {output_path}")
    print(f"Total de registros consolidados: {len(df_master)}")
    print("\nPrimeras 5 filas del DataFrame consolidado:")
    print(df_master.head().to_markdown(index=False, numalign="left", stralign="left"))
    
    # Guardar un resumen de la estructura
    with open("master_data_summary.txt", "w") as f:
        f.write(f"Total de registros consolidados: {len(df_master)}\n\n")
        f.write("Primeras 5 filas:\n")
        f.write(df_master.head().to_markdown(index=False, numalign="left", stralign="left"))
        f.write("\n\nInformación de las columnas:\n")
        df_master.info(buf=f)
else:
    print("No se pudo cargar ningún archivo. Revisar el proceso.")
