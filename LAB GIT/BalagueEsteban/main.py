import random
import csv
import math

def generar_saldos():
    return [round(random.uniform(1000, 10000), 2) for _ in range(10)]

def clasificar_saldos(saldos):
    rango1 = [saldo for saldo in saldos if saldo < 3000]
    rango2 = [saldo for saldo in saldos if 3000 <= saldo <= 7000]
    rango3 = [saldo for saldo in saldos if saldo > 7000]
    return rango1, rango2, rango3

def calcular_estadisticas(saldos):
    saldo_maximo = max(saldos)
    saldo_minimo = min(saldos)
    saldo_promedio = sum(saldos) / len(saldos)
    media_geometrica = math.prod(saldos) ** (1/len(saldos))
    return saldo_maximo, saldo_minimo, saldo_promedio, media_geometrica

def generar_reporte(saldos):
    deducciones = {
        'impuesto': 0.10,  # 10%
        'seguro': 0.05,    # 5%
        'otros': 0.02      # 2%
    }

    reporte = []
    for idx, saldo in enumerate(saldos):
        impuesto = saldo * deducciones['impuesto']
        seguro = saldo * deducciones['seguro']
        otros = saldo * deducciones['otros']
        saldo_neto = saldo - impuesto - seguro - otros
        reporte.append({
            'Cliente': f'Cliente {idx + 1}',
            'Saldo': saldo,
            'Impuesto': impuesto,
            'Seguro': seguro,
            'Otros': otros,
            'Saldo Neto': saldo_neto
        })
    
    keys = reporte[0].keys()
    with open('reporte_saldos.csv', 'w', newline='') as archivo_csv:
        dict_writer = csv.DictWriter(archivo_csv, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(reporte)
    
    return reporte

def mostrar_menu():
    print("1. Asignar saldos aleatorios")
    print("2. Clasificar saldos")
    print("3. Ver estadísticas")
    print("4. Generar reporte de saldos")
    print("5. Salir")

def main():
    saldos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            saldos = generar_saldos()
            print("Saldos generados:", saldos)
        elif opcion == '2':
            if not saldos:
                print("Primero debe generar los saldos.")
            else:
                rango1, rango2, rango3 = clasificar_saldos(saldos)
                print("Rango 1 (< 3000):", rango1)
                print("Rango 2 (3000 - 7000):", rango2)
                print("Rango 3 (> 7000):", rango3)
        elif opcion == '3':
            if not saldos:
                print("Primero debe generar los saldos.")
            else:
                saldo_maximo, saldo_minimo, saldo_promedio, media_geometrica = calcular_estadisticas(saldos)
                print(f"Saldo más alto: {saldo_maximo}")
                print(f"Saldo más bajo: {saldo_minimo}")
                print(f"Saldo promedio: {saldo_promedio}")
                print(f"Media geométrica: {media_geometrica}")
        elif opcion == '4':
            if not saldos:
                print("Primero debe generar los saldos.")
            else:
                reporte = generar_reporte(saldos)
                print("Reporte generado y guardado en 'reporte_saldos.csv'.")
        elif opcion == '5':
            print("Gracias por usar la aplicación. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
