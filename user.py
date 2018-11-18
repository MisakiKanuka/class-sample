class User:
    def __init__(self, name, age, country):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country

    def display_profile(self):
        # display_profile()はUseクラスのインスタンスメゾット
        # print("私はBobです。USA出身の15歳です。")
        print(f"{self.name}国籍：{self.country}年齢：{self.age}")

    def change_nationality(self, country_name):
        self.country = country_name


if __name__ == "__main__":
    bob = User("Bob", 15, "USA") #Userクラスをインスタンス化
    # bob.display_profile()
    bob.change_nationality("China")
    bob.display_profile()

    #print(bob.name)

    tom = User("Tom", 57, "USA")
    tom.change_nationality("China")
    tom.display_profile()
    #print(tom.name)

    ken = User("Ken", 49, "JP")
    ken.change_nationality("China")
    ken.display_profile()
    #print(ken.name)
