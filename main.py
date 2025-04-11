class Human:
    def sprint_right(self):
        pass

    def sprint_left(self):
        pass

    def sprint_up(self):
        pass

    def sprint_down(self):
        pass

    def __raise_if_cannot_sprint(self):
        pass

    def __use_sprint_stamina(self):
        pass

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina
