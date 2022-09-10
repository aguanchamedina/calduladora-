from math import log 

print("---------------------------")
print("--------CALCULADORA--------")
print("---------------------------")

#INPUT
bandera = False 

x = float(input("Dame el valor de el numero x: "))
y = float(input("Dame el valor de el numero y: "))

print("Dame la opcion que deseas realizar: \n")

# Se despliega el menu para colocar la opcion que deseas realizar 
print("1. Sumar (El primero mas el segundo)")
print("2. Restar (El primero meno el segundo)")
print("3. Multiplicar (El primero por el segundo)")
print("4. Dividir (El primero sobre el segundo)")
print("5. Potencia (El primero mas el segundo)")
print("6. Logaritmo (El logaritmo del segundo)")

opcion = int(input("\n dame la opción: "))