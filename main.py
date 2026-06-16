# ============================================================
# Trabajo Práctico Integrador - Programación 1
# Gestión de Datos de Países en Python: filtros, ordenamientos
# y estadísticas
# Alumna: Claudia Eugenia González
# ============================================================

import csv


# ── 1. CARGA DE DATOS DESDE CSV ──────────────────────────────
def cargar_paises(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un país con sus datos.
    Maneja errores de archivo no encontrado o formato incorrecto.
    """
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Fila inválida en el CSV, se omite: {fila} ({e})")
        print(f"✅ Se cargaron {len(paises)} países desde '{nombre_archivo}'.")
    except FileNotFoundError:
        print(f"❌ Error: no se encontró el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"❌ Error inesperado al leer el archivo: {e}")

    return paises


def guardar_paises(paises, nombre_archivo):
    """Sobrescribe el archivo CSV con la lista completa de países actualizada."""
    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        print(f"✅ Datos guardados correctamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")


# ── 2. AGREGAR PAÍS ───────────────────────────────────────────
def agregar_pais(paises):
    """Solicita los datos de un nuevo país y lo agrega a la lista.
    No permite campos vacíos ni nombres duplicados."""
    print("\n--- Agregar nuevo país ---")

    # Nombre: no vacío y no duplicado
    while True:
        nombre = input("Nombre del país: ").strip()
        if nombre == "":
            print("❌ El nombre no puede estar vacío.")
            continue
        if buscar_indice_por_nombre_exacto(paises, nombre) != -1:
            print(f"❌ '{nombre}' ya existe en la lista.")
            continue
        break

    # Población: entero positivo
    while True:
        try:
            poblacion = int(input("Población: "))
            if poblacion <= 0:
                print("❌ La población debe ser un número entero positivo.")
                continue
            break
        except ValueError:
            print("❌ Debe ingresar un número entero válido.")

    # Superficie: entero positivo
    while True:
        try:
            superficie = int(input("Superficie (km²): "))
            if superficie <= 0:
                print("❌ La superficie debe ser un número entero positivo.")
                continue
            break
        except ValueError:
            print("❌ Debe ingresar un número entero válido.")

    # Continente: no vacío
    while True:
        continente = input("Continente: ").strip()
        if continente == "":
            print("❌ El continente no puede estar vacío.")
            continue
        break

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    print(f"✅ País '{nombre}' agregado correctamente.")


# ── 3. ACTUALIZAR DATOS DE UN PAÍS ───────────────────────────
def actualizar_pais(paises):
    """Permite actualizar la población y/o superficie de un país existente."""
    if len(paises) == 0:
        print("⚠️  No hay países cargados.")
        return

    nombre = input("\nIngrese el nombre del país a actualizar: ").strip()
    indice = buscar_indice_por_nombre_exacto(paises, nombre)

    if indice == -1:
        print(f"❌ No se encontró el país '{nombre}'.")
        return

    pais = paises[indice]
    print(f"Datos actuales de {pais['nombre']}: "
          f"Población={pais['poblacion']}, Superficie={pais['superficie']}")

    try:
        nueva_poblacion = input("Nueva población (Enter para no modificar): ").strip()
        if nueva_poblacion != "":
            nueva_poblacion = int(nueva_poblacion)
            if nueva_poblacion <= 0:
                raise ValueError("La población debe ser positiva.")
            pais["poblacion"] = nueva_poblacion

        nueva_superficie = input("Nueva superficie (Enter para no modificar): ").strip()
        if nueva_superficie != "":
            nueva_superficie = int(nueva_superficie)
            if nueva_superficie <= 0:
                raise ValueError("La superficie debe ser positiva.")
            pais["superficie"] = nueva_superficie

        print(f"✅ Datos de '{pais['nombre']}' actualizados correctamente.")

    except ValueError as e:
        print(f"❌ Error: {e}. No se realizaron cambios.")


# ── FUNCIONES AUXILIARES DE BÚSQUEDA ─────────────────────────
def buscar_indice_por_nombre_exacto(paises, nombre):
    """Devuelve el índice del país con coincidencia EXACTA (sin mayúsculas/espacios) o -1."""
    nombre_norm = nombre.strip().lower()
    for i, pais in enumerate(paises):
        if pais["nombre"].strip().lower() == nombre_norm:
            return i
    return -1


# ── 4. BUSCAR PAÍS POR NOMBRE ─────────────────────────────────
def buscar_pais(paises):
    """Busca países cuyo nombre contenga (parcial o exacto) el texto ingresado."""
    if len(paises) == 0:
        print("⚠️  No hay países cargados.")
        return

    texto = input("\nIngrese el nombre (o parte del nombre) a buscar: ").strip().lower()

    encontrados = [p for p in paises if texto in p["nombre"].lower()]

    if len(encontrados) == 0:
        print(f"❌ No se encontraron países que coincidan con '{texto}'.")
    else:
        print(f"\n✅ Se encontraron {len(encontrados)} resultado/s:")
        mostrar_tabla(encontrados)


# ── 5. FILTRAR PAÍSES ─────────────────────────────────────────
def filtrar_por_continente(paises):
    """Filtra y muestra los países que pertenecen a un continente determinado."""
    if len(paises) == 0:
        print("⚠️  No hay países cargados.")
        return

    continente = input("\nIngrese el continente a filtrar: ").strip().lower()
    filtrados = [p for p in paises if p["continente"].lower() == continente]

    if len(filtrados) == 0:
        print(f"❌ No hay países en el continente '{continente}'.")
    else:
        print(f"\n✅ Países en {continente.capitalize()}:")
        mostrar_tabla(filtrados)


def filtrar_por_rango_poblacion(paises):
    """Filtra países cuya población esté dentro de un rango ingresado por el usuario."""
    if len(paises) == 0:
        print("⚠️  No hay países cargados.")
        return

    try:
        minimo = int(input("\nPoblación mínima: "))
        maximo = int(input("Población máxima: "))

        if minimo > maximo:
            print("❌ El valor mínimo no puede ser mayor que el máximo.")
            return

        filtrados = [p for p in paises if minimo <= p["poblacion"] <= maximo]

        if len(filtrados) == 0:
            print("❌ No hay países en ese rango de población.")
        else:
            print(f"\n✅ Países con población entre {minimo} y {maximo}:")
            mostrar_tabla(filtrados)

    except ValueError:
        print("❌ Debe ingresar valores numéricos enteros.")


def filtrar_por_rango_superficie(paises):
    """Filtra países cuya superficie esté dentro de un rango ingresado por el usuario."""
    if len(paises) == 0:
        print("⚠️  No hay países cargados.")
        return

    try:
        minimo = int(input("\nSuperficie mínima (km²): "))
        maximo = int(input("Superficie máxima (km²): "))

        if minimo > maximo:
            print("❌ El valor mínimo no puede ser mayor que el máximo.")
            return

        filtrados = [p for p in paises if minimo <= p["superficie"] <= maximo]

        if len(filtrados) == 0:
            print("❌ No hay países en ese rango de superficie.")
        else:
            print(f"\n✅ Países con superficie entre {minimo} y {maximo} km²:")
            mostrar_tabla(filtrados)

    except ValueError:
        print("❌ Debe ingresar valores numéricos enteros.")


# ── 6. ORDENAR PAÍSES ─────────────────────────────────────────
def ordenar_paises(paises):
    """Ordena y muestra los países según el criterio elegido por el usuario."""
    if len(paises) == 0:
        print("⚠️  No hay países cargados.")
        return

    print("\n--- Ordenar países por ---")
    print("  1. Nombre")
    print("  2. Población")
    print("  3. Superficie")

    try:
        criterio = int(input("Seleccione un criterio (1-3): "))
        if criterio not in [1, 2, 3]:
            print("❌ Opción inválida.")
            return

        orden = input("¿Orden ascendente o descendente? (a/d): ").strip().lower()
        if orden not in ["a", "d"]:
            print("❌ Opción inválida. Debe ingresar 'a' o 'd'.")
            return

        descendente = (orden == "d")

        if criterio == 1:
            ordenados = sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)
        elif criterio == 2:
            ordenados = sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)
        else:
            ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

        print(f"\n✅ Países ordenados:")
        mostrar_tabla(ordenados)

    except ValueError:
        print("❌ Debe ingresar un número entero.")


# ── 7. ESTADÍSTICAS ────────────────────────────────────────────
def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas generales del dataset de países."""
    if len(paises) == 0:
        print("⚠️  No hay países cargados.")
        return

    # País con mayor y menor población
    pais_mayor_poblacion = max(paises, key=lambda p: p["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda p: p["poblacion"])

    # Promedios
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)

    # Cantidad de países por continente
    conteo_continentes = {}
    for p in paises:
        continente = p["continente"]
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    print("\n" + "=" * 50)
    print(f"{'ESTADÍSTICAS GENERALES':^50}")
    print("=" * 50)
    print(f"País con MAYOR población: {pais_mayor_poblacion['nombre']} "
          f"({pais_mayor_poblacion['poblacion']:,} hab.)")
    print(f"País con MENOR población: {pais_menor_poblacion['nombre']} "
          f"({pais_menor_poblacion['poblacion']:,} hab.)")
    print(f"\nPromedio de población:  {promedio_poblacion:,.2f} hab.")
    print(f"Promedio de superficie: {promedio_superficie:,.2f} km²")

    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad}")
    print("=" * 50)


# ── FUNCIÓN AUXILIAR: MOSTRAR TABLA ──────────────────────────
def mostrar_tabla(paises):
    """Muestra una lista de países en formato de tabla."""
    print(f"\n{'Nombre':<20} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<12}")
    print("-" * 67)
    for p in paises:
        print(f"{p['nombre']:<20} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<12}")


# ── MENÚ PRINCIPAL ─────────────────────────────────────────────
def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n" + "=" * 50)
    print(f"{'GESTIÓN DE DATOS DE PAÍSES':^50}")
    print("=" * 50)
    print("  1. Mostrar todos los países")
    print("  2. Agregar país")
    print("  3. Actualizar población/superficie de un país")
    print("  4. Buscar país por nombre")
    print("  5. Filtrar por continente")
    print("  6. Filtrar por rango de población")
    print("  7. Filtrar por rango de superficie")
    print("  8. Ordenar países")
    print("  9. Mostrar estadísticas")
    print("  10. Guardar cambios en el archivo CSV")
    print("  11. Salir")
    print("=" * 50)


def main():
    """Función principal: controla el flujo del programa mediante un menú."""
    nombre_archivo = "paises.csv"
    paises = cargar_paises(nombre_archivo)

    opcion = 0
    while opcion != 11:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                if len(paises) == 0:
                    print("⚠️  No hay países cargados.")
                else:
                    mostrar_tabla(paises)
            elif opcion == 2:
                agregar_pais(paises)
            elif opcion == 3:
                actualizar_pais(paises)
            elif opcion == 4:
                buscar_pais(paises)
            elif opcion == 5:
                filtrar_por_continente(paises)
            elif opcion == 6:
                filtrar_por_rango_poblacion(paises)
            elif opcion == 7:
                filtrar_por_rango_superficie(paises)
            elif opcion == 8:
                ordenar_paises(paises)
            elif opcion == 9:
                mostrar_estadisticas(paises)
            elif opcion == 10:
                guardar_paises(paises, nombre_archivo)
            elif opcion == 11:
                print("\n👋 Saliendo del sistema. ¡Hasta pronto!")
            else:
                print("❌ Opción inválida. Ingrese un número entre 1 y 11.")

        except ValueError:
            print("❌ Opción inválida. Debe ingresar un número entero.")


if __name__ == "__main__":
    main()
