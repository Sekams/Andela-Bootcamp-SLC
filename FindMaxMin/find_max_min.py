def find_max_min(argument):
    if not not argument and isinstance(argument, list):
        argument.sort()
        mini = argument[0]
        maxi = argument[len(argument) - 1]
        if mini == maxi:
            return [len(argument)]
        return [mini, maxi]
