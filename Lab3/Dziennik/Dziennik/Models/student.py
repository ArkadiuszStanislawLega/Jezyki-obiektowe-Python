from .grade import Grade


class Student:
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__surname = ""
        self.__grades = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def full_name(self):
        return f'{self.__name} {self.__surname}'

    @property
    def average_grade(self):
        sum_counter = 0
        number_of_grades = len(self.__grades)
        if number_of_grades > 0:
            for grade in self.__grades:
                sum_counter += grade.value
            return sum_counter/number_of_grades
        else:
            return sum_counter

    def __str__(self):
        return f'{self.__name} {self.__surname}'

    def __repr__(self):
        return f'{self.__name} {self.__surname}'

    def add_grade(self, rating: Grade):
        if isinstance(rating, Grade):
            self.__grades.append(rating)

    def print_grades(self):
        print(f'Oceny {self.full_name}: {self.__grades}')
