# Caracterización de áreas celulares en frutos de tres variedades de arándano

**Autor/a:** Santiago  
**Curso:** Data Science en Recursos Naturales — Universidad de Chile  
**Tipo de trabajo:** Documentación y propuesta de análisis exploratorio de datos (EDA)  
**Estado:** Documentación inicial; las comparaciones estadísticas están pendientes de validación.

## 1. Descripción del proyecto

Este repositorio documenta un conjunto de mediciones anatómicas de frutos de arándano correspondientes a tres variedades, codificadas en el archivo como 1, 2 y 3. La finalidad es organizar la información, explicitar los criterios de calidad de datos y proponer un análisis exploratorio reproducible.
El archivo de origen contiene una hoja llamada `Hoja1 (2)`, con 72 observaciones (24 registros por código de variedad), una columna identificadora y cuatro columnas de medidas anatómicas. Las observaciones originales no se publican en este repositorio.

## 2. Pregunta de trabajo

¿Cómo varían las mediciones registradas del mesocarpo medio, mesocarpo externo, epidermis e hipodermis entre las tres variedades codificadas de arándano?
Se plantea una comparación exploratoria y descriptiva; no se afirma que existan diferencias estadísticamente significativas.

## 3. Objetivos

**Objetivo general:** organizar, documentar y proponer un análisis exploratorio de las mediciones anatómicas en frutos de tres variedades de arándano.

**Objetivos específicos:**

-Identificar las variables y sus códigos en el archivo original.
-Revisar la consistencia de unidades, codificación y valores no disponibles.
-Resumir cada variable por variedad mediante estadísticas descriptivas.
-Proponer gráficos que faciliten la comparación de distribuciones entre los tres grupos.
-Registrar el trabajo documental mediante ramas, commits, un pull request y merge en GitHub.

## 4. Características del estudio

El estudio considera mediciones anatómicas realizadas en frutos de tres variedades de arándano, identificadas mediante los códigos 1, 2 y 3.

| Característica | Descripción |
|---|---|
| Material vegetal | Frutos de arándano |
| Número de variedades | 3 |
| Identificación | Variedades codificadas como 1, 2 y 3 |
| Total de observaciones | 72 |
| Distribución de registros | 24 observaciones por variedad |
| Variables anatómicas | 4 |
| Tejidos evaluados | Mesocarpo medio, mesocarpo externo, epidermis e hipodermis |
| Registros por verificar | Dos valores identificados como `sd` |

Las mediciones permiten plantear un análisis exploratorio de las características anatómicas de los frutos de las tres variedades de arándano.

## 5. Variables registradas

| Nombre original de columna | Descripción orientativa | Observación |
|---|---|---|
| `variedad` | Código de grupo: 1, 2 o 3 | Nombres de variedades por confirmar |
| `área c mesocarpo medio (um2)` | Área celular del mesocarpo medio | Encabezado indica `um2` |
| `áre c mesocarpo externo (um2)` | Área celular del mesocarpo externo | Encabezado indica `um2`; contiene una celda `sd` |
| `Área c epidermis (um)` | Medida celular de epidermis | Encabezado indica `um`; contiene una celda `sd` |
| `Área c hipodermis (um)` | Medida celular de hipodermis | Encabezado indica `um` |

**Unidades pendientes de revisión:** aunque las columnas se refieren a áreas celulares, el archivo usa tanto `um2` como `um`. Antes de comunicar resultados con unidades físicas, se debe confirmar si todas las mediciones representan áreas expresadas en µm².


## 6. Plan de análisis exploratorio (propuesto)

Para caracterizar las diferencias anatómicas entre las tres variedades de arándano, se propone el siguiente procedimiento:

1. **Importación de datos:** leer el archivo Excel original en un equipo autorizado, sin publicar las observaciones experimentales.

2. **Exploración inicial:** inspeccionar el número de registros, los tipos de datos y los códigos correspondientes a cada variedad.

3. **Control de calidad:** verificar el significado de los valores `sd`, las unidades de medición y la correspondencia entre los códigos y los nombres de las variedades.

4. **Limpieza de datos:** identificar valores faltantes y convertir las variables a formatos numéricos cuando corresponda, sin modificar el archivo original.

5. **Análisis descriptivo:** calcular el número de observaciones válidas, media, mediana, desviación estándar y rangos de cada variable anatómica por variedad.

6. **Visualización:** elaborar histogramas y diagramas de caja (boxplots) para comparar la distribución de las mediciones entre variedades.

7. **Interpretación:** describir los patrones observados, considerando la variabilidad de las mediciones y las limitaciones del conjunto de datos.

La metodología se describe con mayor detalle en [Plan de análisis](docs/plan_analisis.md).

## 7. Estructura del repositorio

El repositorio se organiza en carpetas que permiten documentar el proyecto, identificar las variables anatómicas y mantener un flujo de trabajo reproducible.

```text
.
├── README.md
├── .gitignore
├── requirements.txt
├── docs/
│   ├── descripcion_datos.md
│   ├── diccionario_variables.md
│   └── plan_analisis.md
├── datos/
│   └── README.md
└── scripts/
    └── analisis_local.py
```

**Descripción de los archivos:**

- **README.md:** presenta el proyecto, sus objetivos, las variables estudiadas y la metodología propuesta.
- **docs/descripcion_datos.md:** describe la estructura del archivo original y las características de las observaciones.
- **docs/diccionario_variables.md:** documenta las cuatro variables anatómicas y sus unidades pendientes de verificación.
- **docs/plan_analisis.md:** explica las etapas de limpieza, análisis estadístico descriptivo y visualización.
- **datos/README.md:** informa sobre el origen de los datos y las restricciones para su publicación.
- **scripts/analisis_local.py:** contiene un ejemplo de análisis exploratorio utilizando Python y Pandas.
- **requirements.txt:** identifica las librerías necesarias para ejecutar el análisis.
- **.gitignore:** define archivos y carpetas que deben excluirse del control de versiones local.

