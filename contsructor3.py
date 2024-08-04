class MyClass:
    def __init__(self, public_var, protected_var, private_var):
        self.public_var = public_var
        self._protected_var = protected_var
        self.__private_var = private_var

obj = MyClass(1, 2, 3)
print(obj.public_var)  # Works
print(obj._protected_var)  # Works (but discouraged)
print(obj.__private_var)  # Error (name mangling)