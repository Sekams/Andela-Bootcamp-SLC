class Car(object):
    def __init__(self, **other_data):
        for key, value in other_data.items():
            setattr(self, key, value)
