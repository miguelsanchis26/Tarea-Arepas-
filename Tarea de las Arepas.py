


def calcular_arepas(harina_str, agua_str, sal_str):
 
  try:
    # Convertir las cadenas de texto a números
    harina = int(harina_str)
    agua = int(agua_str)
    sal = int(sal_str)

    # La cantidad de agua debe ser suficiente
    if agua < (harina * 0.6):
      print("No hay suficiente agua para preparar las arepas.")
      return 0

    # Calcular la cantidad de arepas
    formula = harina / 250
    cantidad_arepas = min(formula, int(agua / 250))

    # Mostrar el resultado
    print(f"Con {harina} gramos de harina, {agua} ml de agua y {sal} cda de sal, se pueden preparar {cantidad_arepas} arepas.")
    return cantidad_arepas

  except ValueError:
    # Manejar el error de conversión de tipo
    print("Error: Los valores ingresados deben ser números.")
    return 0



# Pedirle todos los ingredientes al usuario
harina_str = input("Ingrese la cantidad de harina de maíz en gramos: ")
agua_str = input("Ingrese la cantidad de agua en ml: ")
sal_str = input("Ingrese la cantidad de sal en cdas: ")

# Para poder calcular la cantidad de arepas
cantidad_arepas = calcular_arepas(harina_str, agua_str, sal_str)
# Se muestra el resultado
if cantidad_arepas > 0:
  print(f"¡Buen provecho! Disfruta de tus {cantidad_arepas} arepas.")

