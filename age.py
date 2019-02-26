import datetime

class Person():
    """
    Calculate birthday using datetime.
    """
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def age(self):
        b = datetime.date.today() - self.birthday
        return int(b.days/365)

    def __str__(self):
        return '%s, %d Years' %(self.name, self.age())

fulano = Person('Giovani', datetime.date(1982, 12, 29))
print(fulano.age())
print(fulano)