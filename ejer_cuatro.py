# En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas.
# Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
#  ¿Colon descubrió América?
#  ¿La independencia de México fue en el año 1810?
#  ¿The Doors fue un grupo de rock Americano?

rta_uno=input("¿Colon descubrió América? Si / no ").lower()
if rta_uno=="no":
    print("Perdiste ")
else:
    rta_dos=input("¿La independencia de México fue en el año 1810? Si / no ").lower()
    if rta_dos=="no":
        print("Perdiste")
    else:
        rta_tres=input("¿The Doors fue un grupo de rock Americano?Si / no ").lower()
        if rta_tres =="no":
            print("Perdiste")
        else:
            print("Ganastes")

        