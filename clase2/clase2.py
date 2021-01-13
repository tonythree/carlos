def sumar(x, y):
    print("estoy dentro")
    resultado = x + y
    return resultado


if __name__ == "__main__":
    resultado1 = sumar(x=1, y=2)
    resultado2 = sumar(5, 5)
    print(resultado1)
    print(resultado2)
