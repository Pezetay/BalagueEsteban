import random
import csv
import math

# Función para asignar saldos aleatorios a 10 clientes
def asignar_saldos():
    return [random.uniform(1000, 10000) for _ in range(10)]

# Función para clasificar saldos en tres rangos
def clasificar_saldos(saldos):
    rango_bajo = [saldo for saldo in saldos if saldo < 3000]
    rango_medio = [saldo for saldo in saldos if 3000 <= saldo <= 7000]
    rango_alto = [saldo for saldo in saldos if saldo > 7000]
    return rango_bajo, rango_medio, rango_alto

# Función para calcular estadísticas
def calcular_estadisticas(saldos):
    saldo_maximo = max(saldos)
    saldo_minimo = min(saldos)
    saldo_promedio = sum(saldos) / len(saldos)
    media_geometrica = math.exp(sum(math.log(saldo) for saldo in saldos) / len(saldos))
    return saldo_maximo, saldo_minimo, saldo_promedio, media_geometrica

# Función para generar reporte y exportar a CSV
def generar_reporte(saldos, deducciones):
    with open('reporte_saldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Cliente', 'Saldo Inicial', 'Deducción 1', 'Deducción 2', 'Deducción 3', 'Saldo Neto'])
        for i, saldo in enumerate(saldos):
            deduccion1 = deducciones.get('deduccion1', 0)
            deduccion2 = deducciones.get('deduccion2', 0)
            deduccion3 = deducciones.get('deduccion3', 0)
            saldo_neto = saldo - deduccion1 - deduccion2 - deduccion3
            writer.writerow([i+1, saldo, deduccion1, deduccion2, deduccion3, saldo_neto])

# Función principal del programa
def main():
    print("Bienvenido al sistema de gestión de saldos del banco internacional")
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
            print(saldos)
        
        elif opcion == '2':
            if 'saldos' not in locals():
                print("Primero debe asignar los saldos (opción 1)")
            else:
                rango_bajo, rango_medio, rango_alto = clasificar_saldos(saldos)
                print("Rango Bajo (< 3000):", rango_bajo)
                print("Rango Medio (3000 - 7000):", rango_medio)
                print("Rango Alto (> 7000):", rango_alto)
        
        elif opcion == '3':
            if 'saldos' not in locals():
                print("Primero debe asignar los saldos (opción 1)")
            else:
                saldo_maximo, saldo_minimo, saldo_promedio, media_geometrica = calcular_estadisticas(saldos)
                print("Saldo más alto:", saldo_maximo)
                print("Saldo más bajo:", saldo_minimo)
                print("Saldo promedio:", saldo_promedio)
                print("Media geométrica:", media_geometrica)
        
        elif opcion == '4':
            if 'saldos' not in locals():
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
