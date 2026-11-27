
"""Análisis exploratorio local de mediciones anatómicas de arándano.

Los datos originales no se publican.
El significado de 'sd' y las unidades deben verificarse.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]

RUTA = BASE / "datos_privados" / "mediciones_originales.xlsx"
SALIDA = BASE / "resultados_locales"

COLUMNAS = [
    "área c mesocarpo medio (um2)",
    "áre c mesocarpo externo (um2)",
    "Área c epidermis (um)",
    "Área c hipodermis (um)"
]

if not RUTA.exists():
    raise FileNotFoundError(
        "No se encontró el Excel en la carpeta privada."
    )

# Importación del Excel
# El tratamiento de 'sd' como ausente es provisional.
df = pd.read_excel(
    RUTA,
    sheet_name="Hoja1 (2)",
    na_values=["sd"]
)

# Verificación de columnas
requeridas = ["variedad"] + COLUMNAS

for columna in requeridas:
    if columna not in df.columns:
        raise ValueError(f"Falta la columna: {columna}")

# Conversión de las medidas a valores numéricos
for columna in COLUMNAS:
    df[columna] = pd.to_numeric(
        df[columna], errors="coerce"
    )

# Exploración inicial
print("Dimensiones:", df.shape)
print("\nObservaciones por variedad:")
print(df["variedad"].value_counts())

print("\nValores faltantes:")
print(df.isna().sum())

# Estadística descriptiva por variedad
resumen = df.groupby("variedad")[COLUMNAS].agg(
    ["count", "mean", "median", "std", "min", "max"]
)

print("\nResumen estadístico:")
print(resumen.round(2))

# Guardar resultados localmente
SALIDA.mkdir(exist_ok=True)

resumen.to_csv(
    SALIDA / "resumen_local.csv",
    encoding="utf-8-sig"
)

# Gráficos de caja
for i, columna in enumerate(COLUMNAS, start=1):
    grupos = []
    etiquetas = []

    for variedad, bloque in df.groupby("variedad"):
        valores = bloque[columna].dropna()

        if not valores.empty:
            grupos.append(valores)
            etiquetas.append(str(variedad))

    if grupos:
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.boxplot(grupos)
        ax.set_xticks(
            range(1, len(grupos) + 1),
            labels=etiquetas
        )

        ax.set_title(columna)
        ax.set_xlabel("Código de variedad")
        ax.set_ylabel("Unidad por verificar")

        fig.tight_layout()
        fig.savefig(
            SALIDA / f"boxplot_variable_{i}.png",
            dpi=160
        )
        plt.close(fig)

print("\nAnálisis exploratorio preparado.")
