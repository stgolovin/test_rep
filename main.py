class Person():
    def show_info(self):
        pass
        # print(self.name, self.surname)
    def get_age(self, k):
        print(f'His age is {k - self.year_of_birth} year.')

p1 = Person()
p1.name = 'Elon'
p1.surname = 'Musk'
p1.year_of_birth = 1971

p1.show_info()
p1.get_age(2022)