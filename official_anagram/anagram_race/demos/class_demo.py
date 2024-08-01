class Student:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.classes = []

    def add_class(self, class_name):
        self.classes.append(class_name)

    def get_classes(self):
        return self.classes

    
if __name__ == "__main__":
    julian = Student("Julian", "12/21")
    print(julian.birthday)
    julian.add_class("CS2")
    print(julian.get_classes())