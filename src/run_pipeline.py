import pandas as pd

# Datos crudos para cargar
df = pd.read_csv("datos/cruda/clientes_raw.csv")

# limpieza de telefonos
df["telefono_limpieza"] = df["numero_telefono"].str.replace(r"\D", "", regex=True)

# Reglas limpieza
df = df[df["telefono_limpieza"].notna()]
df = df[df["telefono_limpieza"].str.len() >= 10]
df = df.drop_duplicates(subset=["telefono_limpieza"])

# Guardar dataset final
df[["cliente_id", "telefono_limpieza"]].to_csv(
    "datos/procesados/telefono_dataset.csv",
    index=False
)

print("Se ha genereado el dataset de telefonos")
