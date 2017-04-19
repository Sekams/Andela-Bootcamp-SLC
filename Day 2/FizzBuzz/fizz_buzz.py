def fizz_buzz(argument):
    if isinstance(argument, int):
        if argument % 3 == 0 and argument % 5 == 0:
            return 'FizzBuzz'
        elif argument % 3 == 0 and argument % 5 > 0:
            return 'Fizz'
        elif argument % 5 == 0 and argument % 3 > 0:
            return 'Buzz'
        else:
            return argument
