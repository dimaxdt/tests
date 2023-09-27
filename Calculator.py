import math
class calc:
    def add(x, y):
        return x + y
    def sub(x, y):
        return x - y
    def mul(x, y):
        return x * y
    def div(x, y):
        return x / y
    def fac(z):
        return math.factorial(z)


def main():
    print("Данный калькулятор создан для операций только с двумя целыми числами, "
          "а для вычисления факториала, нужно ввести любые числа")
    x = int(input("Первое число: "))
    y = int(input("Второе число: "))
    action = input("Действие (+ - * / !): ")
    if action == "+":
        print("Сумма =", calc.add(x, y))
    elif action == "-":
        print("Разность =",calc.sub(x, y))
    elif action == "*":
        print("Произведение =", calc.mul(x, y))
    elif action == "/":
        print("Деление =", calc.div(x, y))
    elif action == "!":
        z = int(input("Введите целое число: "))
        print("Факториал числа =", calc.fac(z))
    else:
        print("NO")
    input("\n\nНажмите Enter, чтобы выйти.")


if __name__ == '__main__':
    main()