import random;

def jugar():
    print("Bienvenidos a roca, papel o tijeras")
    r = print("R para Roca")
    p = print("P para Papel")
    t = print("T para Tijeras")
    jugador = input("Para jugar ingrese R, P o T respectivamente: ").lower()
    pc = random.choice(["r","p","t"])

    if (jugador == pc):
        return "Empate"
    if victoria(jugador,pc):
        return "Ganaste"
    else:
        return "Perdiste"


def victoria(jugador, pc):
    if (jugador == "r" and pc =="t") or (jugador == "t" and pc =="p") or (jugador == "p" and pc =="r"):
        return True
print(jugar())