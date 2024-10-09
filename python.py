def registrar_notas():
    notas = []  # Lista para guardar las notas

    while True:
        nota = input("Ingresa una nota (o 'fin' para terminar): ")

        if nota == 'fin':  # Si el usuario escribe 'fin', se termina el ciclo
            break

        try: #Intenta convertir la entrada del usuario en un número flotante.
            nota = float(nota)  # Convierte la entrada a número
        except: #Si falla, muestra un mensaje de error y continúa con el siguiente ciclo.
            print("Por favor, ingresa un número válido.")
            continue

        if 0 <= nota <= 10:  # Acepta solo notas entre 0 y 10
            notas.append(nota)  # Agrega la nota a la lista (registrar_nota)
        else: #Muestra el promedio con dos decimales.
            print("La nota debe estar entre 0 y 10.")

    if notas:  # Si hay notas en la lista
        promedio = sum(notas) / len(notas)  # len() se utiliza para contar cuántas notas han sido ingresadas en la lista (notas).
        print(f"Promedio: {promedio:.2f}")

        if promedio >= 6: #Determina si el promedio es 6 o más.
            print("Aprobaste.")
        else: 
            print("No aprobaste.")
    else: #Imprime "No ingresaste ninguna nota" si no se registraron notas.
        print("No ingresaste ninguna nota.")

registrar_notas() #Llama a la función para ejecutar el proceso completo.
