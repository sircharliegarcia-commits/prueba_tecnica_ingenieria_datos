#ejercicio_1_dataset_telefonos_clientes

##Proyecto
A partir de lod datos crudos, se diseña un dataset confiable de numero de telefonos de clientes con la aplicación de reglas de limpieza, normalización y validacion de calidad. Se automatiza con CI/CD para garantizar consistencia.

##Estructura del proyecto

1. ingesta de datos
2. Limpieza y normalización
3. Validaciones (números nulos, formato telefono,longitud mínima, eliminar duplicados)
5. Generación del dataset final
6. Ejecución automatica CI/CD

#Repositorio

├── data/
│ ├── cruda/ # Datos de entrada
│ └── procesados/ # Dataset final
├── sql/
│ ├── telefonos_limpieza.sql
│ └── validaciones.sql
├── src/
│ └── run_pipeline.py
├── .github/workflows/
│ └── ci-cd.yml
├── .gitignore
├── README.md
└── requirements.txt