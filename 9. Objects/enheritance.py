class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name}'


class Employee(Person):
    # __init__ нужно выполнить, чтобы устанавливать аттрибуты
    # Если удалить self.name, то аттрибут в подклассе не будет установлен
    # По правилу ICPO всегда будет вызываться только один метод, и это будет
    # тот, который ближе всего к экземпляру
    # Этот код работает, но нарушает принцип DRY
    # def __init__(self, name, id_number):
    #     self.name = name
    #     self.id_number = id_number
    # super() позволяет вызывать метод для родительского объекта без явного именования этого родителя.
    def __init__(self, name, id_number):
        super().__init__(name)
        self.id_number = id_number


e = Employee('empname', 1)
print(e.greet())
