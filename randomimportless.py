class RandomImportLess:
    def __init__(self, random_library):
        self.random_library = random_library

    def int_to_ten(self):
        print(self.random_library.randint(0,11))