print('task 1')
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))



my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])



print(my_matrix.__add__())

print('task 2')
class Cloves:
    def __init__(self, W, H):
        self.W = W
        self.H = H

    def get_square_1(self):
        return self.W / 6.5 + 0.5

    def get_square_2(self):
        return self.H * 2 + 0.3

    @property
    def get_sq(self):
        return str(f'Общая площадь ткани \n'
                   f'{(self.W / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Cloves):
    def __init__(self, W, H):
        super().__init__(W, H)
        self.get_square_1 = round(self.W / 6.5 + 0.6)

    def __str__(self):
        return f'ткани на пальто {self.get_square_1}'


class Costume(Cloves):
    def __init__(self, W, H):
        super().__init__(W, H)
        self.get_square_2 = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'Ткани на костюм {self.get_square_2}'

coat = Coat(3, 6)
costume = Costume(2, 4)
print(coat)
print(costume)
print(coat.get_sq)
print(costume.get_sq)






