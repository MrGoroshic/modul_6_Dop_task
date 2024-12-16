import math

class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            return False
        else:
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("You entered the wrong color")

    def __is_valid_sides(self, *args):
        if len(args) != self.sides_count:
            return False
        else:
            for side in args:
                if not isinstance(side, int) or side < 0:
                    return False
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            print("You entered the wrong number of sides")
        else:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled = False):
        super().__init__(color, list(sides), filled)
        self.__color = color
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__radius = self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, list(sides), filled)
        self.__color = color
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_square(self):
        half = sum(self.__sides) / 2
        return (half * (half - self.__sides[0]) * (half - self.__sides[1]) * (half - self.__sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled= False):
        self.__color = color
        if len(sides) == 1:
            self.__sides = list(sides) * self.sides_count
        else:
            self.__sides = [1] * self.sides_count
        super().__init__(color, self.__sides, filled)

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())