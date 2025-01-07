
try:
    age = int(input("Por favor, introduce tu edad: "))
    age +=10
    print("Your age is: " + str(age))  
except ValueError:
    print("Por favor, introduce un número válido.") 