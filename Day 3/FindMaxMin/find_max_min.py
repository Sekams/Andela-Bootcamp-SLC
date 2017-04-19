def find_max_min(argument):
    """
        This function returns an array containing the minimum and maximum numbers, respectively from a list argument.
    """

    if not not argument and isinstance(argument, list):
        argument.sort()
        mini = argument[0]
        maxi = argument[len(argument) - 1]
        if mini == maxi:
            return [len(argument)]
        return [mini, maxi]
