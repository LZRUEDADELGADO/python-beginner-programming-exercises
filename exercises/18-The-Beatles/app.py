# ✅↓ Write your code here ↓✅
def sing():
    # Frases repetidas
    let_it_be = "let it be,"
    wisdom = "whisper words of wisdom, let it be"
    answer = "there will be an answer,"

    # Construcción de la letra
    result = ""  # Inicializar la cadena

    # Repetir "let it be," 4 veces
    for _ in range(4):
        result += let_it_be + "\n"

    # Agregar "there will be an answer,"
    result += answer + "\n"

    # Repetir "let it be," 5 veces
    for _ in range(5):
        result += let_it_be + "\n"

    # Agregar "whisper words of wisdom, let it be" sin salto al final
    result += wisdom

    return result  # Devolver la cadena completa

# Llamar a la función y mostrar el resultado
print(sing())