El script de ejemplo está diseñado para analizar el Excel de manera local. No se presentan resultados científicos definitivos ni se publican las observaciones experimentales originales.

## 8. Cómo utilizar el ejemplo de análisis

El proyecto contempla el uso de Python y la librería Pandas para realizar un análisis exploratorio de las mediciones anatómicas de los frutos de arándano.

El procedimiento propuesto es el siguiente:

1. **Preparación de los datos:** conservar el archivo Excel original en una carpeta privada y trabajar con una copia autorizada.

2. **Importación:** utilizar `pandas.read_excel()` para cargar las mediciones en un DataFrame.

3. **Exploración inicial:** revisar la estructura de los datos mediante `head()`, `info()`, `shape` y `describe()`.

4. **Control de calidad:** identificar valores faltantes, verificar el significado de los registros `sd` y comprobar las unidades de medición.

5. **Agrupación por variedad:** utilizar `groupby()` para organizar las observaciones correspondientes a los códigos 1, 2 y 3.

6. **Estadística descriptiva:** calcular media, mediana, desviación estándar, valores mínimos y máximos para cada variable anatómica.

7. **Visualización:** elaborar histogramas y diagramas de caja para explorar las distribuciones de las mediciones entre variedades.

8. **Interpretación:** describir los patrones observados y sus limitaciones, sin afirmar diferencias estadísticamente significativas que no hayan sido comprobadas.

Para ejecutar el ejemplo de Python incluido en el repositorio, se debe guardar una copia autorizada del Excel en la carpeta local `datos_privados/`, utilizando el nombre `mediciones_originales.xlsx`, e instalar las dependencias indicadas en `requirements.txt`.

Los resultados del análisis se guardarán localmente en `resultados_locales/`, sin publicar automáticamente los datos de investigación.

El tratamiento de `sd` como valor ausente en el script es provisional y requiere confirmación antes de realizar el análisis definitivo.

## 9. Control de versiones y flujo de trabajo en GitHub

Para organizar el desarrollo del proyecto se utiliza GitHub como plataforma de control de versiones.

El flujo de trabajo contempla las siguientes etapas:

1. **Repositorio:** creación de un repositorio para centralizar la documentación y los archivos del proyecto.

2. **Rama de trabajo:** creación de la rama `readme-edits` a partir de `main`, permitiendo realizar modificaciones sin alterar inicialmente la versión principal.

3. **Commits:** registro de los cambios mediante mensajes descriptivos que permitan identificar las modificaciones realizadas.

4. **Pull Request:** propuesta de integración de los cambios de `readme-edits` hacia `main`, facilitando su revisión.

5. **Revisión y Merge:** verificación de los archivos modificados y posterior integración de los cambios a la rama principal.

Este procedimiento permite mantener un historial de modificaciones, documentar decisiones y facilitar la trazabilidad del proyecto.

## 10. Procedencia de los datos, ética y limitaciones

El conjunto de datos utilizado como referencia proviene de un archivo Excel asociado a un trabajo académico de investigación en frutos de arándano.

**Consideraciones principales:**

- **Material vegetal:** frutos correspondientes a tres variedades de arándano, identificadas mediante los códigos 1, 2 y 3.
- **Observaciones:** el archivo contiene 72 registros, distribuidos en 24 observaciones por código de variedad.
- **Variables:** mediciones celulares del mesocarpo medio, mesocarpo externo, epidermis e hipodermis.
- **Identificación varietal:** los nombres correspondientes a los códigos 1, 2 y 3 requieren confirmación.
- **Unidades de medición:** se debe verificar la consistencia de las unidades utilizadas en los encabezados del archivo original.
- **Datos no disponibles:** existen dos registros identificados como `sd`, cuyo significado requiere validación.
- **Diseño experimental:** es necesario verificar la unidad de muestreo y la independencia de las observaciones antes de realizar análisis inferenciales.
- **Confidencialidad:** las mediciones experimentales originales no se publican en este repositorio.
- **Interpretación:** cualquier comparación debe considerar las limitaciones del conjunto de datos y evitar conclusiones estadísticas sin respaldo.
- **Autorización:** la publicación de datos o resultados derivados requiere los permisos correspondientes.

El proyecto se presenta como una propuesta de organización y análisis exploratorio, sin atribuir resultados científicos que todavía no hayan sido validados.

## 11. Próximos pasos

Como continuación del proyecto se propone:

1. Confirmar la identidad de las tres variedades de arándano.
2. Verificar las unidades de las cuatro variables anatómicas.
3. Revisar y validar los registros identificados como `sd`.
4. Determinar la estructura de muestreo y las repeticiones experimentales.
5. Realizar la limpieza de datos utilizando Python y Pandas.
6. Obtener estadísticas descriptivas para cada variedad.
7. Elaborar visualizaciones que permitan comparar la distribución de las mediciones anatómicas.
8. Evaluar la pertinencia de análisis estadísticos adicionales de acuerdo con el diseño experimental.
9. Documentar los procedimientos y mantener el historial de modificaciones en GitHub.
10. Incorporar únicamente archivos y resultados autorizados para su publicación.

Este repositorio constituye una base documental para organizar y desarrollar el análisis de datos de un estudio anatómico de frutos de arándano, promoviendo buenas prácticas de trazabilidad, reproducibilidad y gestión de versiones.
