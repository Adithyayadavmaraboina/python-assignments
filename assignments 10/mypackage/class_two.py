# class_two.py - contains ClassTwo

# 7. Relative import - importing ClassOne into ClassTwo's module
from .class_one import ClassOne


class ClassTwo:
    def __init__(self, value):
        print("Constructor of ClassTwo called")
        self.value = value

    def show_value(self):
        print("Value stored in ClassTwo is:", self.value)
        return self.value

    def use_class_one(self):
        # demonstrating that ClassTwo can use ClassOne via the relative import above
        helper = ClassOne("Helper (created inside ClassTwo)")
        helper.greet()
