
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = min(x1, x2)
        self.__y1 = min(y1, y2)
        self.__x2 = max(x1, x2)
        self.__y2 = max(y1, y2)

    def get_left_x(self):
        return self.__x1

    def get_bottom_y(self):
        return self.__y1

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
