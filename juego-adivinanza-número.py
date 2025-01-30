import random

def juego_adivinanza():
    # Generar un número del 1 al 100
    numeros_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False 
   
    # Primeras líneas del juego dónde se da la bienvenida
    print("¡Bienvenido al juego de adivinanza de número!")
    print("Debes adivinar un número entre 1 y 100")
    print("¡Intenta adivinarlo! Empecemos el juego")


    while not adivinado:
      #Solicitar un número del 1 al 100
       adivinanza = input("Introduzca un número entre el 1 al 100: ")

      # Verificar que la entrada sea un número
       if adivinanza.isdigit():
         adivinanza = int(adivinanza) # Lo estamos pasando de texto a entero
         intentos += 1

         if adivinanza < numeros_secreto:
            print(f"El número secreto es mayor a {adivinanza}")
         elif adivinanza > numeros_secreto:
            print(f"El número secreto en menor a {adivinanza} ")  
         elif adivinanza == numeros_secreto:
            print(f"¡Felicitaciones has GANADO el juego! El número {adivinanza} es el número secreto y lo has logrado en {intentos} intentos.") 
     

# Preguntar si el usuario desea jugar otra vez
         while True:  # Validar hasta obtener una respuesta válida
            opcion = input("\n¿Quieres jugar otra vez? (sí/no): ").lower()
            if opcion == "sí":
                print(f"Ok sigamos con el juego.")
                break  # Salir del bucle y reiniciar el juego
            elif opcion == "no":
                print("Gracias por jugar. ¡Hasta luego!")
                return  # Terminar el programa
            else:
                print("Respuesta no válida. Por favor, escribe 'sí' o 'no'.")



juego_adivinanza()
