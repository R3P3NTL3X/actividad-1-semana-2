#Sistema de gestion y recaudo de una aerolinea

# Importamos librería para generar fechas
from datetime import datetime

# Definimos precios en base a el destino escogido por el usuario
precios_base = {
    "nacional": {"destino": "Bogotá → Medellín", "precio": 230000},
    "internacional": {"destino": "Bogotá → España", "precio": 4200000}
}

# Definimos el costo del equipaje basandonos en el peso
def calcular_costo_equipaje_principal(peso):
    if peso <= 20:
        return 50000, "Admitido"
    elif peso <= 30:
        return 70000, "Admitido"
    elif peso <= 50:
        return 110000, "Admitido"
    else:
        return 0, "No admitido (Debe cancelar o viajar sin equipaje principal)"

# Validamos el equipaje de mano
def validar_equipaje_mano(peso):
    if peso <= 13:
        return "Admitido"
    else:
        return "Rechazado"

# Generador de ID de compra
def generar_id(numero):
    return f"COMP{numero:04d}"

# Lista para almacenar las compras realizadas
compras = []
contador_compras = 0

# Función principal para registrar una compra
def registrar_compra():
    global contador_compras

    nombre = input("Ingrese el nombre del pasajero: ")
    tipo_viaje = input("Tipo de viaje (nacional/internacional): ").lower()

    if tipo_viaje not in precios_base:
        print("❌ Tipo de viaje inválido. Intente de nuevo.")
        return

    try:
        peso_principal = float(input("Peso del equipaje principal (kg): "))
        lleva_mano = input("¿Lleva equipaje de mano? (si/no): ").lower()

        peso_mano = 0
        if lleva_mano == "si":
            peso_mano = float(input("Peso del equipaje de mano (kg): "))

        fecha_viaje = input("Ingrese la fecha del viaje (YYYY-MM-DD): ")

        # Validación de equipaje
        costo_equipaje, estado_principal = calcular_costo_equipaje_principal(peso_principal)
        estado_mano = validar_equipaje_mano(peso_mano)

        if estado_principal.startswith("No admitido"):
            print("⚠️ Advertencia: Su equipaje principal no es admitido. Se registrará la compra sin costo de equipaje principal.")
            costo_equipaje = 0

        # Generamos ID de compra
        contador_compras += 1
        id_compra = generar_id(contador_compras)

        # Calculamos costo total
        precio_base = precios_base[tipo_viaje]["precio"]
        total_pagar = precio_base + costo_equipaje

        # Guardamos la compra
        compra = {
            "id": id_compra,
            "nombre": nombre,
            "destino": precios_base[tipo_viaje]["destino"],
            "tipo_viaje": tipo_viaje,
            "fecha": fecha_viaje,
            "estado_principal": estado_principal,
            "estado_mano": estado_mano,
            "total": total_pagar
        }

        compras.append(compra)

        # Mostramos resumen (claramente)
        print("\n=====================")
        print("✅ COMPRA REGISTRADA")
        print("=====================")
        print(f"ID de compra (Guárdelo bien): ** {id_compra} **")
        print(f"Nombre del pasajero: {nombre}")
        print(f"Destino: {precios_base[tipo_viaje]['destino']}")
        print(f"Fecha: {fecha_viaje}")
        print(f"Estado del equipaje principal: {estado_principal}")
        print(f"Estado del equipaje de mano: {estado_mano}")
        print(f"Costo total del viaje: ${total_pagar:,.0f}")
        print("=====================\n")

    except ValueError:
        print("❌ Error: Ingreso inválido. Intente de nuevo.")

# Consultar compra por ID
def consultar_compra():
    id_buscar = input("Ingrese el ID de compra a consultar (ejemplo COMP0001): ").upper()
    for c in compras:
        if c["id"] == id_buscar:
            print("\n--- Detalle de la compra ---")
            print(f"ID de compra: {c['id']}")
            print(f"Nombre del pasajero: {c['nombre']}")
            print(f"Destino: {c['destino']}")
            print(f"Fecha: {c['fecha']}")
            print(f"Estado del equipaje principal: {c['estado_principal']}")
            print(f"Estado del equipaje de mano: {c['estado_mano']}")
            print(f"Costo total del viaje: ${c['total']:,.0f}")
            return
    print("❌ ID no encontrado. Revise que esté bien escrito.")

# Listado de TODAS las compras registradas (para verificar)
def listar_compras():
    if not compras:
        print("⚠️ No hay compras registradas aún.")
        return
    print("\n=== LISTADO DE COMPRAS ===")
    for c in compras:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Destino: {c['destino']} | Fecha: {c['fecha']} | Total: ${c['total']:,.0f}")
    print("===========================\n")

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar compra")
        print("2. Consultar compra por ID")
        print("3. Ver todas las compras registradas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_compra()
        elif opcion == "2":
            consultar_compra()
        elif opcion == "3":
            listar_compras()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

# Ejecutamos el menú
menu()
