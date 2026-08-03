#3/08/2026
"""
tính đóng gói
"""

class Person:
    def __init__(self, name, person_id, gender, age):
        self.__name = name
        self.__id = person_id
        self.__gender = gender
        self.__age = age

    def get_info(self):
        return {
            "name": self.__name,
            "id": self.__id,
            "gender": self.__gender,
            "age": self.__age,
        }

    def print_info(self):
        info = self.get_info()
        print("Name:", info["name"])
        print("ID:", info["id"])
        print("Gender:", info["gender"])
        print("Age:", info["age"])
    def print(self):
        print("Name:",self._name)
        print("Id:",self._id)
        print("Gender:",self._gender)
        print("Age:",self._age)
        

person = Person("Ngân", "25It2", "Nữ", 19)
person.print_info()
person.print
