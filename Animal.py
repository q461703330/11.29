import yaml

print('hello github')

class Animal:
    name:str = None
    color: str = "白色"
    age: int = 3
    sex: str = "雄"

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def shout(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")


class Cat(Animal):
    hair: str = "短毛"

    def __init__(self, name, color, age, sex, hair):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def shout(self):
        print(f"{self.name}会喵喵叫")


class Dog(Animal):
    hair: str = "长毛"

    def __init__(self, name, color, age, sex, hair):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def watch(self):
        print(f" {self.name}会看家")

    def shout(self):
        print(f"{self.name}会汪汪叫")


if __name__ == '__main__':
    with open("Animal.yml", encoding="UTF-8") as f:
        animal = yaml.safe_load(f)
    # hair = animal['default']['hair']
    # name = animal['default']['name']
    # color = animal['default']['color']
    # age = animal['default']['age']
    # sex = animal['default']['sex']

    hair = animal['cat']['hair']
    name = animal['cat']['name']
    color = animal['cat']['color']
    age = animal['cat']['age']
    sex = animal['cat']['sex']
    cat = Cat(name, color, age, sex, hair)
    print(f" 猫的姓名是:{name}\n", f"猫的颜色是:{color}\n", f"猫的年龄是:{age}\n", f"猫的性别是:{sex}\n", f"猫是毛发是:{hair}")

    print("\n")

    hair = animal['dog']['hair']
    name = animal['dog']['name']
    color = animal['dog']['color']
    age = animal['dog']['age']
    sex = animal['dog']['sex']
    dog = Dog(name, color, age, sex, hair)
    print(f" 狗的姓名是:{name}\n", f"狗的颜色是:{color}\n", f"狗的年龄是:{age}\n", f"狗的性别是:{sex}\n", f"狗是毛发是:{hair}")
    dog.shout()
    dog.watch()
