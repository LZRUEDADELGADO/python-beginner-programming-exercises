import random

def get_color(color_number=4):
    # Making sure is a number and not a string
    color_number = int(color_number)

    switcher = {
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    
    return switcher.get(color_number, "Invalid Color Number")

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

def get_allStudentColors():
    students_array = []
    # ✅ ↓ your loop here ↓ ✅
    for _ in range(10):  # Iterar 10 veces, una por cada estudiante
        random_color_number = random.randint(0, 3)  # Generar un número aleatorio entre 0 y 3
        color = get_color(random_color_number)  # Obtener el color correspondiente
        students_array.append(color)  # Añadir el color a la lista
    return students_array  # Devolver la lista de colores

# Llamar a la función y mostrar el resultado
print(get_allStudentColors())
