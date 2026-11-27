
# Diccionario de variables del estudio

## 1. Descripción general

El conjunto de datos corresponde a mediciones anatómicas de frutos de tres variedades de arándano, identificadas mediante los códigos 1, 2 y 3.

Se dispone de 72 observaciones, distribuidas en 24 registros por código de variedad.

## 2. Variables registradas

| Variable | Tipo de dato | Descripción | Observaciones |
|---|---|---|---|
| `variedad` | Categórica | Código de variedad: 1, 2 o 3 | Nombres de cultivares pendientes de confirmación |
| `área c mesocarpo medio (um2)` | Numérica | Medición del mesocarpo medio del fruto | Verificar unidades de área |
| `áre c mesocarpo externo (um2)` | Numérica | Medición del mesocarpo externo del fruto | Contiene un registro `sd` |
| `Área c epidermis (um)` | Numérica | Medición celular de la epidermis | Contiene un registro `sd`; verificar unidades |
| `Área c hipodermis (um)` | Numérica | Medición celular de la hipodermis | Verificar unidades |

## 3. Clasificación de las variables

**Variable categórica:** `variedad`, que identifica tres grupos mediante los códigos 1, 2 y 3.

**Variables numéricas:** las cuatro mediciones anatómicas registradas en los distintos tejidos del fruto.

## 4. Consideraciones sobre las unidades

Los encabezados del Excel contienen tanto `um2` como `um`. Es necesario confirmar las unidades originales antes de interpretarlas como áreas expresadas en µm².

## 5. Valores pendientes de verificación

Se identificaron dos celdas con el texto `sd`. Su significado debe confirmarse antes de tratarlas como datos faltantes.

## 6. Aplicación en ciencia de datos

Se propone utilizar Python y Pandas para:

1. Importar los datos mediante `pd.read_excel()`.
2. Inspeccionar la estructura con `df.info()`.
3. Identificar valores faltantes mediante `df.isna()`.
4. Agrupar observaciones con `df.groupby()`.
5. Calcular estadísticas descriptivas mediante `df.agg()`.
6. Visualizar distribuciones mediante `sns.boxplot()`.

Estas operaciones forman parte del análisis exploratorio propuesto y no representan resultados estadísticos ya obtenidos.
