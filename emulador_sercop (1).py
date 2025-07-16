
from decimal import Decimal, getcontext

# Configurar precisión
getcontext().prec = 20

def calcular_valor_unitario(valor_total_str, iva_str, cantidad_str):
    valor_total = Decimal(valor_total_str)
    iva = Decimal(iva_str)
    cantidad = Decimal(cantidad_str)

    resultado = valor_total / iva / cantidad
    return resultado

if __name__ == "__main__":
    print("=== Emulador SERCOP - Cálculo Unitario sin IVA ===")
    valor_total_input = input("Ingresa el valor total con IVA: ")
    iva_input = input("Ingresa el valor del IVA (ej. 1.15): ")
    cantidad_input = input("Ingresa la cantidad de unidades: ")

    resultado = calcular_valor_unitario(valor_total_input, iva_input, cantidad_input)
    print(f"Valor unitario sin IVA: {resultado}")
