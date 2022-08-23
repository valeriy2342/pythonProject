class Myiskl(Exception):

    def my_func(self, a, b):
        try:
            result = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} -- Нельзя делить на ноль")
        else:
            print(f"{a} / {b} = {result}")


iskl = Myiskl()
iskl.my_func(5, 12)
iskl.my_func(-51, 7)
iskl.my_func(67, 0)
