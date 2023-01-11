import random

class Randomier:
    count = 100

    def __init__(self):
        self.__val = self.rand_value()
        self.__id = Randomier.count
        Randomier.count += 3
        self.__name = str(self.id) + "@" + hex(id(self))

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, new):
        self.__name = new

    @name.getter
    def get_name(self):
        return self.__name

    @property
    def val(self):
        return self.__val

    @val.setter
    def set_val(self, new):
        self.__val = new

    @val.getter
    def get_val(self):
        return self.__val

    @property
    def id(self):
        return self.__id

    @id.setter
    def set_id(self, new):
        self.__id = new

    @name.getter
    def get_id(self):
        return self.__id

    @staticmethod
    def rand_value(donja=10, gornja=300):
        return random.randint(donja, gornja)

    def __str__(self):
        return self.id

    def __repr__(self):
        return  str(self.__class__) + " with ID:" + str(self.id)

    def __eq__(self, o: object):
        if self.id == o.id:
            return True
        else:
            return False