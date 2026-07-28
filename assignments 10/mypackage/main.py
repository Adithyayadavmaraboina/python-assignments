# main.py - outside the package, uses classes from mypackage

# 3. Import using different methods

# Method 1: import the module, then access the class through it
import mypackage.class_one

# Method 2: import the class directly from the module
from mypackage.class_two import ClassTwo

# 6. Alias import
import mypackage.class_one as c1


print("----- 4. Using ClassOne (imported via 'import mypackage.class_one') -----")
obj1 = mypackage.class_one.ClassOne("Amit")
obj1.greet()


print("\n----- Using ClassTwo (imported via 'from mypackage.class_two import ClassTwo') -----")
obj2 = ClassTwo(100)
obj2.show_value()


print("\n----- 6. Using ClassOne via alias import (import mypackage.class_one as c1) -----")
obj3 = c1.ClassOne("Priya")
obj3.greet()


print("\n----- 7. ClassTwo using ClassOne internally (relative import inside the package) -----")
obj2.use_class_one()


print("\n----- Bonus: using the __init__.py shortcut imports -----")
# Because __init__.py imports ClassOne and ClassTwo, we could also do:
from mypackage import ClassOne, ClassTwo as CT2

obj4 = ClassOne("Karan")
obj4.greet()

obj5 = CT2(250)
obj5.show_value()


print("\n----- 5. Final summary demonstrating constructor execution order -----")
print("All constructors above printed a message the moment each object was created,")
print("which shows __init__() runs automatically during object creation.")
