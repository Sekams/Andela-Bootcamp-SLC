class Car(object):
    """
        This class describes a class Car that can be used to instantiate various vehicles
    """
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, *arguments):
        self.speed = Car.speed
        self.type = 'saloon'

        if arguments and len(arguments) > 1:
            if arguments[0] == "Porshe" or arguments[0] == "Koenigsegg":
                self.num_of_doors = 2
            else:
                self.num_of_doors = Car.num_of_doors
            for argument in arguments:
                if arguments.index(argument) == 0:
                    self.name = argument
                elif arguments.index(argument) == 1:
                    self.model = argument
                elif len(arguments) > 2 and arguments.index(argument) == 2:
                    self.type = argument
                    if self.type == 'trailer':
                        self.num_of_wheels = 8
        else:
            self.name = 'General'
            self.model = 'GM'

    def is_saloon(self):
        if self.type == 'trailer':
            return False
        else:
            return True

    def drive(self, speed):
        if self.name == 'Mercedes':
            self.speed = speed * (1000 / 3)
        elif self.type == 'trailer':
            self.speed = speed * 11
        return self
