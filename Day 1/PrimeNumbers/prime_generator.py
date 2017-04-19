def prime_generator(argument):
    """ 
        The Function takes O(N^2) seconds where N is the number of inputs
    """
    if isinstance(argument, int):
        result = []
        for number in range(0, argument + 1):
            if number > 1:
                factor = 2
                while factor < number:
                    if number % factor == 0:
                        break
                    factor += 1
                else:
                    result.append(number)
        return result
    else:
        return None