"""
Ejercicio: Convertor de temperatura
Realizar dos funciones para convertir grados celsius a fahrenheit y viceversa.
"""


def celsius_a_fahrenheit(gradosC):
    gradosF = gradosC * 1.8 + 32
    return print(f'Los {gradosC} Celsius son equivalentes a {gradosF} Fahrenheit')


def fahrenheit_a_celsius(gradosF):
    gradosC = (gradosF - 32) / 1.8
    return print(f'Los {gradosF} Fahrenheit son equivalentes a {gradosC} Celsius')

# Ejemplos de prueba
celsius_a_fahrenheit(30)
fahrenheit_a_celsius(86)