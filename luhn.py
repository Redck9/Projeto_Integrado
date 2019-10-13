class Luhn:
    def __init__(self, cardNum):
        d = []
        while(cardNum > 0):
            d.append(cardNum % 10)
            cardNum //= 10

        self.d = d

    def addends(self):
        result = []
        for i in range(len(self.d)):
            digito = self.d[i]
            if i % 2 == 1: 
                digito = digito * 2
                if digito > 9:
                    digito = digito - 9

            result.append(digito)

        return result

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return self.checksum() % 10 == 0

    def create(cardNum):
        check_digit = (10 - Luhn(cardNum * 10).checksum() % 10) % 10
        return cardNum * 10 + check_digit
