Edad=input("Inserta tu nombre y tu edad ")
parts = Edad.split()
edad_numerica_str = parts[-1]
try:
    edad_numerica = int(edad_numerica_str)
    print("Hola, tienes:", edad_numerica , "años")
except ValueError:
    print("No se pudo extraer un valor numérico para la edad.")