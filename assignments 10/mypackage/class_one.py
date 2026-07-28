# class_one.py - contains ClassOne

class ClassOne:
    def __init__(self, name):
        print("Constructor of ClassOne called")
        self.name = name

    def greet(self):
        print("Hello from ClassOne, my name is", self.name)
        return f"Greeting from {self.name}"
