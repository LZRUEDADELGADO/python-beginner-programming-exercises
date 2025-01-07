def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for i in range(1, 101):  # Iterar desde 1 hasta 100
        if i % 3 == 0 and i % 5 == 0:  # Múltiplos de 3 y 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Múltiplos de 3
            print("Fizz")
        elif i % 5 == 0:  # Múltiplos de 5
            print("Buzz")
        else:  # Para todos los demás números
            print(i)

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
