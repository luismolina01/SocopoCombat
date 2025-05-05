import random

# Lista de personajes criollos
personajes = [
    {"nombre": "El Llanero", "atributos": (100, 20, 10)},
    {"nombre": "El Guaro", "atributos": (90, 22, 8)},
    {"nombre": "El Gocho", "atributos": (110, 18, 12)},
    {"nombre": "El Caribeno", "atributos": (85, 25, 5)}
]

# Acciones disponibles
acciones = ["atacar", "defender"]

# Mostrar personajes criollos disponibles
print("=== PERSONAJES VENEZOLANOS DISPONIBLES ===")
for i in range(len(personajes)):
    nombre = personajes[i]["nombre"]
    vida, ataque, defensa = personajes[i]["atributos"]
    print(f"{i+1}. {nombre} - Vida: {vida}, Ataque: {ataque}, Defensa: {defensa}")

# Selección del jugador
while True:
    seleccion = input("Escoge tu personaje (1 al 4): ")
    if seleccion in ["1", "2", "3", "4"]:
        jugador = personajes[int(seleccion) - 1]
        break
    else:
        print("¡Chamo! Esa opción no es válida. Intenta otra vez.")

# Selección del oponente (distinto al jugador)
while True:
    oponente = random.choice(personajes)
    if oponente != jugador:
        break

print(f"\nElegiste a {jugador['nombre']} pa' la pelea.")
print(f"Tu oponente será nada más y nada menos que {oponente['nombre']}.\n")

# Inicializar vida
jugador_vida = jugador["atributos"][0]
oponente_vida = oponente["atributos"][0]

turno = 1
while jugador_vida > 0 and oponente_vida > 0:
    print(f"\n=== RONDA {turno} ===")
    print(f"Tu vida: {jugador_vida} | Vida del pana {oponente['nombre']}: {oponente_vida}")

    # Acción del jugador
    while True:
        accion_jugador = input("¿Qué vas a hacer? (atacar/defender): ").lower()
        if accion_jugador in acciones:
            break
        else:
            print("Eso no se vale. Escribe 'atacar' o 'defender'.")

    # Acción aleatoria del oponente
    accion_oponente = random.choice(acciones)
    print(f"{oponente['nombre']} decide: {accion_oponente}")

    # Atributos
    jugador_ataque = jugador["atributos"][1]
    jugador_defensa = jugador["atributos"][2]
    oponente_ataque = oponente["atributos"][1]
    oponente_defensa = oponente["atributos"][2]

    # Lógica de combate
    if accion_jugador == "atacar":
        if accion_oponente == "atacar":
            jugador_vida -= max(0, oponente_ataque - jugador_defensa)
            oponente_vida -= max(0, jugador_ataque - oponente_defensa)
        elif accion_oponente == "defender":
            oponente_vida -= max(0, (jugador_ataque - oponente_defensa * 2))
    elif accion_jugador == "defender":
        if accion_oponente == "atacar":
            jugador_vida -= max(0, (oponente_ataque - jugador_defensa * 2))
        elif accion_oponente == "defender":
            print("Ambos se pusieron en guardia. Nadie atacó.")

    turno += 1

# Resultado del combate
print("\n=== RESULTADO FINAL ===")
if jugador_vida <= 0 and oponente_vida <= 0:
    print("¡Empate! Ambos cayeron como buenos guerreros criollos.")
elif jugador_vida <= 0:
    print(f"¡{oponente['nombre']} te ganó esta vuelta, pero no te achicopales!")
else:
    print(f"¡Ganaste, {jugador['nombre']}! Ahora sí, a celebrar con una empanada y un refresco.")
