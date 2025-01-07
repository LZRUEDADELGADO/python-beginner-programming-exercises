# ✅↓ Write your code here ↓✅
def number_of_bottles():
    # Manejar el rango desde 99 hasta 3
    for x in range(99, 2, -1):
        print(f"{x} bottles of milk on the wall, {x} bottles of milk. Take one down and pass it around, {x - 1} bottles of milk on the wall.")
    
    # Caso especial para 2 botellas
    print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")
    
    # Caso especial para 1 botella
    print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
    
    # Última línea de la canción
    print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
    
    return None

# Llamar a la función
number_of_bottles()
