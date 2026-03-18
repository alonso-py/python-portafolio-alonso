# prueba_inicial.py - Primer script en el portafolio

print("¡Portafolio vivo y venv activado! 🚀")
print("Fecha actual:", "17 de marzo 2026")  # solo para referencia

nombre = input("¿Cómo te llamas, crack? ")
edad = input("¿Cuántos años tienes? ")

try:
    edad_num = int(edad)
    print(f"Órale {nombre}, tienes {edad_num} años.")
    print(f"En 5 años tendrás {edad_num + 5}... ¡ya casi eres pro! 💪")
except ValueError:
    print("La edad debe ser un número, inténtalo de nuevo la próxima 😅")

# Prueba rápida de lista y comprehension (para refrescar basics)
numeros = list(range(1, 11))
cuadrados_impares = [x**2 for x in numeros if x % 2 != 0]
print("Cuadrados de números impares del 1 al 10:", cuadrados_impares)