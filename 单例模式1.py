class Single:
    __instance = None

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = Single(18, 'xxx')
b = Single(8, 'xx')

print(id(a))
print(id(b))

a.age = 20
print(b.age)
