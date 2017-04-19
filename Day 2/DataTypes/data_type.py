def data_type(argument):
    if isinstance(argument, str):
        return len(argument)
    elif argument is None:
        return "no value"
    elif isinstance(argument, bool):
        return argument
    elif isinstance(argument, int):
        if argument < 100:
            return 'less than 100'
        elif argument > 100:
            return 'more than 100'
        else: 
            return 'equal to 100'
    elif isinstance(argument, list):
        if len(argument) >= 3:
            return argument[2]
        else:
            return None 
