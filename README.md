# Gestión de Datos de Países en Python

## Descripción
Aplicación de consola desarrollada en Python para gestionar información de países (nombre, población, superficie y continente), permitiendo búsquedas, filtros, ordenamientos y estadísticas a partir de un dataset cargado desde un archivo CSV.

## Autora
Claudia Eugenia González — Tecnicatura Universitaria en Programación a Distancia — Programación 1

## Requisitos
- Python 3.x (no requiere librerías externas, solo `csv` de la biblioteca estándar)

## Cómo ejecutar
1. Asegurarse de que `main.py` y `paises.csv` estén en la misma carpeta.
2. Ejecutar:
   ```bash
   python main.py
   ```
3. Se mostrará un menú interactivo en la consola.

## Estructura del proyecto
```
tpi_paises/
├── main.py          # Código fuente principal
├── paises.csv        # Dataset base de países
└── README.md         # Este archivo
```

## Estructura de datos
Cada país se representa como un diccionario dentro de una lista:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América"
}
```

## Funcionalidades del menú

| Opción | Descripción |
|---|---|
| 1 | Mostrar todos los países cargados |
| 2 | Agregar un nuevo país (valida campos vacíos y duplicados) |
| 3 | Actualizar población y/o superficie de un país existente |
| 4 | Buscar país por nombre (coincidencia parcial) |
| 5 | Filtrar países por continente |
| 6 | Filtrar países por rango de población |
| 7 | Filtrar países por rango de superficie |
| 8 | Ordenar países por nombre, población o superficie (asc/desc) |
| 9 | Mostrar estadísticas generales (mayor/menor población, promedios, conteo por continente) |
| 10 | Guardar los cambios realizados en el archivo CSV |
| 11 | Salir del programa |

## Ejemplo de uso

```
==================================================
            GESTIÓN DE DATOS DE PAÍSES
==================================================
  1. Mostrar todos los países
  2. Agregar país
  ...
  11. Salir
==================================================
Seleccione una opción: 9

==================================================
              ESTADÍSTICAS GENERALES
==================================================
País con MAYOR población: China (1,412,600,000 hab.)
País con MENOR población: Nueva Zelanda (5,084,300 hab.)

Promedio de población:  227,593,487.60 hab.
Promedio de superficie: 3,856,461.60 km²

Cantidad de países por continente:
  - América: 6
  - Asia: 4
  - Europa: 5
  - África: 3
  - Oceanía: 2
==================================================
```

## Enlaces
- **Video demostrativo:** [pendiente de subir]
- **Documentación PDF:** ver `informe_TPI.pdf` en la raíz del repositorio
