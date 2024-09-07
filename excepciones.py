suma = 3000 
contador = 0 

 
def dividir(a, b): 
    if b == 0: 
        raise ZeroDivisionError("Division por cero.") 
    return a / b 
 
try: 
    resultado = dividir(suma, contador) 

except ZeroDivisionError as e: 
    print(f"Error {e}") 