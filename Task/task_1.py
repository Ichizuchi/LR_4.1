class Pair:
    def __init__(self, first, second):
        if not (isinstance(first, int) and isinstance(second, int)):
            raise ValueError("Оба поля должны быть целыми числами.")
        if first <= 0:
            raise ValueError("Поле first должно быть положительным числом.")
        if second <= 0:
            raise ValueError("Поле second должно быть положительным числом.")
        
        self.first = first
        self.second = second

    def read(self):
        try:
            first = int(input("Введите целое положительное число first (): "))
            second = int(input("Введите целое положительное число second (): "))
            self.__init__(first, second)
        except ValueError as e:
            print(f"Ошибка: {e}")
            exit(1)

    def display(self):
        print(f"first = {self.first}, second = {self.second}")

    def ipart(self):
        if self.second == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю.")
        return self.first // self.second


def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)


if __name__ == '__main__':
    pair = make_pair(5, 2)
    pair.display()
    print(f"Целая часть дроби: {pair.ipart()}")

    pair.read()
    pair.display()
    print(f"Целая часть дроби: {pair.ipart()}")
