#Escreva uma função chamada middle que receba uma lista e retorne uma
#nova lista com todos os elementos originais, exceto o primeiro e o último
#elementos.

def middle(t):
    return t[1:-1]

if __name__ == "__main__":
    t = [1, 2, 5, 7, 3, 4]
    print(middle(t))
    