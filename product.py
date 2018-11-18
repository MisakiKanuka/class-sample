class Product:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def discount(self, price):
        self.amount -= price
        # self.amount = self.amount price


if __name__ == "__main__":
    p1 = Product("iPhone", 100000)  # Productクラスのインスタンス化
    print(p1)
    print(p1.name)  # iPhone
    print(p1.amount)  # 100000
    p1.discoount(5000)
    print(p1.amount)  # 95000

    p2 = Product("MBA", 150000)  # Productクラスのインスタンス化S
    print(p2.name)  # MBA
    print(p2.amount)  # 150000
    p2.discount(9800)
    print(p2.amount)
