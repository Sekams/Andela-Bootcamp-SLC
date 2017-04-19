class Car(object):
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, *args):
        self.speed = Car.speed
        self.type = 'saloon'

        if args and len(args) > 1:
            if args[0] == "Porshe" or args[0] == "Koenigsegg":
                self.num_of_doors = 2
            else:
                self.num_of_doors = Car.num_of_doors
            for arg in args:
                if args.index(arg) == 0:
                    self.name = arg
                elif args.index(arg) == 1:
                    self.model = arg
                elif len(args) > 2 and args.index(arg) == 2:
                    self.type = arg
                    if self.type == 'trailer':
                        self.num_of_wheels = 8
                else:
                    setattr(self, arg, arg)
        else:
            self.name = 'General'
            self.model = 'GM'

    def is_saloon(self):
        if self.type == 'trailer':
            return Car.is_saloon
        else:
            self.type == 'saloon'
            return Car.is_saloon

    def drive(self, spd):
        if self.name == 'Mercedes':
            self.speed = spd * (1000 / 3)
        elif self.type == 'trailer':
            self.speed = spd * 11
        return self
