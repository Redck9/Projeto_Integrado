PRICES = (0, 800, 1520, 2160, 2560, 3000)                   #preco ja com descontos todos

def group(basket):
    """agrupar em conjuntos de livros """
    b = basket.copy()

    while len(b) > 0:
        s = set(b)
        yield s                                             #yield para produzir uma sequencia de valores
        for book in s:
            b.remove(book)                                 

def total(basket):
    """ calcula o preco total para uma cesta de livros  """
    price = sum(PRICES[len(s)] for s in group(basket))
    
    if len(basket) % 8 == 0 and len(set(basket)) == 5:
        price -= 5 * len(basket)                            # se agruparmos 4 livros diferentes com 4 fica mais barato do que 5 com 3, logo ajustamos aqui o preco
    return price