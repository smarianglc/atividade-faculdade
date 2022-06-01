#Escreva uma função chamada cumsum que receba uma lista de números e
#retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo
#elemento é a soma dos primeiros i+1 elementos da lista original. 

def consum (t):
    total = 0
    res = []

    for x in t:
        total += x
        res.append(total)
    return res

if __name__ == "__main__":
    t = [1, 2, 3]
    print(consum(t))