class Money:
    def __init__(self, rubles=0, kopecks=0):
        self.rubles = rubles + kopecks // 100
        self.kopecks = kopecks % 100

    def read(self):
        rubles = int(input("Введите рубли: "))
        kopecks = int(input("Введите копейки: "))
        self.__init__(rubles, kopecks)

    def display(self):
        print(f"{self.rubles},{self.kopecks:02d} руб.")

    def __add__(self, other):
        total_kopecks = (self.rubles + other.rubles) * 100 + self.kopecks + other.kopecks
        return Money(0, total_kopecks)

    def __sub__(self, other):
        total_kopecks_self = self.rubles * 100 + self.kopecks
        total_kopecks_other = other.rubles * 100 + other.kopecks
        return Money(0, total_kopecks_self - total_kopecks_other)

    def __mul__(self, factor):
        total_kopecks = int((self.rubles * 100 + self.kopecks) * factor)
        return Money(0, total_kopecks)

    def __truediv__(self, factor):
        total_kopecks = int((self.rubles * 100 + self.kopecks) / factor)
        return Money(0, total_kopecks)


if __name__ == '__main__':

    money1 = Money()
    money1.read()  
    money1.display()

    money2 = Money()
    money2.read()  
    money2.display()

    sum_money = money1 + money2
    print("Сумма двух сумм:")
    sum_money.display()

    diff_money = money1 - money2
    print("Разность двух сумм:")
    diff_money.display()

    product_money = money1 * 2
    print("Умножение суммы на 2:")
    product_money.display()

    quotient_money = money1 / 2
    print("Деление суммы на 2:")
    quotient_money.display()
