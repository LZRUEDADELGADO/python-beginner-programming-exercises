import random

bullet_position = 3

def spin_chamber():
    chamber_position = random.randint(1, 6)  # Genera una posición entre 1 y 6
    return chamber_position

def fire_gun():
    chamber_position = spin_chamber()  # Obtener posición aleatoria de la recámara
    print(f"Debug: chamber_position={chamber_position}, bullet_position={bullet_position}")
    if chamber_position == bullet_position:  # Comparar con la posición de la bala
        return "You are dead!"
    else:
        return "Keep playing!"

print(fire_gun())
