def second_largest(lista):
    # Verificamos que la lista tenga al menos dos elementos
    if len(lista) < 2:
        return None

    # Eliminamos duplicados y ordenamos la lista en orden descendente
    uniques_list = list(set(lista))
    uniques_list.sort(reverse=True)

    # Verificamos que haya al menos dos elementos únicos
    if len(uniques_list) < 2:
        return None

    # Retornamos el segundo más grande
    return uniques_list[1]

numeros = [10, 20, 4, 45, 99, 99, 45]
resultado = second_largest(numeros)
print(f"El segundo número más grande es: {resultado}")
