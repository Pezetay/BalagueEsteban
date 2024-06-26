import random
import csv
import math

# Lista de nombres de clientes
NOMBRES_CLIENTES = [
    "Esteban", "Ariel", "Luciano", "Jeff", "Bryan", 
    "Cris", "Agustin", "Michael", "Paula", "Jazmin"
]

# Función para asignar saldos aleatorios a 10 clientes
def asignar_saldos():
    return [(nombre, random.randint(100000, 10000)) for nombre in NOMBRES_CLIENTES]

# Función para clasificar saldos en tres rangos
def clasificar_saldos(saldos):
    rango_bajo = [saldo for nombre, saldo in saldos if saldo < 300000]
    rango_medio = [saldo for nombre, saldo in saldos if 300000 <= saldo <= 700000]
    rango_alto = [saldo for nombre, saldo in saldos if saldo > 700000]
    return rango_bajo, rango_medio, rango_alto

# Función para calcular estadísticas
def calcular_estadisticas(saldos):
    saldos_values = [saldo for nombre, saldo in saldos]
    saldo_maximo = max(saldos_values)
    saldo_minimo = min(saldos_values)
    saldo_promedio = sum(saldos_values) / len(saldos_values)
    media_geometrica = math.exp(sum(math.log(saldo) for saldo in saldos_values) / len(saldos_values))
    return saldo_maximo, saldo_minimo, saldo_promedio, media_geometrica

# Función para generar reporte y exportar a CSV
def generar_reporte(saldos, deducciones):
    with open('reporte_saldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Cliente', 'Saldo Inicial', 'Deduccion 1', 'Deduccion 2', 'Deduccion 3', 'Saldo Neto'])
        for nombre, saldo in saldos:
            deduccion1 = deducciones.get('deduccion1', 0)
            deduccion2 = deducciones.get('deduccion2', 0)
            deduccion3 = deducciones.get('deduccion3', 0)
            saldo_neto = saldo - deduccion1 - deduccion2 - deduccion3
            writer.writerow([nombre, saldo, deduccion1, deduccion2, deduccion3, saldo_neto])

# Función principal del programa
def main():
    print("Bienvenido al sistema de gestión de saldos del banco internacional")
    saldos = []
    
    while True:
        print("\nMenú:")
        print("1. Asignar saldos aleatorios a 10 clientes")
        print("2. Clasificar saldos en rangos")
        print("3. Ver estadísticas de saldos")
        print("4. Generar reporte de saldos y exportar a CSV")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            saldos = asignar_saldos()
            print("Saldos asignados aleatoriamente:")
            for nombre, saldo in saldos:
                print(f"{nombre}: {saldo}")
        
        elif opcion == '2':
            if not saldos:
                print("Primero debe asignar los saldos (opción 1)")
            else:
                rango_bajo, rango_medio, rango_alto = clasificar_saldos(saldos)
                print("Rango Bajo (< 300000):", [saldo for nombre, saldo in saldos if saldo in rango_bajo])
                print("Rango Medio (300000 - 700000):", [saldo for nombre, saldo in saldos if saldo in rango_medio])
                print("Rango Alto (> 700000):", [saldo for nombre, saldo in saldos if saldo in rango_alto])
        
        elif opcion == '3':
            if not saldos:
                print("Primero debe asignar los saldos (opción 1)")
            else:
                saldo_maximo, saldo_minimo, saldo_promedio, media_geometrica = calcular_estadisticas(saldos)
                print("Saldo más alto:", saldo_maximo)
                print("Saldo más bajo:", saldo_minimo)
                print("Saldo promedio:", saldo_promedio)
                print("Media geométrica:", media_geometrica)
        
        elif opcion == '4':
            if not saldos:
                print("Primero debe asignar los saldos (opción 1)")
            else:
                deducciones = {
                    'deduccion1': float(input("Ingrese el monto de la deducción 1: ")),
                    'deduccion2': float(input("Ingrese el monto de la deducción 2: ")),
                    'deduccion3': float(input("Ingrese el monto de la deducción 3: "))
                }
                generar_reporte(saldos, deducciones)
                print("Reporte generado y exportado a 'reporte_saldos.csv'")
        
        elif opcion == '5':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
