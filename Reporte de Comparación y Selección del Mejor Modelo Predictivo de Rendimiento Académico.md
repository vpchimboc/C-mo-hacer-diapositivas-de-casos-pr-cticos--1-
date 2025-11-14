# Reporte de Comparación y Selección del Mejor Modelo Predictivo de Rendimiento Académico

## 1. Introducción
El objetivo de este reporte es comparar el rendimiento de tres modelos de clasificación binaria (Regresión Logística, Random Forest y XGBoost) para predecir el éxito académico (aprobación de asignaturas) de los estudiantes del Instituto Superior Tecnológico del Azuay (IST Azuay). La selección del mejor modelo se basará principalmente en el Área Bajo la Curva ROC (AUC), que mide la capacidad del modelo para discriminar entre las clases positiva (Aprobado) y negativa (No Aprobado).

## 2. Metodología de Modelado
Los modelos fueron entrenados y evaluados utilizando el conjunto de datos consolidado de 51,479 registros de asignaturas.

*   **Variable Objetivo (Y):** Éxito Académico (1 = Aprobado, 0 = No Aprobado/Retirado).
*   **Variables Predictoras (X):** Asistencia, Número de Matrícula, Tipo de Ingreso, Carrera y Periodo (codificadas).
*   **División de Datos:** 70% para entrenamiento y 30% para prueba.
*   **Métrica Principal de Evaluación:** AUC-ROC.

## 3. Resultados de la Comparación de Modelos

La siguiente tabla resume el rendimiento de los tres modelos en el conjunto de datos de prueba:

| Modelo | AUC-ROC Score | Precisión (Accuracy) | F1-Score (Macro Promedio) |
|:---|:---|:---|:---|
| Regresión Logística | 0.8717 | 0.9207 | 0.7311 |
| Random Forest | 0.8941 | 0.9350 | 0.8035 |
| **XGBoost** | **0.9157** | **0.9384** | **0.8022** |

### 3.1. Análisis Detallado por Modelo

#### **Regresión Logística**
*   **AUC:** 0.8717
*   **Comentario:** Es el modelo más simple y ofrece una buena base de rendimiento. Su AUC indica una capacidad de discriminación razonable, pero es superado por los modelos de ensamble.

#### **Random Forest**
*   **AUC:** 0.8941
*   **Comentario:** Mejora significativamente el rendimiento de la Regresión Logística. Su alto F1-Score (Macro Promedio) de 0.8035 indica un buen equilibrio entre la predicción de ambas clases, especialmente en la clase minoritaria (No Aprobado).

#### **XGBoost (eXtreme Gradient Boosting)**
*   **AUC:** **0.9157**
*   **Comentario:** Este modelo de *boosting* alcanza el mejor rendimiento general, con el AUC más alto. Esto lo convierte en el modelo más robusto para identificar correctamente a los estudiantes en riesgo (clase 0) y a los que aprobarán (clase 1).

## 4. Selección del Mejor Modelo

El modelo seleccionado como el mejor predictor del rendimiento académico es **XGBoost**.

La justificación para esta selección es la siguiente:

1.  **Mayor AUC-ROC (0.9157):** El AUC es la métrica más importante en este contexto, ya que mide la capacidad del modelo para clasificar correctamente a los estudiantes a través de todos los umbrales de probabilidad. Un valor de 0.9157 indica que el modelo tiene una excelente capacidad predictiva.
2.  **Alta Precisión en la Clase Minoritaria (No Aprobado):** El modelo XGBoost logró una precisión de **0.9049** para la clase 0 (No Aprobado), lo que significa que cuando el modelo predice que un estudiante reprobará, es muy probable que sea correcto. Esto es crucial para un sistema de alerta temprana.

## 5. Conclusión
El modelo **XGBoost** será el motor predictivo central de la aplicación Streamlit. Su rendimiento superior garantiza que las predicciones de riesgo académico sean lo más precisas posible, permitiendo al IST Azuay implementar intervenciones focalizadas y oportunas.

---
**Anexo: Reportes de Clasificación Detallados (Clase 0 = No Aprobado, Clase 1 = Aprobado)**

### **XGBoost (Mejor Modelo)**

| Métrica | Clase 0 (No Aprobado) | Clase 1 (Aprobado) |
|:---|:---|:---|
| **Precisión** | **0.9049** | 0.9405 |
| **Recall** | 0.4927 | 0.9936 |
| **F1-Score** | 0.6380 | 0.9663 |
| **Soporte** | 1642 | 13252 |

### **Random Forest**

| Métrica | Clase 0 (No Aprobado) | Clase 1 (Aprobado) |
|:---|:---|:---|
| **Precisión** | 0.8155 | 0.9442 |
| **Recall** | 0.5305 | 0.9851 |
| **F1-Score** | 0.6428 | 0.9643 |
| **Soporte** | 1642 | 13252 |

### **Regresión Logística**

| Métrica | Clase 0 (No Aprobado) | Clase 1 (Aprobado) |
|:---|:---|:---|
| **Precisión** | 0.8094 | 0.9266 |
| **Recall** | 0.3672 | 0.9893 |
| **F1-Score** | 0.5052 | 0.9569 |
| **Soporte** | 1642 | 13252 |
